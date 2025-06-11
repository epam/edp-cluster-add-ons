---
mode: 'agent'
description: 'Update an existing add-on in the EDP Cluster Add-ons repository'
---

# Update Existing Add-on

I'll help you update an existing add-on following proper versioning and GitOps practices.

## Tell Me About Your Update

1. **Add-on name**: Which add-on needs updating?
2. **Change type**: Version upgrade, configuration change, or other?
3. **Reason**: Why is this change needed?

## What I'll Help With

- Navigate to correct files in `clusters/core/addons/`
- Update Chart.yaml, values.yaml, or dependencies
- Increment chart version appropriately
- Update documentation if needed
- Provide validation commands

## Testing Commands I'll Provide

```bash
# Lint the updated chart
helm lint clusters/core/addons/{addon-name}

# Template validation
helm template clusters/core/addons/{addon-name}
```

Ready to update? Please specify which add-on and what changes you need.
