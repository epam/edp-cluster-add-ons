---
dependencies:
  data:
    - devops-helm-k8s-standards.md
    - edp-cluster-add-ons-structure.md
  templates:
    - krci-ai/core-task-template.md
---

# Task: Add New Add-on to Cluster

## Description

Automate and validate the process of adding a new add-on (Helm chart) to an existing cluster directory in the cluster-add-ons repository. This task guides the DevOps agent through the creation of the add-on directory, initial configuration files, and integration into the App of Apps Helm chart, following repository conventions and best practices.

<prerequisites>
- Existing cluster directory in repository
- Access to Helm chart repository for the add-on
- Understanding of Helm chart structure and versioning
- Knowledge of repository standards and patterns
- Required permissions for repository changes
- Familiarity with App of Apps pattern
</prerequisites>

## Reference Assets

**Required Dependencies**:
- Add new add-on guide: [add-new-addon.md](./../../docs/add-new-addon.md)
- Add new cluster guide: [add-new-cluster.md](./../../docs/add-new-cluster.md)
- Repository structure: [edp-cluster-add-ons-structure.md](./.krci-ai/data/edp-cluster-add-ons-structure.md)
- DevOps standards: [devops-helm-k8s-standards.md](./.krci-ai/data/devops-helm-k8s-standards.md)

Validation: Verify the dependencies exist at the specified paths before proceeding. HALT if any are missing.

**IMPORTANT**: Do not change the path of the dependencies.

<instructions>
1. Gather Required Information
   - Request cluster name (REQUIRED)
   - Request add-on name and Helm chart details (REQUIRED)
   - Request chart version (OPTIONAL, default to latest stable)
   - Validate inputs against repository standards

2. Create Add-on Structure
   - Create directory in clusters/{cluster-name}/addons/{addon-name}
   - Initialize Helm chart structure
   - Set up Chart.yaml with proper metadata
   - Configure initial values.yaml

3. Configure Helm Chart
   - Set up dependencies in Chart.yaml
   - Configure default values following standards
   - Add required labels and annotations
   - Set resource limits and requests

4. Update App of Apps
   - Add new application template
   - Update values.yaml with enable flag
   - Configure namespace settings

5. Documentation
   - Create README.md for the add-on
   - Update version information
   - Document configuration options

6. Validation Steps
   - Verify directory structure
   - Check Helm chart syntax
   - Validate against standards
</instructions>

## Output Format

The task will create the following structure:
```
clusters/{cluster-name}/addons/{addon-name}/
├── Chart.yaml
├── README.md
├── values.yaml
└── templates/
    └── (if custom templates needed)
```

<success_criteria>
- Add-on directory created with proper structure
- Chart.yaml configured with correct metadata and dependencies
- values.yaml contains proper configuration following standards
- App of Apps integration complete with enable flag
- Documentation created and properly formatted
- Directory structure matches repository standards
- Chart passes initial validation checks
</success_criteria>

## Execution Checklist

1. [ ] Required information collected
2. [ ] Directory structure created
3. [ ] Helm chart files configured
4. [ ] App of Apps integration complete
5. [ ] Documentation added
6. [ ] Standards validation passed

**IMPORTANT NOTES**:
- Do not run testing or linting commands - notify user to run them manually
- Follow security best practices for sensitive values
- Ensure proper resource management
- Maintain clear documentation