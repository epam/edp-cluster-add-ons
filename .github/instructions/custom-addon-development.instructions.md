---
applyTo: "clusters/core/addons/**/templates/**"
---
# Custom Add-on Development Guidelines

When creating a custom add-on (not based on an existing Helm chart), follow these guidelines:

## Chart Structure

1. **Directory Organization**:
   - `templates/` - Contains all Kubernetes resource templates
   - `values.yaml` - Default configuration values
   - `Chart.yaml` - Chart metadata
   - `README.md` - Documentation

2. **Template Design**:
   - Create separate files for each Kubernetes resource type
   - Use a logical naming convention (e.g., `deployment.yaml`, `service.yaml`)
   - Group related resources in the same file when appropriate
   - Consider creation order (use numeric prefixes if necessary)

## Resource Templates

1. **Common Patterns**:
   - Use Helm's built-in objects and functions consistently
   - Create helper templates for repeated elements
   - Include appropriate labels and annotations
   - Set resource requests and limits for all containers

2. **Kubernetes Best Practices**:
   - Use appropriate API versions
   - Apply security contexts
   - Set proper resource requests and limits
   - Include readiness and liveness probes
   - Use namespaced resources when possible

3. **Parameterization**:
   - Make all configurable elements customizable via values.yaml
   - Provide sensible defaults for all parameters
   - Use nested structures for complex configurations
   - Document all configurable parameters

## Common Helpers and Functions

1. **Name Templates**:
   ```yaml
   {{- define "your-addon.name" -}}
   {{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
   {{- end }}
   ```

2. **Label Templates**:
   ```yaml
   {{- define "your-addon.labels" -}}
   helm.sh/chart: {{ include "your-addon.chart" . }}
   app.kubernetes.io/name: {{ include "your-addon.name" . }}
   app.kubernetes.io/instance: {{ .Release.Name }}
   app.kubernetes.io/managed-by: {{ .Release.Service }}
   {{- end }}
   ```

3. **Selector Templates**:
   ```yaml
   {{- define "your-addon.selectorLabels" -}}
   app.kubernetes.io/name: {{ include "your-addon.name" . }}
   app.kubernetes.io/instance: {{ .Release.Name }}
   {{- end }}
   ```

## Testing Custom Add-ons

Always thoroughly test custom add-ons:

1. Lint the chart: `helm lint clusters/core/addons/your-addon`
2. Render templates: `helm template clusters/core/addons/your-addon`
3. Test installation: `make test-charts-full`
4. Verify functionality in a test environment

For complex custom add-ons, consider writing Helm tests that can validate the deployment.
