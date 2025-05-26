---
mode: 'agent'
description: 'Customize configuration for an existing add-on'
---
# Customize Existing Add-on Configuration

I'll help you customize the configuration for an existing add-on in the EDP Cluster Add-ons repository while following all best practices.

First, I need some information about what you want to customize:

1. Which add-on do you want to customize?
2. What specific configuration changes do you need to make?
3. Why are these customizations necessary for your environment?

Based on your answers, I'll help you:

1. Locate the correct values.yaml file to modify
2. Create appropriate custom configuration following repository patterns
3. Ensure your customizations maintain compatibility with updates
4. Test your changes properly

Remember these key principles when customizing add-ons:

- Keep all custom configuration in the add-on's own values.yaml, not the App of Apps values.yaml
- For add-ons based on external Helm charts, use the chart name as the top-level key in values.yaml
- Preserve default configuration structure to ensure upgrades remain compatible
- Document any significant customizations in comments for future reference

Let's get started with your customization!
