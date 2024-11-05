# Enable EDP Capsule Tenant Provisioning

To enable EDP deployment under Capsule tenant management, follow these steps:

1. **Verify Capsule User Groups:**
   Ensure that the default [capsuleUserGroups](../capsule/values.yaml) in Capsule include the necessary users for provisioning the EDP namespace.
2. **Deploy Capsule:**
   Deploy Capsule using the [values.yaml](../../chart/values.yaml) file under the `capsule` section.
3. **Capsule Tenant Configuration:**
   When creating a namespace for EDP deployment under the Capsule tenant, make sure that the users responsible for provisioning the namespace - Tenant Owner is declared in [edp-tenant](edp-tenant.yaml).
4. **Deploy Capsule Tenant:**
   Deploy `capsule-tenant` using the [values.yaml](../../chart/values.yaml) file under the `capsule-tenant` section.
5. **Create EDP Namespace:**
   Create a namespace for EDP deployment under the Capsule [Tenant Owner](edp-tenant.yaml).
6. **Deploy EDP:**
   Deploy EDP using [values.yaml](../../chart/values.yaml) file under the `edp` section.
