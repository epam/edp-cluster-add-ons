---
mode: 'agent'
description: 'Integrate an existing third-party Helm chart as a new add-on'
---
# Integrate Third-Party Helm Chart as Add-on

I'll help you integrate an existing third-party Helm chart as a new add-on in the EDP Cluster Add-ons repository. This process requires creating a wrapper chart that properly references the external chart as a dependency.

First, I need some information:

1. What is the name of the third-party Helm chart you want to integrate?
2. What is the chart repository URL?
3. Which version of the chart do you want to use?
4. What namespace should this add-on be deployed in?
5. Are there any specific configuration values needed for your environment?

Based on your answers, I'll help you:

1. Create the appropriate directory structure in `clusters/core/addons/`
2. Set up the Chart.yaml with the correct dependency references
3. Create a values.yaml file that properly integrates with the external chart
4. Ensure the top-level key in values.yaml matches the dependency chart name
5. Create an App of Apps template in `clusters/core/apps/templates/`
6. Update the App of Apps values.yaml with minimal configuration
7. Add the chart repository to ct.yaml if needed
8. Create a comprehensive README.md for the add-on

I'll follow the pattern described in [add-new-addon.md](../docs/add-new-addon.md) and ensure your integration follows all repository standards for external chart dependencies.

For example, if you're integrating "prometheus-operator", your values.yaml would look like:

```yaml
# Values for the prometheus-operator wrapper chart

# External chart values with chart name as top-level key
prometheus-operator:
  prometheusOperator:
    resources:
      limits:
        memory: "256Mi"
      requests:
        cpu: "50m"
        memory: "128Mi"
  # Additional configuration...
```

Let's get started with integrating your third-party chart!
