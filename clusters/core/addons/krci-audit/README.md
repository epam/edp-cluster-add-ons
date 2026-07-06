# krci-audit

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

A Helm chart for the KubeRocketCI krci-audit add-on — admission audit capture, store, and read API

**Homepage:** <https://docs.kuberocketci.io/>

This add-on is a thin wrapper: it installs the `krci-audit` component chart and only overrides
`db.mode`. Capture, storage, the read API, and scheduled partition retention are all configured
in the component chart's own `values.yaml`.

## Database credentials

The component chart **never generates DB credentials** — it only reads a Secret you supply, in
every `db.mode` (including the default `simple`, which provisions the in-cluster Postgres but not
its Secret). Before enabling this add-on, provide the `krci-audit-db-access` Secret one of two ways:

- **External Secrets Operator** (recommended for GitOps): enable the `eso` block in `values.yaml`, or
- **Pre-create the Secret** once:

  ```bash
  kubectl -n krci-audit create secret generic krci-audit-db-access \
    --from-literal=db-owner-username=krci-audit \
    --from-literal=db-owner-password="$(openssl rand -base64 24)" \
    --from-literal=writer-password="$(openssl rand -base64 24)" \
    --from-literal=reader-password="$(openssl rand -base64 24)"
  ```

  `db-owner-*` is required for `simple` mode (it initializes the in-cluster Postgres);
  `writer-password` always; `reader-password` only when the read API is enabled. For
  `external`/`pgo`, point `db.owner.secretName` at your DB / operator Secret and keep only the
  writer/reader keys here.

## Retention

Scheduled cleanup is on by default (keep 12 months, nightly). The component-chart defaults are
shown commented in `values.yaml` — uncomment the `retention` block to override. Note it is
**month-granular**: `months` is a whole number and data is dropped a whole monthly partition at
a time, so the smallest effective window is ~1 month (sub-monthly windows such as 3 weeks are not
supported).

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | krci-audit | 0.1.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| krci-audit.db.mode | string | `"simple"` | Provisioning mode for the component's PostgreSQL (external | pgo | simple). `simple` runs a self-contained in-cluster Postgres (dev/small installs); use `external` (set db.host + db.owner.secretName) or `pgo` for production. Credentials are a prerequisite in every mode (see the header note) — the chart provisions the DB in simple/pgo, never its Secret. |
