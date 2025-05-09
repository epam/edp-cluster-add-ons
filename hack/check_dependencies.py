import os
import subprocess
import glob
import yaml
import sys
import concurrent.futures
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    print("Warning: tqdm not installed. Run 'pip install -r hack/requirements.txt' for progress bars.", file=sys.stderr)


def collect_helm_repos(chart_files: List[str]) -> Dict[str, str]:
    """Collect all unique Helm repositories from Chart.yaml files"""
    repos = {}

    print("Collecting Helm repositories...", file=sys.stderr)

    if TQDM_AVAILABLE:
        chart_iterator = tqdm(
            chart_files,
            desc="Scanning charts for repositories",
            unit="chart",
            ncols=100,
            bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
        )
    else:
        chart_iterator = chart_files

    for chart_path in chart_iterator:
        try:
            with open(chart_path, 'r') as f:
                chart_data = yaml.safe_load(f)

            if not chart_data or not chart_data.get("dependencies"):
                continue

            for dep in chart_data.get("dependencies", []):
                name = dep.get("name", "")
                repo = dep.get("repository", "")

                if name and repo and not repo.startswith("oci://") and repo != "-":
                    repo_alias = f"{name}-repo"
                    repos[repo_alias] = repo

        except Exception as e:
            print(f"Warning: Error scanning repository in {chart_path}: {e}", file=sys.stderr)

    return repos


