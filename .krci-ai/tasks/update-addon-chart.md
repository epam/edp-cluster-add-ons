# Task: Update Add-on Helm Chart

## Description

Automate and validate the process of updating a Helm chart (add-on) in the repository, ensuring compatibility and compliance with best practices. This task guides the DevOps agent through chart version upgrades, difference analysis, and user approval for critical changes.

## Prerequisites

- [ ] **Helm CLI installed**: Verify `helm` is available in the environment

### Reference Assets

Dependencies:

- ./.krci-ai/data/devops/devops-helm-k8s-standards.md

Validation: Verify the dependency exists at the specified path before proceeding. HALT if missing.

**IMPORTANT**: Do not change the path of the dependency.

## Overview

Your task is to update a Helm chart for an add-on in the repository. Follow the step-by-step implementation guide to ensure the chart is updated correctly, dependencies are managed, and user approval is obtained for critical commands. The process includes pulling current and desired chart versions, comparing them, and updating the chart version in the repository.

## Implementation Steps

### STEP-BY-STEP Implementation

1. **CRITICAL FIRST STEP**: Ask user to provide the add-on name and desired chart version. This is critical step for ensuring the correct chart is updated.

    **IMPORTANT**: User must provide the following information in one message:
        - **Add-on name**: The name of the add-on (helm chart) to update.
        - **Version**: The desired chart version (e.g., `1.2.3`) for the update.

2. **Locate chart**: Find the chart in `clusters/core/addons/{addon}/` directory and read the `Chart.yaml` file. Extract dependency chart name and repository link from the file. It is necessary for the next steps.
   - If the chart does not exist, notify the user and stop the process.
   - If the chart exists, proceed to the next step.

3. **Update Helm repo**: Run `helm repo add {chart name} {repository link} --force-update` command and fill in the `{chart name}` and `{repository link}` with the values extracted from `Chart.yaml`. This ensures the Helm CLI has the latest chart information. User must approve this command before execution.

4. **Pull current and desired chart versions**:
   - `helm pull {repo_name}/{chart_name} --version {current_version} --untar --untardir tmp/old`
   - `helm pull {repo_name}/{chart_name} --version {desired_version} --untar --untardir tmp/new`

    User must approve these commands before execution. Replace `{repo_name}`, `{chart_name}`, `{current_version}`, and `{desired_version}` with appropriate values.

5. **Compare chart versions**: To identify differences, run:
    - `diff -ruN tmp/old tmp/new`

    This command compares the current and desired chart versions, including manifests and `values.yaml` files. User must approve this command before execution.
    **IMPORTANT**: Do not add any additional command or flags to the `diff` command. It must be run exactly as specified.
    **IMPORTANT**: Delete the `tmp/old` and `tmp/new` directories after the comparison to clean up temporary files.

6. **Analyze differences**:
   - If changes affect manifests or `values.yaml`, notify user and propose solutions (e.g., API version changes, breaking changes)
   - Summarize findings and recommendations

7. **Update the chart version**: If the user approves, update the chart version in `Chart.yaml` and `values.yaml` files.

    **IMPORTANT**: After updating the chart version and related files depending on the changes, run `helm dependency build ./clusters/core/addons/atlantis/` and `helm template {addon} ./clusters/core/addons/{addon}/` commands to generate the updated manifests.Verify that the output does not contain any errors or warnings. User must approve this command before execution.
    **IMPORTANT**: Do not add any additional command or flags to the `helm template` command. It must be run exactly as specified. The command `helm dependency build` must be run before `helm template` to ensure all dependencies are correctly built.

## Output Format

- **User approval required**: All CLI commands must be approved by user before execution
