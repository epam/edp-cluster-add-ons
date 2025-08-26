# Task: Update Add-on Helm Chart

## Description

Provide guidance and recommendations to users who want to update a Helm chart (add-on) in the repository, ensuring compatibility and compliance with best practices. This task helps the DevOps agent advise users on the proper steps for updating chart versions, analyzing differences, and ensuring smooth upgrades.

### Reference Assets

Dependencies:

- ./docs/add-new-addon.md

Validation: Verify the dependencies exist at the specified paths before proceeding. HALT if missing.

**IMPORTANT**: Do not change the path of the dependencies.

## Overview

Your task is to provide guidance to users who want to update a Helm chart for an add-on in the repository. Instead of performing the actions yourself, you'll offer clear recommendations and best practices for the update process, focusing on version comparison, identifying breaking changes, and proper chart updates.

## Implementation Steps

### STEP-BY-STEP Recommendations

1. **Research release notes**: Recommend that the user check the official release notes or changelog for the Helm chart they want to update. Explain that this is crucial for:
   - Identifying breaking changes
   - Understanding new features
   - Being aware of deprecated functionality
   - Finding migration steps or special upgrade instructions

2. **Suggest version discovery**: Provide the following recommendations for discovering available versions:
   ```
   # Update Helm repositories
   helm repo update

   # List available versions for the chart
   helm search repo <chart-repo-name>/<chart-name> -l
   ```

3. **Recommend chart comparison**: Suggest the following approach to compare chart versions:
   ```
   # Pull the current and new chart versions
   helm pull <chart-repo>/<chart-name> --version <current-version> --untar --untardir tmp/old
   helm pull <chart-repo>/<chart-name> --version <desired-version> --untar --untardir tmp/new

   # Compare the two versions
   diff -ruN tmp/old tmp/new
   ```

   Also mention that they can use comparison tools in their IDE if they prefer.

4. **Provide analysis guidance**: Recommend looking for the following during comparison:
   - Changes to default values in `values.yaml`
   - New required values or parameters
   - Removed values or parameters
   - Changes to CRD (Custom Resource Definition) resources
   - API version changes in templates
   - Structural changes to templates
   - Changes in dependencies

5. **Updating the chart**: Suggest the following steps to update the add-on:
   - Update the dependency version in the add-on's `Chart.yaml` file
   - Update the chart version and appVersion fields
   - Make necessary changes to the add-on's `values.yaml` based on the comparison
   - Run `helm dependency update` in the add-on directory to download the new dependencies

6. **Testing recommendations**: Suggest testing the updated chart before committing:
   ```
   # Lint the chart to check for issues
   helm lint ./clusters/core/addons/<addon-name>

   # Render the templates to verify they generate correctly
   helm template <addon-name> ./clusters/core/addons/<addon-name>
   ```

7. **Documentation updates**: Recommend the following:
   - Update the add-on's README.md if necessary
   - Run `helm-docs` in the add-on directory to update auto-generated documentation
   - Run `make update-readme` in the repository root to update the main README

8. **Final validation**: Suggest testing the chart in a non-production environment before applying it to production.

**NOTES**:
- The agent should ONLY provide guidance and recommendations, not attempt to execute commands or update files itself
- Emphasize the importance of checking release notes and understanding breaking changes
- Remind users to always test chart updates in a non-production environment first
- Suggest incremental updates for charts that are several versions behind
