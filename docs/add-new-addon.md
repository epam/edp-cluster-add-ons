# Adding New Add-ons to the Cluster Add-ons Repository

This document provides detailed instructions for adding new add-ons (Helm charts) to the KRCI cluster add-ons repository.

<!-- TOC -->

- [Adding New Add-ons to the Cluster Add-ons Repository](#adding-new-add-ons-to-the-cluster-add-ons-repository)
  - [Overview](#overview)
  - [Repository Structure](#repository-structure)
  - [Step-by-Step Guide to Adding a New Add-on](#step-by-step-guide-to-adding-a-new-add-on)
    - [Create the Add-on Directory](#create-the-add-on-directory)
    - [Create Helm Chart Files](#create-helm-chart-files)
      - [Chart.yaml Example](#chartyaml-example)
    - [Integrating Existing Helm Charts](#integrating-existing-helm-charts)
      - [values.yaml Examples](#valuesyaml-examples)
        - [For Custom Charts](#for-custom-charts)
        - [For Existing Helm Charts](#for-existing-helm-charts)
    - [Add the Add-on to the App of Apps](#add-the-add-on-to-the-app-of-apps)
    - [Update values.yaml in App of Apps](#update-valuesyaml-in-app-of-apps)
    - [Update README.md](#update-readmemd)
    - [Test Your Add-on](#test-your-add-on)
    - [Add External Helm Repository if needed](#add-external-helm-repository-if-needed)
  - [Best Practices](#best-practices)
  - [Examples](#examples)
    - [Real-world Example: ingress-nginx](#real-world-example-ingress-nginx)
  - [Troubleshooting](#troubleshooting)
  - [Advanced Integration Patterns](#advanced-integration-patterns)
    - [Complex Dependencies](#complex-dependencies)
    - [Custom Resources](#custom-resources)

<!-- /TOC -->

## Overview

The KubeRocketCI cluster add-ons repository follows GitOps principles and uses Argo CD's App of Apps pattern to manage and deploy Kubernetes add-ons. Add-ons are organized as Helm charts within a standardized directory structure.

> **Important Guidelines**
>
> 1. **Configuration Placement**: All custom logic and configuration for an add-on should be placed in the add-on's own values.yaml file. The App of Apps values.yaml should ONLY contain enable flags and namespace settings.
>
> 2. **For Existing Helm Charts**: When integrating existing Helm charts, use them as dependencies in your wrapper chart. In your values.yaml, use the dependency chart's name as a top-level key (see the ingress-nginx example below).

## Repository Structure

Before adding a new add-on, it's important to understand the repository structure:

```plaintext
.
├── argo-cd               # Main Argo CD configuration
└── clusters
    └── core
        ├── apps         # App of Apps Helm chart that references all add-ons
        │   ├── templates
        │   │   ├── argo-cd.yaml
        │   │   ├── atlantis.yaml
        │   │   └── ...
        │   ├── Chart.yaml
        │   ├── README.md
        │   └── values.yaml
        ├── addons       # Directory containing individual add-on Helm charts
        │   ├── argo-cd
        │   ├── atlantis
        │   └── ...
        └── bootstrap-addons.yaml  # Initial Argo CD application
```

## Step-by-Step Guide to Adding a New Add-on

### 1. Create the Add-on Directory

Create a new directory for your add-on in the `clusters/<cluster-name>/addons` directory:

```bash
mkdir -p clusters/<cluster-name>/addons/your-addon-name
```

### 2. Create Helm Chart Files

Add the necessary Helm chart files to your add-on directory. At minimum, you need:

```plaintext
clusters/<cluster-name>/addons/your-addon-name/
├── Chart.yaml           # Chart metadata
├── README.md            # Documentation
├── templates/           # Kubernetes manifests templates
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ...
└── values.yaml          # Default configuration values
```

#### Chart.yaml Example

```yaml
apiVersion: v2
name: your-addon-name
description: A Helm chart for Your Add-on on Kubernetes
type: application
version: 1.0.0
appVersion: "1.0.0"
dependencies:
  - name: your-addon-dependency
    version: x.y.z
    repository: https://chart-repo-url.com/charts
```

If you're using an existing Helm chart as a dependency, make sure to add the repository to the `chart-repos` section in `ct.yaml`.

### Integrating Existing Helm Charts

When adding an existing Helm chart, follow this approach:

1. Create a wrapper chart that includes the external chart as a dependency
2. Your wrapper chart's `Chart.yaml` should clearly define the dependency:

```yaml
apiVersion: v2
name: your-addon-name
description: A wrapper chart for External-Chart on Kubernetes
type: application
version: 1.0.0
appVersion: "1.0.0"
dependencies:
  - name: external-chart
    version: x.y.z
    repository: https://external-chart-repo-url.com/charts
```

In your `values.yaml`, provide configuration using the external chart's name as a top-level key:

```yaml
# Configuration for the external chart
external-chart:
  component1:
    enabled: true
  component2:
    setting: value
```

This ensures that values are correctly passed to the subchart and maintains separation between your wrapper configuration and the external chart configuration.

#### values.yaml Examples

##### For Custom Charts

If you're creating a custom chart, your `values.yaml` might look like this:

```yaml
# Default configuration values
replicaCount: 1

image:
  repository: your-addon-image
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

# Add-on specific configuration
config:
  key1: value1
  key2: value2
```

##### For Existing Helm Charts

If you're integrating an existing Helm chart, your `values.yaml` should include the chart name as a top-level key:

```yaml
# Using ingress-nginx as an example
your-dependency-chart-name:
  controller:
    resources:
      limits:
        memory: "256Mi"
      requests:
        cpu: "50m"
        memory: "128M"
    config:
      ssl-redirect: 'true'
    service:
      type: NodePort
```

This approach ensures that all configuration for the dependency is properly passed to the subchart.

### 3. Add the Add-on to the App of Apps

Create an Argo CD Application template for your add-on in `clusters/<cluster-name>/apps/templates`:

```bash
touch clusters/<cluster-name>/apps/templates/your-addon-name.yaml
```

Add the following content:

```yaml
{{- if and (index .Values "your-addon-name") (index .Values "your-addon-name" "enable") -}}
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: {{ .Values.destinationServer}}-your-addon-name
  namespace: {{ .Values.argoNamespace | default "argocd" }}
spec:
  project: {{ .Values.argoProject | default "default" }}
  source:
    repoURL: {{ .Values.repoUrl }}
    path: clusters/{{ .Values.clusterName }}/addons/your-addon-name
    targetRevision: {{ .Values.targetRevision }}
    helm:
      releaseName: your-addon-name
  destination:
    name: {{ .Values.destinationServer | default "in-cluster" }}
    namespace: {{ index .Values "your-addon-name" "namespace" }}
  syncPolicy:
    syncOptions:
      - CreateNamespace={{ (index .Values "your-addon-name" "createNamespace") }}
    retry:
      limit: 1
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 1m
{{- end -}}
```

Note that we're using `index .Values "your-addon-name"` syntax rather than `.Values.addons.your-addon-name` for addons that has dash in their name.

### 4. Update values.yaml in App of Apps

Add your add-on to the `clusters/<cluster-name>/apps/values.yaml` file with minimal configuration:

```yaml
# ... existing add-ons ...
your-addon-name:
  enable: true  # Set to true to enable
  namespace: your-addon-namespace
  createNamespace: true  # Optional, defaults to true
```

> **Important**: The App of Apps values.yaml should only contain the enable flag and namespace configuration. DO NOT put custom logic or addon-specific values here. All addon-specific configuration should go in the addon's own values.yaml file.

### 5. Update README.md

Update the table in the root `README.md` with information about your add-on. The `make update-readme` command can be used to automate this process.

### 6. Test Your Add-on

Before submitting a pull request, test your add-on locally using the chart-testing tool:

```bash
# Lint your chart
make lint-chart CHART=your-addon-name

# Test full installation in a kind cluster
make test-charts-full
```

See the [Chart Testing](chart-testing.md) documentation for more details on testing.

### 7. Add External Helm Repository (if needed)

If your add-on depends on charts from an external repository, add it to the `chart-repos` section in the `ct.yaml` file:

```yaml
chart-repos:
  - existing-repo=https://existing-repo-url.com
  - your-addon-repo=https://your-addon-repo-url.com
```

## Best Practices

1. **Documentation**: Provide clear documentation in your add-on's README.md file, including:
   - Purpose of the add-on
   - Configuration options
   - Requirements
   - Usage examples

2. **Configuration**: Make your add-on configurable through values.yaml, allowing users to customize the deployment without modifying templates.

3. **Dependencies**: Explicitly declare dependencies in Chart.yaml if your add-on requires other components.

4. **Namespace**: Use a dedicated namespace for your add-on to avoid conflicts with other components.

5. **Resource Requests/Limits**: Define appropriate resource requests and limits for your add-on.

6. **Tests**: Include Helm tests in your chart to verify that the add-on works as expected.

7. **Version**: Follow semantic versioning for your chart and update the version when making changes.

8. **Configuration Separation**: Always keep custom logic and configuration in the add-on's values.yaml, not in the App of Apps values.yaml. This separation offers several benefits:
   - Improved maintainability: Changes to add-on configuration don't require modifying the central App of Apps values
   - Better version control: Each add-on's configuration evolves independently
   - Clearer responsibility boundaries: The App of Apps only controls deployment, not configuration
   - Easier testing: Add-ons can be tested in isolation with their full configuration

## Examples

You can refer to existing add-ons in the repository for examples:

- argo-cd
- atlantis
- cert-manager

Each add-on follows the same structure and pattern, making it easy to understand how to implement your own.

### Real-world Example: ingress-nginx

The ingress-nginx add-on provides an excellent example of how to integrate an existing Helm chart:

**Chart.yaml** defines the dependency:

```yaml
apiVersion: v2
name: ingress-nginx
description: A Helm chart for Nginx Ingress Controller
type: application
version: 4.12.1
appVersion: "1.12.1"
dependencies:
- name: ingress-nginx
  version: 4.12.1
  repository: https://kubernetes.github.io/ingress-nginx
```

**values.yaml** uses the dependency name as a top-level key:

```yaml
ingress-nginx:
  controller:
    allowSnippetAnnotations: true
    podAnnotations:
      fluentbit.io/parser: k8s-nginx-ingress
    addHeaders:
      X-Content-Type-Options: nosniff
    resources:
      limits:
        memory: "256Mi"
      requests:
        cpu: "50m"
        memory: "128M"
    service:
      type: NodePort
```

**App of Apps template** (in `clusters/core/apps/templates/ingress-nginx.yaml`) only needs enable and namespace flags:

```yaml
{{- if and (index .Values "ingress-nginx") (index .Values "ingress-nginx" "enable") -}}
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: {{ .Values.destinationServer}}-ingress-nginx
  namespace: {{ .Values.argoNamespace | default "argocd" }}
spec:
  project: {{ .Values.argoProject | default "default" }}
  source:
    repoURL: {{ .Values.repoUrl }}
    path: clusters/{{ .Values.clusterName }}/addons/ingress-nginx
    targetRevision: {{ .Values.targetRevision }}
    helm:
      releaseName: ingress-nginx
  destination:
    name: {{ .Values.destinationServer | default "in-cluster" }}
    namespace: {{ index .Values "ingress-nginx" "namespace" }}
  syncPolicy:
    syncOptions:
      - CreateNamespace={{ (index .Values "ingress-nginx" "createNamespace") }}
    retry:
      limit: 1
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 1m
{{- end -}}
```

**App of Apps values.yaml** contains only the essential flags:

```yaml
ingress-nginx:
  enable: true
  namespace: ingress-nginx
  createNamespace: true
```

This pattern ensures that:

- Configuration for the ingress-nginx chart is kept in the add-on's values.yaml
- The App of Apps only controls whether the add-on is enabled and where it deploys
- All custom logic and configuration is properly contained in the add-on directory

## Troubleshooting

If you encounter issues with your add-on:

1. Check the Argo CD logs for deployment errors
2. Verify that your Helm chart syntax is correct
3. Review the chart-testing output for linting errors
4. Ensure all dependencies are properly configured and available
5. Confirm that the namespace settings are correct

## Advanced Integration Patterns

### Complex Dependencies

For add-ons with multiple dependencies or complex configuration requirements:

Organize dependencies clearly in Chart.yaml:

```yaml
dependencies:
  - name: primary-chart
    version: 1.2.3
    repository: https://charts.example.com/
    condition: primary-chart.enabled
  - name: secondary-chart
    version: 4.5.6
    repository: https://charts.example.com/
    condition: secondary-chart.enabled
```

Structure your `values.yaml` to maintain clear separation between dependencies:

```yaml
# Global configuration
global:
  storageClass: standard

# Primary chart configuration
primary-chart:
  enabled: true
  replicaCount: 2

# Secondary chart configuration
secondary-chart:
  enabled: false
  replicaCount: 1
```

### Custom Resources

When your add-on needs to create custom resources beyond what the dependency chart provides:

Add additional templates in your wrapper chart's templates directory:

```plaintext
templates/
  ├── additional-resource.yaml
  ├── configmap.yaml
  └── secret.yaml
```

Reference shared values between your templates and the dependency:

```yaml
# In your add-on's values.yaml
my-addon:
  sharedConfig:
    key: value

# Then in your template
apiVersion: v1
kind: ConfigMap
metadata:
  name: additional-config
data:
  key: {{ .Values.my-addon.sharedConfig.key }}
```

This approach allows you to extend existing charts while maintaining a clean separation of concerns.
