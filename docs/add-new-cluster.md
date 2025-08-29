# Adding New Clusters to the Cluster Add-ons Repository

This document provides detailed instructions for adding new cluster directories to the KubeRocketCI cluster add-ons repository, enabling the management of multiple clusters with dedicated add-ons and configuration.

<!-- TOC -->
- [Adding New Clusters to the Cluster Add-ons Repository](#adding-new-clusters-to-the-cluster-add-ons-repository)
  - [Overview](#overview)
  - [Repository Structure](#repository-structure)
  - [Step-by-Step Guide to Adding a New Cluster Directory](#step-by-step-guide-to-adding-a-new-cluster-directory)
    - [Create the Cluster Directory](#1-create-the-cluster-directory)
    - [Create initial Argo CD Application](#2-create-initial-argo-cd-application)
    - [Create the Add-ons Directory](#3-create-the-add-ons-directory)
    - [Add Add-on Charts](#4-add-add-on-charts)
    - [Create the App of Apps Helm Chart](#5-create-the-app-of-apps-helm-chart)
    - [Configure App of Apps Chart values](#6-configure-app-of-apps-chart-values)
    - [Update Documentation and Chart Metadata](#7-update-documentation-and-chart-metadata)
  - [Best Practices](#best-practices)
  - [Examples](#examples)
    - [Example: Adding a prod cluster](#example-adding-a-prod-cluster-with-the-atlantis-add-on)
<!-- /TOC -->

## Overview

The KubeRocketCI cluster add-ons repository supports managing multiple Kubernetes clusters, each with its own set of add-ons and configuration. This separation allows for:

- **Environment isolation**: Each cluster (e.g., `core`, `prod`, `dev`) can have its own add-ons, configurations, and deployment logic.
- **Scalability**: Easily add new clusters as your infrastructure grows.
- **Customizability**: Tailor add-ons and settings to the needs of each cluster.
- **GitOps best practices**: Maintain declarative, version-controlled infrastructure for all clusters.

> **Reference**: Before adding a new cluster, review [add-new-addon.md](./add-new-addon.md) for principles and patterns used for add-on management.

## Repository Structure

The repository organizes clusters as top-level directories under `clusters/`, each containing its own add-ons and App of Apps configuration. For example, the structure for the multiple clusters might look like this:

```plaintext
.
└── clusters
    ├── core                       # Core cluster directory
    │   ├── apps                   # App of Apps Helm chart that references all add-ons
    │   │   ├── templates
    │   │   │   ├── argo-cd.yaml
    │   │   │   ├── atlantis.yaml
    │   │   │   └── ...
    │   │   ├── Chart.yaml
    │   │   ├── README.md
    │   │   └── values.yaml
    │   ├── addons                 # Directory containing individual add-on Helm charts
    │   │   ├── argo-cd
    │   │   ├── atlantis
    │   │   └── ...
    │   └── bootstrap-addons.yaml  # Initial Argo CD application
    ├── prod                       # Production cluster directory
    │   ├── apps                   # App of Apps Helm chart for 'prod'
    │   │   ├── templates
    │   │   │   ├── argo-cd.yaml
    │   │   │   ├── atlantis.yaml
    │   │   │   └── ...
    │   │   ├── Chart.yaml
    │   │   ├── README.md
    │   │   └── values.yaml
    │   ├── addons                 # Directory containing individual add-on Helm charts
    │   │   ├── argo-cd
    │   │   ├── atlantis
    │   │   └── ...
    │   └── bootstrap-addons.yaml  # Initial Argo CD application for 'prod'
    └── dev                        # Development cluster directory
        └── ...
```

## Step-by-Step Guide to Adding a New Cluster Directory

### 1. Create the Cluster Directory

Create a new directory for the cluster you want to add.

```bash
mkdir -p clusters/<cluster-name>
```

### 2. Create initial Argo CD Application

In the new cluster directory, create a file named `bootstrap-addons.yaml` to define the initial Argo CD application that will manage the add-ons for this cluster:

```bash
touch clusters/<cluster-name>/bootstrap-addons.yaml
```

Add the following content to `bootstrap-addons.yaml`:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: addons-<cluster-name>
  namespace: argocd
spec:
  destination:
    server: https://kubernetes.default.svc
  project: <cluster-name>
  source:
    path: clusters/<cluster-name>/apps
    repoURL: ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons.git
    targetRevision: HEAD
```

Define the following fields:
- `name`: Unique name for the application (e.g., `addons-prod`).
- `namespace`: Namespace where the Argo CD instance is running (e.g., `argocd`).
- `destination`: The Kubernetes cluster and namespace where the application will be deployed.
- `project`: The Argo CD project this application belongs to (e.g., `prod`).
- `source`: The path to the App of Apps Helm chart for this cluster, including the repository URL and target revision.

### 3. Create the Add-ons Directory

Create the directory for add-ons within the cluster directory:

```bash
mkdir -p clusters/<cluster-name>/addons
```

This directory will contain the Helm charts for each add-on specific to this cluster.

### 4. Add Add-on Charts

Add the required Helm chart for each add-on you want to manage in this cluster.

Each add-on should follow the standard structure:

```plaintext
.
└── clusters
    └── prod
        └── addons
            └── atlantis
                ├── Chart.yaml    # Chart metadata
                ├── README.md     # Text documentation for the add-on
                ├── README.md.gotmpl (optional)
                ├── values.yaml   # Default values for the add-on
                └── templates/    # Kubernetes manifests for the add-on (Optional)
                    └── ...
```

### 5. Create the App of Apps Helm Chart

Create the App of Apps Helm chart that will manage the add-ons for this cluster. This chart will reference all the add-ons defined in the `addons` directory.

> **Important Guideline**:
> The directory must be named `apps` to follow the naming convention used in the repository.

```bash
helm create clusters/<cluster-name>/apps
```

This command creates a basic Helm chart structure in `clusters/<cluster-name>/apps/`. The target structure should look like this:

```plaintext
.
└── clusters
    └── prod
        └── apps
            ├── templates/       # Contains Argo CD Application templates for each add-on
            │   ├── argo-cd.yaml
            │   ├── atlantis.yaml
            │   └── ...
            ├── Chart.yaml       # Chart metadata for the App of Apps
            ├── README.md        # Documentation for the App of Apps
            └── values.yaml      # Default values for the App of Apps
```

In `templates/`, add an Argo CD Application template for each add-on. Example of creating an Argo CD Application for the `atlantis` add-on is provided below:

```yaml
{{- if and (index .Values "atlantis") (index .Values "atlantis" "enable") -}}
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: {{ .Values.destinationServer}}-atlantis
  namespace: {{ .Values.argoNamespace | default "argocd" }}
spec:
  project: {{ .Values.argoProject | default "default" }}
  source:
    repoURL: {{ .Values.repoUrl }}
    path: clusters/{{ .Values.clusterName }}/addons/atlantis
    targetRevision: {{ .Values.targetRevision }}
    helm:
      releaseName: atlantis
  destination:
    name: {{ .Values.destinationServer | default "in-cluster" }}
    namespace: {{ index .Values "atlantis" "namespace" }}
  syncPolicy:
    syncOptions:
      - CreateNamespace={{ (index .Values "atlantis" "createNamespace") }}
    retry:
      limit: 1
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 1m
{{- end -}}
```

### 6. Configure App of Apps Chart values

In the `clusters/prod/apps/values.yaml` file, it is necessary to define the values that will be used by the App of Apps chart. This includes the Argo CD project, cluster name, destination server, repository URL, target revision, and any add-on-specific configurations.

```yaml
# The Argo CD project to which this application belongs.
argoProject: core

# Specifies the name of the cluster. This value is used to dynamically set the path for Argo CD Application manifests.
clusterName: core

# Specifies the destination server where the code will be deployed.
# In this case, "in-cluster" indicates that the deployment will happen within the Kubernetes cluster itself.
destinationServer: "in-cluster"

# Specifies the URL of the Git repository from which the code will be pulled for deployment.
# It is provided in the SSH format, indicating the username (`ci`), hostname (`git.example.com`),
# and port (`22`) of the Git server, along with the repository path (`cluster-add-ons`).
repoUrl: "ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons"

# Specifies the target revision or branch of the Git repository that will be deployed.
# In this case, "main" indicates that the main branch of the repository will be used for deployment.
targetRevision: "main"

# Add-on configurations
argo-cd:
  createNamespace: false
  enable: true
  namespace: argocd

atlantis:
  createNamespace: false
  enable: true
  namespace: atlantis

# Add more add-ons as needed
```

This `values.yaml` file serves as the central configuration for the App of Apps chart, allowing you to enable or disable specific add-ons and set their configuration options.

### 7. Update Documentation and Chart Metadata

Update the `README.md` and `Chart.yaml` files in the `clusters/<cluster-name>/apps/` directory to document the purpose of the App of Apps chart, its values, and how to use it.

```bash
helm-docs -c clusters/<cluster-name>/apps
```

## Best Practices

1. **Cluster Isolation**: Always use a dedicated directory for each cluster under `clusters/`. This ensures clear separation of configuration and add-ons, reducing the risk of cross-cluster conflicts.
2. **Consistent Structure**: Maintain the same directory and chart structure for all clusters. This simplifies onboarding, automation, and troubleshooting.
3. **Minimal App of Apps values.yaml**: Only include enable flags and namespace settings for add-ons in the App of Apps chart values. All custom logic and configuration for each add-on must be placed in the add-on's own values.yaml file.
4. **Documentation**: Document the purpose, configuration, and usage of each cluster and add-on. Update the relevant README.md files whenever changes are made.
5. **Testing**: Use chart-testing tools to lint and test cluster-specific add-ons before deployment. Validate changes in a test environment when possible.
6. **Version Control**: Track all changes to cluster configuration and add-ons in Git. Use meaningful commit messages and pull requests for auditability and rollback.
7. **Naming Conventions**: Follow the established naming conventions for directories and files (e.g., `apps`, `addons`, `bootstrap-addons.yaml`) to ensure compatibility with automation and documentation tools.
8. **Security and Access**: Restrict access to cluster-specific directories and sensitive configuration files as appropriate. Use namespaces to isolate resources within clusters.

## Examples

### Example: Adding a `prod` Cluster with the `atlantis` Add-on

1. Create the `prod` cluster directory:

    ```bash
    mkdir -p clusters/prod
    ```

2. Create the initial Argo CD application for the `prod` cluster in `clusters/prod` directory:

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: addons-prod
      namespace: argocd
    spec:
      destination:
        server: https://kubernetes.default.svc
      project: prod
      source:
        path: clusters/prod/apps
        repoURL: ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons.git
        targetRevision: HEAD
    ```

3. Create the add-ons directory for the `prod` cluster:

    ```bash
    mkdir -p clusters/prod/addons
    ```

    Place the Helm charts for the `atlantis` add-on in `clusters/prod/addons/atlantis`.

    ```plaintext
    .
    └── clusters
        └── prod
            └── addons
                └── atlantis
                    ├── Chart.yaml
                    ├── README.md
                    ├── README.md.gotmpl (optional)
                    ├── values.yaml
                    └── templates/
    ```

4. Create the App of Apps Helm chart for the `prod` cluster:

    ```bash
    helm create clusters/prod/apps
    ```

5. Add the Argo CD Application template for the `atlantis` add-on in `clusters/prod/apps/templates/atlantis.yaml`:

    ```yaml
    {{- if and (index .Values "atlantis") (index .Values "atlantis" "enable") -}}
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: {{ .Values.destinationServer}}-atlantis
      namespace: {{ .Values.argoNamespace | default "argocd" }}
    spec:
      project: {{ .Values.argoProject | default "default" }}
      source:
        repoURL: {{ .Values.repoUrl }}
        path: clusters/{{ .Values.clusterName }}/addons/atlantis
        targetRevision: {{ .Values.targetRevision }}
        helm:
          releaseName: atlantis
      destination:
        name: {{ .Values.destinationServer | default "in-cluster" }}
        namespace: {{ index .Values "atlantis" "namespace" }}
      syncPolicy:
        syncOptions:
          - CreateNamespace={{ (index .Values "atlantis" "createNamespace") }}
        retry:
          limit: 1
          backoff:
            duration: 5s
            factor: 2
            maxDuration: 1m
    {{- end -}}
    ```

6. Configure the App of Apps chart values in `clusters/prod/apps/values.yaml`. Specify the `atlantis` add-on values, enable it, and set the namespace. Also, set the Argo CD project, cluster name, destination server, repository URL, and target revision parameters:

    ```yaml
    argoProject: prod

    clusterName: prod

    destinationServer: "in-cluster"

    repoUrl: "ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons"

    targetRevision: "main"

    atlantis:
      createNamespace: false
      enable: true
      namespace: atlantis
    ```

7. Update the `README.md` and `Chart.yaml` files in the `clusters/prod/apps/` directory to document the purpose of the App of Apps chart, its values, and how to use it.

    ```bash
    helm-docs -c clusters/prod/apps
    ```

This process enables you to manage the `prod` cluster with the `atlantis` add-on, following GitOps and best practices for scalable, maintainable infrastructure.