def add_helm_repos(repos: Dict[str, str]) -> None:
    """Add all collected Helm repositories"""
    if not repos:
        return

    print(f"Adding {len(repos)} unique Helm repositories...", file=sys.stderr)

    if TQDM_AVAILABLE:
        repo_iterator = tqdm(
            repos.items(),
            desc="Adding repositories",
            unit="repo",
            ncols=100,
            bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
        )
    else:
        repo_iterator = repos.items()

    for repo_alias, repo_url in repo_iterator:
        try:
            subprocess.run(
                ["helm", "repo", "add", repo_alias, repo_url, "--force-update"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False
            )
        except Exception as e:
            print(f"Warning: Failed to add repository {repo_url}: {e}", file=sys.stderr)


def update_helm_repos() -> None:
    """Update all Helm repositories"""
    print("Updating Helm repositories...", file=sys.stderr)
    try:
        subprocess.run(["helm", "repo", "update"],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,
                       check=False)
    except Exception as e:
        print(f"Warning: Failed to update Helm repositories: {e}", file=sys.stderr)


def find_chart_files() -> List[str]:
    """Find all Chart.yaml files in the clusters directory"""
    return glob.glob("clusters/core/addons/**/Chart.yaml", recursive=True)


def get_chart_name_from_path(chart_path: str) -> str:
    """Extract the chart name from its path"""
    return os.path.basename(os.path.dirname(chart_path))


def get_latest_version(name: str, repo: str, current_version: str = "") -> Tuple[str, str]:
    """Get the latest version and appVersion of a chart from its repository

    Args:
        name: Name of the chart
        repo: Repository URL
        current_version: Current version of the chart to filter results (optional)
        Note: current_version is kept for API compatibility but not used for filtering

    Returns:
        Tuple[str, str]: A tuple with (version, appVersion)
    """
    if not repo or repo == "-":
        return "-", "-"

    repo_alias = f"{name}-repo"

    try:
        if not repo.startswith("oci://"):
            # Search for the chart in the repository with all versions (which should already be added)
            cmd = ["helm", "search", "repo", f"{repo_alias}/{name}", "--versions", "-o", "json"]

            # We're not using version filtering because it limits results to the same major version
            # We want to show all available versions, especially major upgrades

            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                check=False
            )

            if result.returncode == 0 and result.stdout:
                try:
                    import json
                    chart_data = json.loads(result.stdout)
                    if chart_data and isinstance(chart_data, list) and len(chart_data) > 0:
                        # First entry is the latest version
                        version = chart_data[0].get("version", "-")
                        # Use app_version instead of appVersion since that's what the JSON output from helm uses
                        app_version = chart_data[0].get("app_version", "-")
                        return version, app_version
                except Exception as e:
                    print(f"Warning: Error parsing JSON for {name}: {e}", file=sys.stderr)
        else:
            # For OCI repositories
            result = subprocess.run(
                ["helm", "show", "chart", f"{repo}/{name}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                check=False
            )

            if result.returncode == 0 and result.stdout:
                try:
                    chart_info = yaml.safe_load(result.stdout)
                    version = chart_info.get("version", "-")
                    app_version = chart_info.get("appVersion", "-")
                    return version, app_version
                except Exception:
                    pass
    except Exception as e:
        print(f"Warning: Error checking latest version for {name}: {e}", file=sys.stderr)

    return "-", "-"


def process_chart(chart_path: str) -> List[Tuple[str, str, str, str, str, str]]:
    """Process a Chart.yaml file and return dependency information

    Returns:
        List[Tuple[str, str, str, str, str, str]]: List of tuples with
            (name, current_version, current_appversion, latest_version, latest_appversion, chart_path)
    """
    results = []

    try:
        with open(chart_path, 'r') as f:
            chart_data = yaml.safe_load(f)

        # If chart has no dependencies section or empty dependencies
        if not chart_data.get("dependencies"):
            dir_name = get_chart_name_from_path(chart_path)
            # Try to get version and appVersion from the chart itself
            chart_version = chart_data.get("version", "-")
            chart_app_version = chart_data.get("appVersion", "-")
            results.append((dir_name, chart_version, chart_app_version, "-", "-", chart_path))
            return results

        # Process dependencies
        for dep in chart_data.get("dependencies", []):
            name = dep.get("name", "")
            version = dep.get("version", "")
            app_version = dep.get("appVersion", "-")
            repo = dep.get("repository", "")

            # If not specified in the dependency, try to get app version from parent chart's appVersion
            if app_version == "-":
                # For direct dependencies, the parent chart might have the appVersion
                if chart_data.get("appVersion"):
                    app_version = chart_data.get("appVersion")

            # Try to get app version from the referenced chart if still not found
            if app_version == "-" and repo and name:
                # First try to look for installed chart in the charts/ directory
                chart_dir = os.path.dirname(chart_path)
                chart_lock_path = os.path.join(chart_dir, "Chart.lock")

                if os.path.exists(chart_lock_path):
                    try:
                        with open(chart_lock_path, 'r') as f:
                            lock_data = yaml.safe_load(f)

                            # Find the matching dependency in the lock file
                            for lock_dep in lock_data.get("dependencies", []):
                                if lock_dep.get("name") == name:
                                    # Try to find the chart file based on the locked version
                                    locked_version = lock_dep.get("version")
                                    chart_tgz = os.path.join(chart_dir, "charts", f"{name}-{locked_version}.tgz")

                                    if os.path.exists(chart_tgz):
                                        # Extract app version from the chart archive
                                        try:
                                            result = subprocess.run(
                                                ["helm", "show", "chart", chart_tgz],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.DEVNULL,
                                                text=True,
                                                check=False
                                            )
                                            if result.returncode == 0:
                                                chart_info = yaml.safe_load(result.stdout)
                                                app_version = chart_info.get("appVersion", "-")
                                        except Exception:
                                            pass
                    except Exception:
                        pass

            # Handle incomplete dependencies
            if not name:
                name = get_chart_name_from_path(chart_path)
            if not version:
                version = "-"
            if not repo:
                repo = "-"
                latest_version = "-"
                latest_app_version = "-"
            else:
                latest_version, latest_app_version = get_latest_version(name, repo, version)

            results.append((name, version, app_version, latest_version, latest_app_version, chart_path))

        # If no results were created but dependencies existed, use directory name
        if not results and chart_data.get("dependencies"):
            dir_name = get_chart_name_from_path(chart_path)
            results.append((dir_name, "-", "-", "-", "-", chart_path))

    except Exception as e:
        print(f"Warning: Error processing {chart_path}: {e}", file=sys.stderr)
        dir_name = get_chart_name_from_path(chart_path)
        results.append((dir_name, "-", "-", "-", "-", chart_path))

    return results


def print_table(all_dependencies: List[Tuple[str, str, str, str, str, str]]) -> None:
    """Print the dependency table in the required format"""
    header = "+--------------------------+-----------------+-----------------+-----------------+-----------------+--------------------------------------------------------+"
    print(header)
    print("| Dependency Name          | Current Version | Current AppVer  | Latest Version  | Latest AppVer   | Path                                                   |")
    print(header)

    # Sort dependencies by name (first element in each tuple)
    sorted_dependencies = sorted(all_dependencies, key=lambda x: x[0].lower())

    for name, version, app_version, latest_version, latest_app_version, path in sorted_dependencies:
        print(f"| {name:<24} | {version:<15} | {app_version:<15} | {latest_version:<15} | {latest_app_version:<15} | {path:<54} |")

    print(header)


def main():
    """Main function to check dependencies"""
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description="Check Helm chart dependencies for updates.")
    parser.add_argument("--workers", "-w", type=int, default=5,
                        help="Number of parallel workers for processing charts (default: 5)")
    args = parser.parse_args()

    print("Finding Chart.yaml files...", file=sys.stderr)
    chart_files = find_chart_files()
    print(f"Found {len(chart_files)} Chart.yaml files", file=sys.stderr)

    # First pass: collect all repositories
    repos = collect_helm_repos(chart_files)

    # Add all repositories at once
    add_helm_repos(repos)

    # Update repositories once
    update_helm_repos()

    # Second pass: process dependencies and get versions with parallel execution
    all_dependencies = []

    print(f"Processing chart dependencies in parallel with {args.workers} workers...", file=sys.stderr)

    # Use the number of workers specified in command line arguments
    max_workers = args.workers

    # Use ThreadPoolExecutor to process charts in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all chart processing tasks
        future_to_chart = {executor.submit(process_chart, chart_path): chart_path for chart_path in chart_files}

        # Setup progress bar if available
        if TQDM_AVAILABLE:
            futures_iterator = tqdm(
                concurrent.futures.as_completed(future_to_chart),
                total=len(chart_files),
                desc="Checking versions",
                unit="chart",
                ncols=100,
                bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
            )
        else:
            futures_iterator = concurrent.futures.as_completed(future_to_chart)

        # Process completed tasks as they finish
        for future in futures_iterator:
            chart_path = future_to_chart[future]
            try:
                if not TQDM_AVAILABLE:
                    print(f"Processing {chart_path}...", file=sys.stderr)
                dependencies = future.result()
                all_dependencies.extend(dependencies)
            except Exception as e:
                print(f"Error processing {chart_path}: {e}", file=sys.stderr)

    print("\nGenerating dependency table...", file=sys.stderr)
    print_table(all_dependencies)


if __name__ == "__main__":
    main()
