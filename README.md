# EPAM Delivery Platform (EDP) Cluster Add-ons Repository

This repository contains a collection of pre-configured solutions (add-ons) for Kubernetes cluster. It follows the GitOps methodology and utilizes the ArgoCD App of Apps pattern for streamlined configuration and deployment.

The repository offers a variety of Kubernetes add-ons that can be easily integrated into Kubernetes cluster, whether running on Openshift or any other Managed Kubernetes distribution. These add-ons enhance cluster capabilities and provide additional functionalities for the EPAM Delivery Platform (EDP).

Using ArgoCD, one can leverage the repository to expedite the setup process of the EPAM Delivery Platform (EDP) and cluster components. The repository provides ready-to-use configurations for add-ons, simplifying deployment and reducing complexity.

Explore this repository to access a comprehensive collection of Kubernetes add-ons for your Kubernetes. Simplify deployment, enhance cluster capabilities, and stay up-to-date with the evolving landscape of Kubernetes.

## Repository structure

* `add-ons` - contains the source code of the Add Ons in the form of the Helm charts
* `chart` - contains the Helm chart that uses Apps of Apps pattern and contains ArgoCD Application CRs

```bash
.
├── add-ons
│   ├── argocd
│   ├── aws-efs-csi-driver
│   ├── cert-manager
...
│   ├── tekton
│   └── vault
└── chart
    ├── Chart.yaml
    ├── README.md
    ├── templates
    │   ├── argocd.yaml
    │   ├── aws-efs-csi-driver.yaml
    │   ├── cert-manager.yaml
...
    │   ├── tekton.yaml
    │   └── vault.yaml
    └── values.yaml
    └── values.yaml
```

## Available add-ons

Check out the list of available add-ons in the [chart](./chart/README.md) directory.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| argocd.enable | bool | `false` |  |
| awsEfsCsiDriver.enable | bool | `true` |  |
| certmanager.enable | bool | `true` |  |
| defectdojo.enable | bool | `true` |  |
| dependencyTrack.enable | bool | `true` |  |
| edp.enable | bool | `false` |  |
| extensionsOIDC.enable | bool | `true` |  |
| externalSecrets.enable | bool | `true` |  |
| fluentbit.enable | bool | `false` |  |
| harbor.enable | bool | `true` |  |
| ingressNginx.enable | bool | `true` |  |
| jaegerOperator.enable | bool | `true` |  |
| keycloak.enable | bool | `true` |  |
| keycloakPostgresql.enable | bool | `false` |  |
| minioOperator.enable | bool | `true` |  |
| opensearch.enable | bool | `true` |  |
| opentelemetryOperator.enable | bool | `true` |  |
| postgresOperator.enable | bool | `true` |  |
| prometheusOperator.enable | bool | `true` |  |
| redisOperator.enable | bool | `true` |  |
| storageClass.enable | bool | `true` |  |
| tekton.enable | bool | `true` |  |
| vault.enable | bool | `true` |  |
