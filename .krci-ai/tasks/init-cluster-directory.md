# Task: Initialize New Cluster Directory

## Description

Automate and validate the process of initializing a new cluster directory in the cluster-add-ons repository. This task guides the DevOps agent through the creation of the directory structure, initial configuration files, and integration of add-ons, following repository conventions and best practices.

## Prerequisites

- [ ] **Helm CLI installed**: Verify `helm` is available in the environment

### Reference Assets

Dependencies:

- ./docs/add-new-cluster.md
- ./docs/add-new-addon.md
- ./.krci-ai/data/devops/edp-cluster-add-ons-structure.md

Validation: Verify both dependencies exist at the specified paths before proceeding. HALT if any missing.

**IMPORTANT**: Do not change the path of the dependencies.

## Overview

Your task is to initialize a new cluster directory in the repository, following the step-by-step guide and best practices described in the reference assets. The process includes creating the directory structure, initial Argo CD application, add-ons directory, App of Apps Helm chart, and updating documentation.

## Instructions

1. **Analyze the repository structure**: Refer to the [EDP Cluster Add-ons Repository Instructions](./.krci-ai/data/devops/edp-cluster-add-ons-structure.md) to understand the expected directory layout and naming conventions.
2. **Analyze the documentation**: Review the [add-new-cluster.md](./docs/add-new-cluster.md) and [add-new-addon.md](./docs/add-new-addon.md) files for precise instructions on how to create a new cluster directory and add new add-ons.
3. **Follow the step-by-step implementation guide**: Use the [add-new-cluster.md](./docs/add-new-cluster.md) as a roadmap for creating the new cluster directory, ensuring all required files and directories are created and configured correctly.

## Implementation Steps

### STEP-BY-STEP Implementation

1. **CRITICAL FIRST STEP**: Ask the user to provide the cluster name.

2. Follow the steps outlined in the [add-new-cluster.md](./docs/add-new-cluster.md) to create the new cluster directory.

3. **IMPORTANT NOTES**:
    - You can use already existing add-on directories with Helm charts as template for the new cluster.
    - **IMPORTANT**: You must refer to the already existing add-on directories to ensure the new cluster directory follows the correct structure and naming conventions.
    - You need to create at least one add-on directory in the `clusters/<cluster-name>/addons/` directory. You can use an existing add-on from another cluster as a template.

## Success Criteria

- [ ] **Cluster directory created**: All required directories and files exist
- [ ] **Initial Argo CD application present**: `bootstrap-addons.yaml` created and configured
- [ ] **App of Apps chart scaffolded**: Helm chart present in `apps/` directory
- [ ] **values.yaml configured**: Minimal configuration present
- [ ] **Documentation updated**: User reminded to update `README.md` and chart metadata
- [ ] **Reference assets validated**: Both `add-new-cluster.md` and `add-new-addon.md` exist

---

**Note:** For full details and examples, refer to `docs/add-new-cluster.md` and `docs/add-new-addon.md` in the repository.
