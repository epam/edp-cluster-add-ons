# DevOps Helm & Kubernetes Standards

## General Principles

- Always follow Kubernetes and Helm best practices for reliability and maintainability
- Keep configuration declarative and version-controlled according to GitOps principles
- Separate concerns: add-on configuration should be distinct from deployment configuration
- Validate all chart changes through proper testing before deployment

---

## Kubernetes Best Practices

- **Use stable API versions** in manifests; avoid deprecated resources
- **Validate resource compatibility** with your cluster version
- **Set resource limits and requests** for all workloads
- **Apply RBAC and security best practices**: Use least privilege, audit roles regularly
- **Use namespaces for isolation**: Each add-on should have its own dedicated namespace
- **Use labels and annotations** for better resource organization and discovery
- **Follow secret management best practices**: Avoid hardcoding sensitive information

---

## Helm Chart Structure & Standards

- **Wrapper Chart Pattern**: For existing Helm charts, create wrapper charts with the external chart as a dependency
- **Configuration Structure**: Use the dependency chart name as a top-level key in values.yaml
- **Values Placement**: Keep all custom logic and configuration in the add-on's values.yaml, not in App of Apps values
- **Directory Structure**: 
  - All add-on charts are stored in `clusters/{cluster-name}/addons/{addon}/`
  - Each add-on has its own `Chart.yaml`, `values.yaml`, and optional `templates/`
  - App of Apps templates are stored in `clusters/{cluster-name}/apps/templates/`
- **Chart Documentation**: Update README.md and Chart.yaml with every version change
- **Version Control**: Follow semantic versioning for charts and increment versions with changes
- **Dependencies**: Clearly define dependencies in Chart.yaml using proper versioning

---

## App of Apps Pattern Best Practices

- **Minimal App of Apps Configuration**: App of Apps values.yaml should ONLY contain:
  - Enable/disable flags for each add-on
  - Namespace settings
  - CreateNamespace option
- **Application Templates**: Use conditional templates to enable/disable add-ons
- **Cluster Isolation**: Use separate cluster directories to isolate configuration between environments

---

## Maintaining and Updating Charts

- **Review Upstream Changes**: Always check the CHANGELOG of dependency charts before updating
- **Chart Testing**: Validate charts using `helm lint` and chart-testing tools
- **Version Increment**: Always increment chart version when making changes
- **Diff Analysis**: Before applying updates, review diffs for potential breaking changes
- **Rollback Plan**: Always have a rollback strategy ready in case of deployment issues

---

## Chart Testing

- **Lint Charts**: Use `make lint-chart CHART=<chart-name>` for basic validation
- **Full Testing**: Run `make test-charts-full` for comprehensive testing including installation
- **Version Check**: Ensure version increments with `check-version-increment: true` in ct.yaml
- **Test in Isolation**: Test charts individually before integration with other add-ons
