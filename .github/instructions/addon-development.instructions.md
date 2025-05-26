---
applyTo: "clusters/core/addons/**/*"
---
# Add-on Development Guidelines

## Structure and Standards

When working with add-ons in this repository, follow these guidelines:

1. **Directory Structure**: Each add-on should be in its own directory under `clusters/core/addons/`.
   - Required files: `Chart.yaml`, `values.yaml`, `README.md`
   - Templates directory with Kubernetes manifests as needed

2. **Dependency Management**:
   - For existing Helm charts, use them as dependencies in your wrapper chart
   - In `values.yaml`, use the dependency chart name as a top-level key
   - Example:
     ```yaml
     ingress-nginx:  # Dependency chart name as top-level key
       controller:
         resources:
           limits:
             memory: "256Mi"
     ```

3. **Configuration Separation**:
   - All custom logic and configuration should be in the add-on's own `values.yaml`
   - The App of Apps `values.yaml` should ONLY contain enable flags and namespace settings
   - Example for App of Apps:
     ```yaml
     your-addon-name:
       enable: true
       namespace: your-addon-namespace
     ```

4. **Naming Conventions**:
   - Use kebab-case for directory and chart names
   - Use descriptive names that clearly identify the add-on's purpose

5. **Documentation**:
   - Include a comprehensive README.md for each add-on
   - Document all configurable parameters in your values.yaml
   - Reference external documentation when appropriate

## Testing Requirements

Before committing a new add-on:
- Lint the chart with `make lint-chart CHART=your-addon-name`
- Test installation with `make test-charts-full`
- Verify the add-on functions as expected in a test environment

## Integration with App of Apps

Remember to:
1. Create an Argo CD Application template in `clusters/core/apps/templates/`
2. Update `clusters/core/apps/values.yaml` with minimal configuration
3. Update the main README.md table (use `make update-readme`)

For any complex patterns or unique requirements, refer to the documentation in `/docs/`.
