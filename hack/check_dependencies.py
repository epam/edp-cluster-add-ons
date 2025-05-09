import os
import subprocess
import glob
import yaml
import re
import sys
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


def get_latest_version(name: str, repo: str) -> str:
    """Get the latest version of a chart from its repository"""
    if not repo or repo == "-":
        return "-"

    repo_alias = f"{name}-repo"

    try:
        if not repo.startswith("oci://"):
            # Search for the chart in the repository (which should already be added)
            result = subprocess.run(
                ["helm", "search", "repo", f"{repo_alias}/{name}", "-o", "yaml"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                check=False
            )

            if result.returncode == 0 and result.stdout:
                try:
                    chart_data = yaml.safe_load(result.stdout)
                    if chart_data and isinstance(chart_data, list) and len(chart_data) > 0:
                        return chart_data[0].get("version", "-")
                except Exception:
                    pass
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
                    return chart_info.get("version", "-")
                except Exception:
                    pass
    except Exception as e:
        print(f"Warning: Error checking latest version for {name}: {e}", file=sys.stderr)

    return "-"


def process_chart(chart_path: str) -> List[Tuple[str, str, str, str]]:
    """Process a Chart.yaml file and return dependency information"""
    results = []

    try:
        with open(chart_path, 'r') as f:
            chart_data = yaml.safe_load(f)

        # If chart has no dependencies section or empty dependencies
        if not chart_data.get("dependencies"):
            dir_name = get_chart_name_from_path(chart_path)
            results.append((dir_name, "-", "-", chart_path))
            return results

        # Process dependencies
        for dep in chart_data.get("dependencies", []):
            name = dep.get("name", "")
            version = dep.get("version", "")
            repo = dep.get("repository", "")

            # Handle incomplete dependencies
            if not name:
                name = get_chart_name_from_path(chart_path)
            if not version:
                version = "-"
            if not repo:
                repo = "-"
                latest_version = "-"
            else:
                latest_version = get_latest_version(name, repo)

            results.append((name, version, latest_version, chart_path))

        # If no results were created but dependencies existed, use directory name
        if not results and chart_data.get("dependencies"):
            dir_name = get_chart_name_from_path(chart_path)
            results.append((dir_name, "-", "-", chart_path))

    except Exception as e:
        print(f"Warning: Error processing {chart_path}: {e}", file=sys.stderr)
        dir_name = get_chart_name_from_path(chart_path)
        results.append((dir_name, "-", "-", chart_path))

    return results


def print_table(all_dependencies: List[Tuple[str, str, str, str]]) -> None:
    """Print the dependency table in the required format"""
    header = "+--------------------------+-----------------+-----------------+--------------------------------------------------------+"
    print(header)
    print("| Dependency Name          | Current Version | Latest Version  | Path                                                   |")
    print(header)

    # Sort dependencies by name (first element in each tuple)
    sorted_dependencies = sorted(all_dependencies, key=lambda x: x[0].lower())

    for name, version, latest, path in sorted_dependencies:
        print(f"| {name:<24} | {version:<15} | {latest:<15} | {path:<54} |")

    print(header)


def main():
    """Main function to check dependencies"""
    print("Finding Chart.yaml files...", file=sys.stderr)
    chart_files = find_chart_files()
    print(f"Found {len(chart_files)} Chart.yaml files", file=sys.stderr)

    # First pass: collect all repositories
    repos = collect_helm_repos(chart_files)

    # Add all repositories at once
    add_helm_repos(repos)

    # Update repositories once
    update_helm_repos()

    # Second pass: process dependencies and get versions
    all_dependencies = []

    print("Processing chart dependencies...", file=sys.stderr)
    if TQDM_AVAILABLE:
        chart_iterator = tqdm(
            chart_files,
            desc="Checking versions",
            unit="chart",
            ncols=100,
            bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
        )
    else:
        chart_iterator = chart_files

    for chart_path in chart_iterator:
        if not TQDM_AVAILABLE:
            print(f"Processing {chart_path}...", file=sys.stderr)
        dependencies = process_chart(chart_path)
        all_dependencies.extend(dependencies)

    print("\nGenerating dependency table...", file=sys.stderr)
    print_table(all_dependencies)


if __name__ == "__main__":
    main()
