---
mode: 'agent'
description: 'Get started with the EDP Cluster Add-ons repository'
---
# Getting Started with EDP Cluster Add-ons

I'll help you get started with the EDP Cluster Add-ons repository. This repository follows GitOps principles and uses Argo CD's App of Apps pattern to manage and deploy Kubernetes add-ons.

## Repository Overview

The repository is structured as follows:
- `/argo-cd/` - Main Argo CD configuration
- `/clusters/core/addons/` - Individual add-on Helm charts
- `/clusters/core/apps/` - App of Apps Helm chart referencing all add-ons
- `/docs/` - Documentation for the repository and add-ons

## Key Concepts

1. **App of Apps Pattern**: A central Argo CD application that manages multiple child applications
2. **Wrapper Charts**: Custom Helm charts that include existing charts as dependencies
3. **Configuration Separation**: Add-on specific configuration stays in the add-on's values.yaml
4. **GitOps Workflow**: All changes to the cluster come through this repository

## Common Tasks

I can help you with:

1. **Adding a new add-on**:
   - Creating a new add-on directory and Helm chart
   - Setting up dependencies for existing charts
   - Integrating with the App of Apps

2. **Updating existing add-ons**:
   - Upgrading chart versions
   - Modifying configuration
   - Testing changes

3. **Troubleshooting**:
   - Diagnosing deployment issues
   - Verifying chart structure
   - Checking Argo CD integration

4. **Development workflow**:
   - Local testing with kind
   - Chart validation
   - Pull request process

## Next Steps

What would you like to learn more about or work on first?

- Add a new add-on to the repository
- Update an existing add-on
- Understand the repository structure in more detail
- Learn about the testing process
