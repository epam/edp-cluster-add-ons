---
mode: 'agent'
description: 'Create a new add-on for the EDP Cluster Add-ons repository'
---
# Create New EDP Cluster Add-on

I'll help you create a new add-on for the EDP Cluster Add-ons repository following all best practices.

First, I need some information about the add-on you want to create:

1. What is the name of the add-on?
2. Is it based on an existing Helm chart? If yes, which one and what version?
3. What namespace should it be deployed in?
4. What is the purpose of this add-on in your cluster?

Based on your answers, I'll help you:

1. Create the appropriate directory structure in `clusters/core/addons/`
2. Create all required files (Chart.yaml, values.yaml, README.md, etc.)
3. Set up proper dependency management if using existing charts
4. Create the App of Apps integration template
5. Update the App of Apps values.yaml with appropriate configuration
6. Provide testing commands to validate your new add-on

I'll follow all best practices from the [add-new-addon.md](../docs/add-new-addon.md) guide and ensure your add-on conforms to all repository standards.

Let's get started!
