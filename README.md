# EPAM Delivery Platform (EDP) Cluster Add-ons Repository

This repository contains a collection of pre-configured solutions for EPAM Delivery Platform (EDP) Kubernetes Cluster deployments. It follows the GitOps methodology and utilizes the ArgoCD App of Apps pattern for streamlined configuration and deployment.

The repository offers a variety of Kubernetes add-ons that can be easily integrated into Kubernetes Clusters, whether running on Openshift or any other Managed Kubernetes distribution. These add-ons enhance cluster capabilities and provide additional functionalities.

Using ArgoCD, one can leverage the repository to expedite the setup process of an EPAM Delivery Platform (EDP) and cluster components. The repository provides ready-to-use configurations for add-ons, simplifying deployment and reducing complexity.

Explore this repository to access a comprehensive collection of Kubernetes add-ons for your EPAM Delivery Platform (EDP). Simplify deployment, enhance cluster capabilities, and stay up-to-date with the evolving landscape of Kubernetes.

## Repository structure

* `add-ons` - contains the source code of the Add Ons in the form of the Helm charts
* `chart` - contains the Helm chart that uses Apps of Apps pattern and contains ArgoCD Application CRs
