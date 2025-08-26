# Quick Start Guide

This guide provides essential steps to get started with using the edp-cluster-add-ons repository, including deploying and configuring Argo CD, setting up cluster directories for add-ons, bootstrapping Argo CD applications, and enabling existing add-ons on your Kubernetes cluster.

<!-- TOC -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [1. Fork the Repository](#1-fork-the-repository)
  - [2. Deploy and Configure Argo CD](#2-deploy-and-configure-argo-cd)
  - [3. Rename Core Cluster Directory (OPTIONAL)](#3-rename-core-cluster-directory-optional)
  - [4. Initialize Bootstrap Add-ons Application](#4-initialize-bootstrap-add-ons-application)
  - [5. Deploy Existing Add-ons](#5-deploy-existing-add-ons)
- [Related Documentation](#related-documentation)

<!-- /TOC -->

## Overview

The edp-cluster-add-ons repository contains a collection of pre-configured Helm charts (add-ons) for Kubernetes clusters. It leverages GitOps principles and employs Argo CD's App of Apps pattern for streamlined deployment and management.

This repository offers various ready-to-use Kubernetes add-ons that can be easily integrated into your cluster with any Managed Kubernetes distribution. With pre-configured components and a consistent structure, it significantly accelerates the deployment process across multiple clusters while maintaining GitOps best practices.

## Prerequisites

Before proceeding, ensure that the following prerequisites are met:

- **Kubernetes Cluster**: You should have access to a Kubernetes cluster where you can deploy Argo CD and other add-ons.
- **Helm**: Helm command-line tool should be installed on your local machine.
- **kubectl**: kubectl command-line tool should be installed and configured to interact with your Kubernetes cluster.
- (OPTIONAL) **External Secrets Operator (ESO)**: Required if using External Secrets Operator for managing Kubernetes secrets.
- (OPTIONAL) **keycloak-operator**: Keycloak Operator is required in case of integration Argo CD with Keycloak for SSO using OIDC.

## Repository Structure

The `edp-cluster-add-ons` repository is organized to facilitate easy management and deployment of add-ons across different clusters. The main components of the repository structure are:

- **argo-cd/**: Contains the main Argo CD Helm chart for deploying Argo CD itself.
- **clusters/**: Contains directories for different clusters (e.g., `core`, `prod`, `sandbox`), each with its own set of add-ons and configurations.
  - Each cluster directory includes:
    - **apps/**: An App of Apps Helm chart that references all add-ons to be deployed on that cluster.
    - **addons/**: A directory containing individual add-on Helm charts.
    - **bootstrap-addons.yaml**: An initial Argo CD application to bootstrap the deployment of add-ons.

The initial structure of the repository looks as follows:

```plaintext
.
├── argo-cd               # Main Argo CD Helm chart
└── clusters
    ├── core              # Core cluster directory
    │   ├── apps          # App of Apps Helm chart that references all add-ons
    │   │   ├── templates
    │   │   │   ├── argo-cd.yaml
    │   │   │   ├── atlantis.yaml
    │   │   │   └── ...
    │   │   ├── Chart.yaml
    │   │   ├── README.md
    │   │   └── values.yaml    # Values that store add-on specific configurations and cluster info
    │   ├── addons             # Directory containing individual add-on Helm charts
    │   │   ├── argo-cd
    │   │   ├── atlantis
    │   │   └── ...
    │   └── bootstrap-addons.yaml  # Initial Argo CD application
    └── prod                       # Production cluster directory
        └── ...
```

## Getting Started

### 1. Fork the Repository

To start using the `edp-cluster-add-ons` repository, it is necessary to fork/copy it to your own GitHub account or organization. This allows you to maintain your own configurations and align structure with your specific requirements.

After forking, clone the repository to your local machine to begin the setup process:

```bash
git clone git@github.com:<account-name>/edp-cluster-add-ons.git
cd edp-cluster-add-ons
```

### 2. Deploy and Configure Argo CD

The `edp-cluster-add-ons` repository is designated for managing and deploying add-ons using Argo CD. To deploy the Argo CD Helm chart, follow the steps below:

1. **Navigate to the Argo CD chart directory**:

    ```bash
    cd argo-cd/
    ```

2. **Configure values.yaml**:

    Configure the `argo-cd/values.yaml` file to match specific requirements of your Kubernetes cluster, including setting for ingress, domain, and other necessary parameters.

3. **Configure AppProject manifests**:

    > **Note**: All Argo CD applications stored in `clusters/core/apps` directory will be automatically assigned to `core` Argo CD AppProject. To change the target AppProject for cluster applications, modify the `argoProject` field in the `clusters/core/apps/values.yaml` file.

    As `edp-cluster-add-ons` repository originally designed to provide additional functionality for KubeRocketCI platform, it is necessary to configure two AppProject manifests, `appProjectCore.yaml` and `appProjectKRCI.yaml`, to define the scope and permissions for Argo CD applications.

    Navigate to the `argo-cd/templates` directory and edit the `appProjectCore.yaml` and `appProjectKRCI.yaml` files by specifying the correct repo source URLs in the `sourceRepos` field for each AppProject. This ensures that Argo CD can access the necessary repositories for deploying applications. For example:

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: AppProject
    metadata:
      name: core
    ...
    spec:
      sourceRepos:
        - ssh://git@github.com:22/<account-name>/*
    ```

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: AppProject
    metadata:
      name: krci 
    ...
    spec:
      sourceRepos:
        - ssh://git@github.com:22/<account-name>/*
    ```

4. Create secrets for VCS integration:

    To enable Argo CD to connect to your version control system (VCS) repositories, it is necessary to create Kubernetes secrets containing the required credentials. There are two methods to create secrets: using `kubectl` command or using External Secrets Operator (ESO).

    **Method 1: Using kubectl**

    Depending on the VCS you are using (GitHub, GitLab, Bitbucket), create a secret with the appropriate configuration. Follow the examples below:

    ```bash
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: argocd-github
      namespace: argocd
      labels:
        argocd.argoproj.io/secret-type: repo-creds
    type: Opaque
    data:
      sshPrivateKey: <base64-encoded-private-key>
      url: "ssh://git@github.com:22/<account-name>"
    EOF
    ```

    **Method 2: Using External Secrets Operator (ESO)**

    > **Note**: The `edp-cluster-add-ons` repository contains only the `argocd-github` external secret manifest in the `argo-cd/templates/external-secrets` directory. If you are using a different VCS, you need to create a corresponding external secret manifest for it.

    Navigate to the `argo-cd/values.yaml` file and enable the ESO integration by setting `eso.enabled` to `true`. Then, configure the ESO parameters according to your requirements.

    Below is an example configuration for ESO using AWS Parameter Store as the secret provider:

    ```yaml
    eso:
      # -- Install components of the ESO.
      enabled: true
      # -- Defines provider type. One of `aws`, `generic`, or `vault`.
      provider: "aws"
      # -- Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`.
      secretPath: "/infra/core/addons/argocd"
      # -- AWS configuration (if provider is `aws`).
      aws:
        # -- AWS region.
        region: "eu-central-1"
        # -- AWS role ARN for the ExternalSecretOperator to assume.
        roleArn: "arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"
    ```

    After configuring the ESO parameters, navigate to the AWS Parameter Store and create the necessary object with the `sshPrivateKey` and `url` fields. The object should be in JSON format, as shown below:

    ```json
    {
    "sshPrivateKey": "<base64-encoded-private-key>",
    "url": "ssh://git@github.com:22/<account-name>",
    "clientSecret": "..."  // Optional parameter, required if OIDC is enabled
    }
    ```

    After deploying the Argo CD Helm chart, the ESO will automatically create a Kubernetes secret named `argocd-github` in the `argocd` namespace, which will be used by Argo CD for VCS integration.

5. (OPTIONAL) **Configure OIDC for SSO**:

    If you want to enable Single Sign-On (SSO) for Argo CD using OpenID Connect (OIDC), it is necessary to configure the OIDC settings in the `argo-cd/values.yaml` file and create a secret for the OIDC client.

    In the `argo-cd/values.yaml` file, locate the `configs.cm."oidc.config"` field and update it with your OIDC provider details. For example, if you are using Keycloak as your OIDC provider, the configuration might look like this:

    ```yaml
    argo-cd:
      configs:
        cm:
          "oidc.config": |
             name: Keycloak
             issuer: https://keycloak.example/auth/realms/shared
             clientID: argocd-tenant
             clientSecret: $keycloak-client-argocd-secret:clientSecret
             requestedScopes:
               - openid
               - profile
               - email
               - groups
    ```

    Navigate to the `argo-cd/templates/oidc` directory and edit the `keycloak-client.yaml` file by specifying the correct `webUrl` field to match your Argo CD ingress URL.

    ```yaml
    apiVersion: v1.edp.epam.com/v1
    kind: KeycloakClient
    metadata:
      name: argocd
    spec:
      ...
      webUrl: https://argocd.example.com
    ```

    After configuring the Keycloak client, enable the OIDC integration in the `argo-cd/values.yaml` file by setting `oidc.enabled` to `true`:

    ```yaml
    argo-cd:
      oidc:
        enabled: true
    ```

    Next, create a Kubernetes secret to store the OIDC client secret. There are two methods to create the secret: using `kubectl` command or using External Secrets Operator (ESO).

    **Method 1: Using kubectl**

    Create the secret using the following command:

    ```bash
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: keycloak-client-argocd-secret
      namespace: argocd
    type: Opaque
    data:
      clientSecret: <base64-encoded-client-secret>  # Random generated string e.g. using `openssl rand -base64 32 | head -c 32` command
    EOF
    ```

    **Method 2: Using External Secrets Operator (ESO)**

    Navigate to the `argo-cd/values.yaml` file and enable the ESO integration by setting `eso.enabled` to `true`. Then, configure the ESO parameters according to your requirements.

    Below is an example configuration for ESO using AWS Parameter Store as the secret provider:

    ```yaml
    eso:
      # -- Install components of the ESO.
      enabled: true
      # -- Defines provider type. One of `aws`, `generic`, or `vault`.
      provider: "aws"
      # -- Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`.
      secretPath: "/infra/core/addons/argocd"
      # -- AWS configuration (if provider is `aws`).
      aws:
        # -- AWS region.
        region: "eu-central-1"
        # -- AWS role ARN for the ExternalSecretOperator to assume.
        roleArn: "arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"
    ```

    After configuring the ESO parameters, navigate to the AWS Parameter Store and create the necessary object with the `clientSecret` field. The object should be in JSON format, as shown below:

    ```json
    {
      "sshPrivateKey": "...",
      "url": "...",
      "clientSecret": "<your-oidc-client-secret>"  // Random generated string e.g. using `openssl rand -base64 32 | head -c 32` command
    }
    ```

    After deploying the Argo CD Helm chart, the ESO will automatically create a Kubernetes secret named `keycloak-client-argocd-secret` in the `argocd` namespace, which will be used by Argo CD for OIDC integration.

6. **Commit and push changes**:

    After making all necessary configurations, commit the changes to remote repository:

    ```bash
    git add .
    git commit -m "<commit-message>"
    git push origin <branch-name>
    ```

7. **Deploy the Argo CD Helm chart**:

    > **Note**: Deployment of the Argo CD Helm chart is managed manually with `helm install` or `helm upgrade --install` commands.

    After configuring the Argo CD Helm chart, deploy it to your Kubernetes cluster using the following command:

    ```bash
    helm install argocd argo-cd/ -n argocd --create-namespace
    ```

    Verify that Argo CD is running correctly by checking the status of the pods in the `argocd` namespace.

### 3. Rename Core Cluster Directory (OPTIONAL)

By default, the `edp-cluster-add-ons` repository contains a `core` cluster directory that contains a full set of pre-configured add-ons with App of Apps Helm chart. In case you want to use another name to identify your cluster inside the repository, you can rename it by following the instructions below:

1. Rename the `core` directory to your desired cluster name.

    ```bash
    mv clusters/core clusters/<your-cluster-name>
    ```

2. Update the `clusterName` field in the `clusters/<your-cluster-name>/apps/values.yaml` file to match the new directory name.

    > **Note**: Do not change the `argoProject` field in the `clusters/<your-cluster-name>/apps/values.yaml` file unless you have also updated the corresponding AppProject manifest in the `argo-cd/templates` directory or created a new one.

    ```yaml
    clusterName: "<your-cluster-name>"
    ```

3. Update the `metadata.name` and `spec.source.path` fields in the `clusters/<your-cluster-name>/bootstrap-addons.yaml` file to match the new directory name.

    > **Note**: Do not change the `spec.project` field in the `clusters/<your-cluster-name>/bootstrap-addons.yaml` file unless you have also updated the corresponding AppProject manifest in the `argo-cd/templates` directory or created a new one.

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: addons-<your-cluster-name>
    spec:
      source:
        path: clusters/<cluster-name>/apps
    ...
    ```

4. Commit and push the changes to your remote repository.

    ```bash
    git add .
    git commit -m "<commit-message>"
    git push origin <branch-name>
    ```

### 4. Initialize Bootstrap Add-ons Application

> **Note**: Before proceeding, ensure that the Argo CD instance is fully operational and accessible.

To bootstrap the deployment of add-ons on your cluster, it is necessary to create an initial Argo CD application that references the App of Apps Helm chart for your cluster. This application will be responsible for deploying all add-ons defined in the App of Apps chart.

To create the bootstrap add-ons application, follow the steps below:

1. Navigate to the `clusters/core/apps` directory and update the `values.yaml` file by specifying the correct `repoUrl` field to point to your forked/copied repository.

    ```yaml
    repoUrl: "ssh://git@github.com:22/<account-name>/edp-cluster-add-ons"
    ```

2. Next, navigate to the `clusters/core` directory.

    ```bash
    cd ../
    ```

3. Align the `spec.source.repoURL` field in the `bootstrap-addons.yaml` file to point to your forked/copied repository.

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: addons-core
      namespace: argocd
    spec:
      source:
        repoURL: ssh://git@github.com:22/<account-name>/edp-cluster-add-ons.git
    ...
    ```

4. Apply the `bootstrap-addons.yaml` manifest to create the Argo CD application.

    ```bash
    kubectl apply -f bootstrap-addons.yaml
    ```

5. Verify that the bootstrap add-ons application is created successfully and is in sync.

### 5. Deploy Existing Add-ons

By default, all add-ons in the `clusters/apps` directory are set to `enabled: false` in the `values.yaml` file, that means they are all disabled. To enable and deploy specific add-on on your cluster, follow the steps below:

1. Choose the add-on you want to enable from the list of available in the `clusters/core/addons` directory and navigate to them.

    ```bash
    cd clusters/core/addons/<addon-name>
    ```

2. Configure the `values.yaml` file to match your specific requirements for the selected add-on.

3. After configuring the add-on values, navigate to the `clusters/core/apps/values.yaml` file.

    ```bash
    cd ../../apps
    ```

4. In the `clusters/core/apps/values.yaml` file, locate the section corresponding to the selected add-on and change the `enabled` field to `true` to enable it for deployment. Change other configuration parameters as needed.

    ```yaml
    <addon-name>:
      createNamespace: true
      enable: true
      namespace: <addon-namespace>
    ```

5. Commit and push the changes to your remote repository.

    ```bash
    git add .
    git commit -m "<commit-message>"
    git push origin <branch-name>
    ```

    After pushing the changes, navigate to the Argo CD and sync the application corresponding to your add-on. Verify that the add-on is deployed successfully and is in sync.

This process can be repeated for any other add-ons you wish to enable and deploy on your cluster.

## Related Documentation

- [Add new Add-on](./add-new-addon.md)
- [Chart Testing](./chart-testing.md)
- [Add new Cluster](./add-new-cluster.md)
