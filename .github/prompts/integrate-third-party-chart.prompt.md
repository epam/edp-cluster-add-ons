---
mode: 'agent'
description: 'Integrate an existing third-party Helm chart as a new add-on'
---

# Integrate Third-Party Helm Chart

I'll help you create a wrapper chart for an existing third-party Helm chart.

## Required Information

1. **Chart name**: Name of the third-party chart
2. **Repository URL**: Helm chart repository URL
3. **Chart version**: Specific version to use
4. **Target namespace**: Deployment namespace
5. **Custom values**: Any environment-specific configuration needed

## Integration Pattern

For a chart like `prometheus-operator`, I'll create:

```yaml
# values.yaml structure
prometheus-operator:  # Chart name as top-level key
  prometheusOperator:
    resources:
      limits:
        memory: "256Mi"
```

## What I'll Generate

- Wrapper chart with proper dependency configuration
- Chart.yaml with external chart reference
- Values.yaml with chart name as top-level key
- App of Apps template and configuration
- Repository reference in ct.yaml if needed

Please provide the chart details to begin integration.
