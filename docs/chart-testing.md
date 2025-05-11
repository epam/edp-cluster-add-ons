# Chart Testing

This document explains how to use and customize the chart-testing configuration for this repository.

## Overview

The chart-testing pipeline is configured to run automatically on pull requests that modify Helm chart-related files (YAML files, templates, Chart.yaml, etc.) within the `clusters` directory. It:

1. Lints all charts to ensure they follow best practices
2. Validates chart structure and schema
3. Installs charts in a kind cluster (Kubernetes v1.32) to ensure they deploy successfully
4. Runs Helm tests to validate chart functionality

## Configuration

### GitHub Actions Workflow

The main workflow is defined in `.github/workflows/chart-testing.yml`. It:

- Runs on pull requests that modify chart-related files in the `clusters` directory
- Uses a two-job approach:
  1. **Lint Job**: Validates chart syntax and best practices
  2. **Install and Test Job**: Sets up a kind cluster with Kubernetes v1.32, installs charts, and runs Helm tests
- Only creates the kind cluster if there are actually changed charts (optimization)
- Uses chart-testing to detect, lint, install, and test charts

### Chart Testing Configuration

The chart-testing configuration is in `ct.yaml` at the root of the repository. Key settings include:

- `chart-dirs`: Directories containing Helm charts to test (clusters/core/addons only)
- `helm-extra-args`: Additional arguments to pass to Helm during installation
- `target-branch`: The target branch to compare changes against
- `check-version-increment`: Ensures chart version is incremented when changes are made
- `lint-conf`: Points to the `lint-conf.yaml` file containing linting rules and configuration
- `chart-repos`: Additional Helm repositories required for dependencies

### Linting Configuration

The linting configuration is defined in `lint-conf.yaml` at the root of the repository. This file contains rules for chart validation, including:

- **Rules for Chart Requirements**: Enforces best practices like requiring README files, NOTES.txt files, and proper maintainer information
- **Validation Rules**: Validates chart names, versions, and Kubernetes schema compatibility
- **Excluded Charts**: Allows excluding certain charts from linting (useful for work-in-progress charts)
- **Custom Lint Values**: Enables specifying additional values files for linting

These rules help ensure that all charts in the repository maintain consistent quality and follow Helm best practices.

## Local Testing

You can run the same tests locally before submitting a pull request. The project includes several Makefile targets to help with testing:

1. Install chart-testing tool (for macOS):

   ```bash
   # For Apple Silicon (M1/M2)
   curl -L https://github.com/helm/chart-testing/releases/latest/download/chart-testing_darwin_arm64.tar.gz | tar xvz -C /tmp
   chmod +x /tmp/ct
   sudo mv /tmp/ct /usr/local/bin/ct

   # For Intel Macs
   curl -L https://github.com/helm/chart-testing/releases/latest/download/chart-testing_darwin_amd64.tar.gz | tar xvz -C /tmp
   chmod +x /tmp/ct
   sudo mv /tmp/ct /usr/local/bin/ct
   ```

2. View all available Makefile targets:

   ```bash
   make help
   ```

3. Run basic chart linting with chart-testing:

   ```bash
   make test-charts
   ```

4. Run advanced linting with all rules defined in lint-conf.yaml:

   ```bash
   make lint-all-charts
   ```

5. Lint a specific chart using the rules:

   ```bash
   make lint-chart CHART=argo-cd
   ```

6. Work with kind clusters for testing:

   ```bash
   # Create a kind cluster using the configuration file
   make kind-create

   # Run a comprehensive test cycle (advanced lint, install, tests)
   make test-charts-full

   # Delete the kind cluster when done
   make kind-delete
   ```

## Understanding Test Targets

The Makefile includes several testing targets with different purposes:

- **`test-charts`**: Basic linting of all charts with chart-testing, no installation
- **`lint-all-charts`**: Advanced linting using the rules in lint-conf.yaml for all charts
- **`lint-chart`**: Advanced linting for a specific chart
- **`kind-create`**: Creates a kind cluster with Kubernetes v1.32 for testing
- **`kind-delete`**: Removes the kind cluster used for testing
- **`test-charts-full`**: Comprehensive workflow combining advanced linting, installation and Helm tests

## Chart Change Detection

The chart-testing tool has a built-in capability to detect which charts have changed compared to a target branch. This is configured in the `ct.yaml` file:

```yaml
remote: origin
target-branch: main
```

With these settings, chart-testing will:

1. Compare your current working branch to the main branch
2. Identify charts that have changes in their files
3. Only process those changed charts

This mechanism is used by the GitHub Actions workflow to avoid testing unchanged charts. When you create a PR, the workflow will automatically detect chart changes and only test the modified charts, making the process more efficient.

## Customizing Chart Testing

To modify which charts are tested or change testing parameters:

1. Edit `ct.yaml` to add/remove chart directories or change validation settings
2. Edit `kind-config.yaml` to customize the kind cluster configuration
3. Update the GitHub Actions workflow in `.github/workflows/chart-testing.yml` if needed

For more information on chart-testing options, see the [chart-testing documentation](https://github.com/helm/chart-testing).
