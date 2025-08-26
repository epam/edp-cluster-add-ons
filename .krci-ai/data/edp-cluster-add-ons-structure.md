# EDP Cluster Add-ons Repository Instructions

This repository follows GitOps principles and uses Argo CD's App of Apps pattern to manage and deploy Kubernetes add-ons. It provides a structured approach to managing multiple clusters and their respective add-ons, enabling consistent deployment and configuration across environments.

## Repository Purpose

The edp-cluster-add-ons repository contains a collection of pre-configured Helm charts (add-ons) for Kubernetes clusters. It leverages GitOps principles and employs Argo CD's App of Apps pattern for streamlined deployment and management. This repository offers various ready-to-use Kubernetes add-ons that can be easily integrated into your cluster with any Managed Kubernetes distribution.

## Repository Structure

The repository follows this structure:
- `/argo-cd/` - Main Argo CD configuration for deploying and configuring Argo CD itself
- `/clusters/<cluster-name>/` - Directory for each cluster (e.g., core, prod, dev)
  - `/addons/` - Individual add-on Helm charts for the specific Kubernetes cluster
  - `/apps/` - App of Apps Helm chart referencing all add-ons for this cluster
  - `bootstrap-addons.yaml` - Initial Argo CD application to bootstrap the deployment
- `/docs/` - Documentation for the repository and add-ons

## Coding Standards and Patterns

### General Helm Chart Standards
- Maintain clear separation between add-on configuration and App of Apps configuration
- Use meaningful comments in templates and values files
- Follow Helm best practices for chart structure and templating
- Always validate templates with `helm lint` before committing

### Add-on Implementation Guidelines
- Each add-on should be self-contained in its own directory
- For existing Helm charts, use them as dependencies and create a wrapper chart
- Use the dependency chart name as the top-level key in values.yaml
- The App of Apps `values.yaml` should ONLY contain enable flags and namespace settings
- All custom logic and configuration for an add-on should be placed in the add-on's own `values.yaml` file

### GitOps Principles
- All changes to the cluster should be made through this repository
- All configuration should be declarative and version-controlled
- Avoid hardcoding sensitive information; use appropriate secret management

## When Helping Users

1. When helping users with adding new add-ons or adding new cluster directories:
    - Reference the pattern in `/docs/add-new-addon.md` and `/docs/add-new-cluster.md`
    - Ensure they follow the directory structure and naming conventions
    - Remind them to update the App of Apps configuration
    - Guide them through the quick start process if they're new to the repository

2. When suggesting code changes:
    - Respect the existing structure and patterns
    - Provide explanations for your suggestions
    - Consider potential impacts on other add-ons or the cluster as a whole

3. When answering questions:
    - Refer to existing documentation when appropriate, especially the `quick-start-guide.md`
    - Explain GitOps and Argo CD concepts as needed
    - Provide concrete examples based on the repository structure
