# Task: Initialize New Cluster Directory

## Description

Automate and validate the process of initializing a new cluster directory in the cluster-add-ons repository. This task guides the DevOps agent through the creation of the directory structure, initial configuration files, and integration of add-ons, following repository conventions and best practices.

### Reference Assets

**Primary Dependencies**:

- Add new add-on guide: [add-new-addon.md](./../../docs/add-new-addon.md)
- Add new cluster guide: [add-new-cluster.md](./../../docs/add-new-cluster.md)
- edp-cluster-add-ons repository structure: [edp-cluster-add-ons-structure.md](./.krci-ai/data/edp-cluster-add-ons-structure.md)
- DevOps Helm and Kubernetes standards: [devops-helm-k8s-standarts.md](./.krci-ai/data/devops-helm-k8s-standards.md)

Validation: Verify the dependencies exist at the specified paths before proceeding. HALT if any are missing.

**IMPORTANT**: Do not change the path of the dependencies.

## Overview

Your task is to initialize a new cluster directory in the repository, following the step-by-step guide and best practices described in the reference assets. The process includes creating the directory structure, initial Argo CD application, add-ons directory, App of Apps Helm chart, and updating documentation.

## Instructions

1. **Analyze the repository structure**: Refer to the [EDP Cluster Add-ons Repository Instructions](../../.krci-ai/data/edp-cluster-add-ons-structure.md) to understand the expected directory layout and naming conventions.
2. **Analyze the documentation**: Review the [add-new-cluster.md](../../docs/add-new-cluster.md) and [add-new-addon.md](../../docs/add-new-addon.md) files for precise instructions on how to create a new cluster directory and add new add-ons.
3. **Follow the step-by-step implementation guide**: Use the [add-new-cluster.md](../../docs/add-new-cluster.md) as a roadmap for creating the new cluster directory, ensuring all required files and directories are created and configured correctly.

## Implementation Steps

### STEP-BY-STEP Implementation

1. **CRITICAL FIRST STEP**: Ask the user to provide the following information:

    - Cluster name (e.g., `dev`, `shared`) (REQUIRED)
    - Any specific add-ons to include initially (REQUIRED)

2. Create the new cluster directory in the `clusters/` directory, following the naming conventions.

