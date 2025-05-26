# EDP Cluster Add-ons Repository Instructions

This repository follows GitOps principles and uses Argo CD's App of Apps pattern to manage and deploy Kubernetes add-ons. These instructions will guide GitHub Copilot in providing consistent and accurate assistance when working with this repository.

## Repository Structure

The repository follows this structure:
- `/argo-cd/` - Main Argo CD configuration
- `/clusters/core/addons/` - Individual add-on Helm charts
- `/clusters/core/apps/` - App of Apps Helm chart referencing all add-ons
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
- The App of Apps values.yaml should ONLY contain enable flags and namespace settings

### GitOps Principles
- All changes to the cluster should be made through this repository
- All configuration should be declarative and version-controlled
- Avoid hardcoding sensitive information; use appropriate secret management

## When Helping Users

1. When helping users add new add-ons:
   - Reference the pattern in `/docs/add-new-addon.md`
   - Ensure they follow the directory structure and naming conventions
   - Remind them to update the App of Apps configuration
   - Suggest appropriate testing steps

2. When suggesting code changes:
   - Respect the existing structure and patterns
   - Provide explanations for your suggestions
   - Consider potential impacts on other add-ons or the cluster as a whole

3. When answering questions:
   - Refer to existing documentation when appropriate
   - Explain GitOps and Argo CD concepts as needed
   - Provide concrete examples based on the repository structure
