# argocd-diff-preview

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.35.1](https://img.shields.io/badge/AppVersion-0.35.1-informational?style=flat-square)

**Homepage:** <https://docs.kuberocketci.io/>

Deploys a standing [vcluster](https://www.vcluster.com/) with a minimal
[Argo CD](https://argo-cd.readthedocs.io/) bootstrapped inside. The
`argocd-diff-preview` step of the KubeRocketCI gitops review pipelines connects
to this environment to render the manifest diff between a merge request and its
target branch, and posts the result as an MR comment.

**Installing this addon is the feature's on-switch.** The pipeline step is
always present and best-effort: when the addon is absent or unhealthy, the step
skips silently and the review pipeline stays green.

## How it works

1. The pipeline step reads the `vc-argocd-diff-preview` kubeconfig secret from this
   addon's namespace and connects to the virtual cluster.
2. Application manifests exported from the platform namespace are applied to
   the embedded Argo CD, with `targetRevision` redirected to the MR head SHA
   (target) and the MR target branch (base).
3. The embedded Argo CD clones the GitOps repository itself over SSH - the
   platform repo-creds secret is projected into the virtual cluster via
   vcluster `sync.fromHost.secrets`, so rotation propagates automatically. The
   syncer's read RBAC is derived from the mapping keys, so adding a mapping
   automatically grants the required access.
4. The rendered manifests of both revisions are diffed and the result is
   posted to the merge request.

## Site-specific configuration

- **Git server host keys**: add them to the embedded Argo CD via
  `configs.ssh.extraHosts` in the bootstrap chart values when the git server is
  not covered by the default `known_hosts` bundle.
- **DNS**: the git server hostname must resolve from cluster workloads. For
  environments where it does not (e.g. the try-kuberocketci testbed's
  `127.0.0.1.nip.io` domain), ship a CoreDNS override via
  `vcluster.experimental.deploy.vcluster.manifests`.
- Keep `vcluster.exportKubeConfig.server` and `controlPlane.proxy.extraSANs`
  aligned with the release name and namespace.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.loft.sh | vcluster | 0.35.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| vcluster.controlPlane.proxy.extraSANs[0] | string | `"argocd-diff-preview.argocd-diff-preview.svc"` |  |
| vcluster.experimental.deploy.vcluster.helm[0].chart.name | string | `"argo-cd"` |  |
| vcluster.experimental.deploy.vcluster.helm[0].chart.repo | string | `"https://argoproj.github.io/argo-helm"` |  |
| vcluster.experimental.deploy.vcluster.helm[0].chart.version | string | `"9.5.17"` |  |
| vcluster.experimental.deploy.vcluster.helm[0].release.name | string | `"argocd"` |  |
| vcluster.experimental.deploy.vcluster.helm[0].release.namespace | string | `"argocd"` |  |
| vcluster.experimental.deploy.vcluster.helm[0].values | string | `"dex:\n  enabled: false\nnotifications:\n  enabled: false\nconfigs:\n  params:\n    server.insecure: true"` |  |
| vcluster.experimental.deploy.vcluster.manifests | string | `""` |  |
| vcluster.exportKubeConfig.server | string | `"https://argocd-diff-preview.argocd-diff-preview.svc:443"` |  |
| vcluster.rbac.clusterRole.enabled | bool | `false` |  |
| vcluster.sync.fromHost.csiDrivers.enabled | bool | `false` |  |
| vcluster.sync.fromHost.csiNodes.enabled | bool | `false` |  |
| vcluster.sync.fromHost.csiStorageCapacities.enabled | bool | `false` |  |
| vcluster.sync.fromHost.secrets.enabled | bool | `true` |  |
| vcluster.sync.fromHost.secrets.mappings.byName.argocd/gitlab-creds | string | `"argocd/gitlab-creds"` |  |
| vcluster.sync.fromHost.storageClasses.enabled | bool | `false` |  |