3. Create the `bootstrap-addons.yaml` file in the new `clusters/{{cluster-name}}` directory, defining the initial Argo CD application for bootstrapping add-ons. Use the following template:

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: addons-{{cluster-name}}
      namespace: argocd
    spec:
      destination:
        server: https://kubernetes.default.svc
      project: {{cluster-name}}
      source:
        path: clusters/{{cluster-name}}/apps
        repoURL: ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons.git
        targetRevision: HEAD
    ```

4. Create the `addons/` and `apps/` directories inside the `clusters/{{cluster-name}}` directory.

5. Scaffold a new App of Apps Helm chart in the `clusters/{{cluster-name}}/apps/` directory using the Helm CLI:

    - Create the `values.yaml` file in the `clusters/{{cluster-name}}/apps/` directory with minimal configuration, using the following template:

        ```yaml
        argoProject: {{cluster-name}}

        clusterName: {{cluster-name}}

        destinationServer: "in-cluster"

        repoUrl: "ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons"

        targetRevision: "main"

        {{add-on-name}}:
          createNamespace: true
          enable: true
          namespace: {{add-on-name}}
        ```

        **IMPORTANT**: The structure of `values.yaml` file must follow exact naming conventions and hierarchy as described above.

    - Create the `Chart.yaml` file in the `clusters/{{cluster-name}}/apps/` directory with the following template:

        ```yaml
        apiVersion: v2
        description: EDP Cluster Addons that extend the Kubernetes Cluster Functionality
        home: https://epam.github.io/edp-install/
        name: edp-cluster-add-ons
        type: application
        version: 0.1.0
        appVersion: 0.1.0
        icon: https://epam.github.io/edp-install/assets/logo.png
        keywords:
          - krci
          - epam
          - addons
          - blueprint
          - pipelines
          - jira
          - ci
          - cd
          - docker
          - image
          - promote
          - git
          - gerrit
          - github
          - gitlab
        maintainers:
          - name: epmd-edp
            email: SupportEPMD-EDP@epam.com
            url: https://solutionshub.epam.com/solution/epam-delivery-platform
          - name: sergk
            url: https://github.com/SergK
        sources:
          - https://github.com/epam/edp-cluster-add-ons
        annotations:
          artifacthub.io/license: Apache-2.0
          artifacthub.io/links: |
            - name: EDP Documentation
              url: https://epam.github.io/edp-install/
            - name: EPAM SolutionHub
              url: https://solutionshub.epam.com/solution/epam-delivery-platform
        ```

        **IMPORTANT**: The `Chart.yaml` file must follow the exact structure and metadata as described above.

    - Create the empty `README.md` file in the `clusters/{{cluster-name}}/apps/` directory.

    - Create the `templates/` directory inside the `clusters/{{cluster-name}}/apps/` directory.

    - Create the Application template file for each add-on in the `clusters/{{cluster-name}}/apps/templates/` directory, using the following template:

        ```yaml
        {{- if and (index .Values "{{add-on-name}}") (index .Values "{{add-on-name}}" "enable") -}}
        apiVersion: argoproj.io/v1alpha1
        kind: Application
        metadata:
          name: {{ .Values.destinationServer}}-{{add-on-name}}
          namespace: {{ .Values.argoNamespace | default "argocd" }}
        spec:
          project: {{ .Values.argoProject | default "default" }}
          source:
            repoURL: {{ .Values.repoUrl }}
            path: clusters/{{ .Values.clusterName }}/addons/{{add-on-name}}
            targetRevision: {{ .Values.targetRevision }}
            helm:
              releaseName: {{add-on-name}}
          destination:
            name: {{ .Values.destinationServer | default "in-cluster" }}
            namespace: {{ index .Values "{{add-on-name}}" "namespace" }}
          syncPolicy:
            syncOptions:
              - CreateNamespace={{ (index .Values "{{add-on-name}}" "createNamespace") }}
            retry:
              limit: 1
              backoff:
                duration: 5s
                factor: 2
                maxDuration: 1m
        {{- end -}}
        ```

        **IMPORTANT**: Each Application template file must follow the exact structure and naming conventions as described above.

6. Create the add-on directory in the `clusters/{{cluster-name}}/addons/` directory for each specified add-on (if any), following the naming conventions.

    - The add-on directory must contain at least the following files:

        - `values.yaml`
        - `Chart.yaml`
        - `README.md`

7. After creating and initializing the new cluster directory, remind the user to:

    - Verify the structure and contents of the new cluster directory against the reference assets.
    - Commit and push the changes to the repository.
    - Sync the new cluster with Argo CD to apply the initial configuration.
    - Update the `README.md` files and chart metadata as necessary to reflect the new cluster and its add-ons.

**NOTES**:
    - You can use already existing add-on directories with Helm charts as template for the new cluster, but ensure to adapt them to the new cluster's requirements.
    - **IMPORTANT**: You must refer to the already existing add-on directories to ensure the new cluster directory follows the correct structure and naming conventions.
    - You need to create at least one add-on directory in the `clusters/<cluster-name>/addons/` directory. You can use an existing add-on from another cluster as a template.

## Success Criteria

- [ ] **Cluster directory created**: All required directories and files exist
- [ ] **Initial Argo CD application present**: `bootstrap-addons.yaml` created and configured
- [ ] **App of Apps chart scaffolded**: Helm chart present in `apps/` directory
- [ ] **values.yaml configured**: Minimal configuration for App of Apps chart exists
- [ ] **Documentation updated**: User reminded to update `README.md` and chart metadata

---

**Note:** For full details and examples, refer to `docs/add-new-cluster.md` and `docs/add-new-addon.md` in the repository.
