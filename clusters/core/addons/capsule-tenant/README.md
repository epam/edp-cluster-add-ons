# Enable KubeRocketCI Capsule Tenant Provisioning

To enable KubeRocketCI deployment under Capsule tenant management, follow these steps:

1. **Verify Capsule User Groups:**
   Ensure that the default [capsuleUserGroups](../capsule/values.yaml) in Capsule include the necessary users for provisioning the KubeRocketCI namespace.
2. **Deploy Capsule:**
   Deploy Capsule using the [values.yaml](../../apps/values.yaml) file under the `capsule` section.
3. **Capsule Tenant Configuration:**
   When creating a namespace for KubeRocketCI deployment under the Capsule tenant, make sure that the users responsible for provisioning the namespace - Tenant Owner is declared in [krci-tenant](krci-tenant.yaml).
4. **Deploy Capsule Tenant:**
   Deploy `capsule-tenant` using the [values.yaml](../../apps/values.yaml) file under the `capsule-tenant` section.
5. **Create KRCI Namespace:**
   Create a namespace for KubeRocketCI deployment under the Capsule [Tenant Owner](krci-tenant.yaml).
6. **Deploy KubeRocketCI:**
   Deploy KubeRocketCI using [values.yaml](../../apps/values.yaml) file under the `kuberocketci` section.
