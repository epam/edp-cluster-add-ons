# argocd-diff-preview

![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.35.1](https://img.shields.io/badge/AppVersion-0.35.1-informational?style=flat-square)

**Homepage:** <https://docs.kuberocketci.io/>

Deploys a standing [vcluster](https://www.vcluster.com/) with a minimal
[Argo CD](https://argo-cd.readthedocs.io/) bootstrapped inside. The
`argocd-diff-preview` step of the KubeRocketCI gitops review pipelines connects
to this environment to render the manifest diff between a merge request and its
target branch, and posts the result as an MR comment.

> **Alpha.** GitLab only, and not yet surfaced in the umbrella `edp-install`
> chart. Enable it deliberately, per cluster.

The pipeline step is always present and best-effort: when the addon is absent
or unhealthy, the step skips silently and the review pipeline stays green.

## Enabling the feature

Two flags, both default `false` - the addon alone is not enough:

| Where | Flag |
|-------|------|
| this repo, `clusters/core/apps/values.yaml` | `argocd-diff-preview.enable` |
| edp-tekton values | `pipelines.argocdDiffPreview.enabled` |

The edp-tekton chart owns the `argocd-diff-preview` namespace (it also grants
the `tekton` ServiceAccount read access to the exported kubeconfig), which is
why the App-of-Apps entry sets `createNamespace: false`.

## How it works

1. The pipeline step reads the `vc-argocd-diff-preview` kubeconfig secret from this
   addon's namespace and connects to the virtual cluster.
2. Application manifests exported from the platform namespace are applied to
   the embedded Argo CD, with `targetRevision` redirected to the MR head SHA
   (target) and the MR target branch (base).
3. The embedded Argo CD clones the repositories itself over SSH, using this
   addon's own read-only credential projected into the virtual cluster via
   vcluster `sync.fromHost.secrets`. Nothing is copied at pipeline runtime and
   rotation propagates automatically.
4. The rendered manifests of both revisions are diffed and the result is
   posted to the merge request.

## Repository credential

The addon carries its own credential rather than reusing the platform's Argo CD
one, so the preview environment stays independent of platform credential
changes. Provision it once:

1. Create an account for the preview (e.g. `krci-preview`) on the git server.
2. Grant it read access to the group holding the GitOps and codebase
   repositories. On GitLab that is the **Reporter** role, which covers every
   current and future project in the group - no per-project setup, and no
   deploy keys to re-enable as codebases are added.
3. Generate an SSH keypair and register the public key on the account.
4. Store the private key and the URL prefix under `eso.secretPath`:

   | Property | Value |
   |----------|-------|
   | `argocd-preview-vcs.sshPrivateKey` | base64-encoded private key |
   | `argocd-preview-vcs.url` | `ssh://<gitUser>@<gitHost>:<sshPort>/` from the `GitServer` spec |

Without External Secrets, create the secret by hand in this addon's namespace
with the same name and keys plus the
`argocd.argoproj.io/secret-type: repo-creds` label.

**It must be a `repo-creds` prefix credential, not a per-repository
`repository` secret.** The preview clones both the GitOps repository (the
`$values` source) and each codebase repository (the `deploy-templates` chart
source); a per-repository secret renders an empty diff.

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

- **Extra credentials**: materialize them into this addon's namespace and add a
  `sync.fromHost.secrets` mapping for each. Mapping a namespace the addon does
  not own grants the syncer read on every secret in it, since `list`/`watch`
  cannot be restricted by `resourceName`.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.loft.sh | vcluster | 0.35.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `false` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/argocd-diff-preview"` | Defines the path to the secret in the provider. If provider is `vault`, this path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"argocd","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"argocd"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
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
| vcluster.sync.fromHost.secrets.mappings.byName.argocd-diff-preview/argocd-preview-vcs | string | `"argocd/argocd-preview-vcs"` |  |
| vcluster.sync.fromHost.storageClasses.enabled | bool | `false` |  |
