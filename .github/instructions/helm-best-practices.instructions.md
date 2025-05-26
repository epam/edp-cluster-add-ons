---
applyTo: "clusters/core/addons/**/*.yaml"
---
# Helm Chart Best Practices

When working with Helm charts in this repository, follow these best practices:

## Chart Structure

1. **Dependency Management**:
   - Use `dependencies` in `Chart.yaml` to reference external charts
   - Run `helm dependency update` before testing
   - Lock versions to ensure reproducible deployments

2. **Template Organization**:
   - Group related resources in the same file
   - Use descriptive filenames that indicate the resource type
   - Prefix filenames with numbers to control creation order if necessary

3. **Values Management**:
   - Provide sensible defaults in `values.yaml`
   - Document all values with comments
   - Use a hierarchical structure for complex configurations
   - Prefix internal values with an underscore (_)

## Template Guidelines

1. **Templating Style**:
   - Use camelCase for variables
   - Use kebab-case for resource names
   - Include whitespace in templates for readability
   - Use indent function to maintain proper YAML structure

2. **Resource Naming**:
   - Use consistent naming patterns
   - Include the release name and chart name in resource names
   - Use templates for common name components

3. **Labels and Annotations**:
   - Always include recommended Kubernetes labels
   - Use Helm's built-in label helpers
   - Group related labels together

4. **Security Considerations**:
   - Never hardcode secrets in templates
   - Use appropriate secret management
   - Set sensible default security contexts
   - Follow principle of least privilege

## Testing

1. **Validation**:
   - Use `helm lint` to validate syntax
   - Use `helm template` to render and inspect output
   - Test installation in a kind cluster before committing

2. **Documentation**:
   - Document all configurable values
   - Include example configurations for common use cases
   - Keep README.md updated with latest features and requirements
