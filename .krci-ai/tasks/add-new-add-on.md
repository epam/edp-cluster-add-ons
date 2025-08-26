# Task: Add New Add-on to Cluster

# Description

Automate and validate the process of adding a new add-on (Helm chart) to an existing cluster directory in the cluster-add-ons repository. This task guides the DevOps agent through the creation of the add-on directory, initial configuration files, and integration into the App of Apps Helm chart, following repository conventions and best practices.

### Reference Assets

**Primary Dependencies**:

- Add new add-on guide: [add-new-addon.md](./../../docs/add-new-addon.md)
- Add new cluster guide: [add-new-cluster.md](./../../docs/add-new-cluster.md)
- edp-cluster-add-ons repository structure: [edp-cluster-add-ons-structure.md](./.krci-ai/data/edp-cluster-add-ons-structure.md)
- DevOps Helm and Kubernetes standards: [devops-helm-k8s-standarts.md](./.krci-ai/data/devops-helm-k8s-standards.md)

Validation: Verify the dependencies exist at the specified paths before proceeding. HALT if any are missing.

**IMPORTANT**: Do not change the path of the dependencies.

## Overview

Your task is to add a new add-on to an existing cluster directory in the repository, following the step-by-step guide and best practices described in the reference assets. The process includes creating the add-on directory, initial Helm chart files, updating the App of Apps Helm chart, and ensuring proper configuration.

## Instructions

1. **Analyze the documentation**: Review the [add-new-cluster.md](../../docs/add-new-cluster.md) and [add-new-addon.md](../../docs/add-new-addon.md) files for precise instructions on how to add a new add-on to an existing cluster directory.

**DO NOT**: Continue until analyzing the [add-new-cluster.md](../../docs/add-new-cluster.md) and [add-new-addon.md](../../docs/add-new-addon.md) files.

## Implementation Steps

### STEP-BY-STEP Implementation

1. **IMPORTANT FIRST STEP**: Ask the user to provide the following information:

    - Cluster name (the cluster to which the add-on will be added) (REQUIRED)
    - Add-on name (the name of the add-on/Helm chart to be added) (REQUIRED)
    - The Chart version (e.g., `1.2.3`) for the add-on (OPTIONAL, if not provided, use the latest stable version)

2. **IMPORTANT** Use the [add-new-addon.md](../../docs/add-new-addon.md) documentation as a step-by-step guide to create the add-on directory and necessary files.

**NOTES**:
- **DO NOT**: Run testing or linting commands. Only notify the user to run them manually after the process is complete.