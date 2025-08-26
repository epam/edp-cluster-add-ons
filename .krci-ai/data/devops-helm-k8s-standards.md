# DevOps Helm & Kubernetes Standards

## General Principles
- Automate repetitive tasks and validate all changes before applying
- Communicate risks, breaking changes, and required actions clearly
- Always follow Kubernetes and Helm best practices for reliability and maintainability

---

## Kubernetes Best Practices
- **Use stable API versions** in manifests; avoid deprecated resources
- **Validate resource compatibility** with your cluster version
- **Set resource limits and requests** for all workloads
- **Apply RBAC and security best practices**: Use least privilege, audit roles regularly
- **Monitor for breaking changes**: Watch for API removals, spec changes, and new required fields
- **Test in staging** before production rollout

---

## Add-on Chart Structure
- All add-on charts are stored in `clusters/{cluster-name}/addons/{addon}/`
- Each add-on has its own `Chart.yaml`, `values.yaml`, and `templates/`
- Dependency charts are defined in Chart.yaml under `dependencies:`
- Repository links and chart names are extracted from Chart.yaml
- Keep chart documentation up to date with every version bump

---

## Migration & Troubleshooting
- Always review upstream chart CHANGELOG and documentation
- For deprecated APIs, update manifests to supported versions
- For new required values, update `values.yaml` and document changes
- If upgrade fails, rollback and analyze diff output for root cause
- Communicate all risks and required actions to stakeholders
