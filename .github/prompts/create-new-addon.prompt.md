---
mode: 'agent'
description: 'Create a new add-on for the EDP Cluster Add-ons repository'
---

# Create New EDP Cluster Add-on

I'll help you create a new add-on following the repository's GitOps patterns and Helm best practices.

## Required Information

1. **Add-on name**: What should this add-on be called?
2. **Chart type**: New chart or wrapper for existing third-party chart?
3. **Target namespace**: Where should it be deployed?
4. **Purpose**: Brief description of what this add-on does

## What I'll Create

- Directory structure in `clusters/core/addons/{addon-name}/`
- Required files: `Chart.yaml`, `values.yaml`, `README.md`
- App of Apps integration in `clusters/core/apps/templates/`
- Minimal configuration in App of Apps `values.yaml`

## Standards I'll Follow

- Self-contained add-on structure
- Dependency chart name as top-level key in values.yaml
- Proper Helm chart versioning
- GitOps declarative configuration

Ready to start? Please provide the required information above.
