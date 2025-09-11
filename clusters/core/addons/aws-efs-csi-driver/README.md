# aws-efs-csi-driver

![Version: 3.2.2](https://img.shields.io/badge/Version-3.2.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.1.11](https://img.shields.io/badge/AppVersion-2.1.11-informational?style=flat-square)

A Helm chart for installing the AWS EFS CSI driver

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://kubernetes-sigs.github.io/aws-efs-csi-driver/ | aws-efs-csi-driver | 3.2.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| aws-efs-csi-driver.controller.logLevel | int | `2` |  |
| aws-efs-csi-driver.controller.serviceAccount.annotations."eks.amazonaws.com/role-arn" | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_EFS_CSI_Driver"` |  |
| aws-efs-csi-driver.controller.serviceAccount.create | bool | `true` |  |
| aws-efs-csi-driver.controller.serviceAccount.name | string | `"efs-csi-controller-sa"` |  |
| aws-efs-csi-driver.controller.tags.BusinessUnit | string | `"EDP"` |  |
| aws-efs-csi-driver.controller.tags.CostCenter | string | `"2023"` |  |
| aws-efs-csi-driver.controller.tags.Department | string | `"DEP1"` |  |
| aws-efs-csi-driver.controller.tags.Environment | string | `"dev"` |  |
| aws-efs-csi-driver.controller.tags.Name | string | `"aws-efs-csi-driver-controller"` |  |
| aws-efs-csi-driver.controller.tags.SysName | string | `"ORG"` |  |
| aws-efs-csi-driver.controller.tags.SysOwner | string | `"YOUR-PROJECT"` |  |
| aws-efs-csi-driver.fullnameOverride | string | `"aws-efs-csi-driver"` |  |
| aws-efs-csi-driver.nameOverride | string | `"aws-efs-csi-driver"` |  |
| aws-efs-csi-driver.node.logLevel | int | `2` |  |
| aws-efs-csi-driver.node.serviceAccount.create | bool | `false` |  |
| aws-efs-csi-driver.node.serviceAccount.name | string | `"efs-csi-controller-sa"` |  |
| aws-efs-csi-driver.storageClasses[0].mountOptions[0] | string | `"iam"` |  |
| aws-efs-csi-driver.storageClasses[0].name | string | `"efs-sc"` |  |
| aws-efs-csi-driver.storageClasses[0].parameters.basePath | string | `"/dynamic_provisioning"` |  |
| aws-efs-csi-driver.storageClasses[0].parameters.directoryPerms | string | `"750"` |  |
| aws-efs-csi-driver.storageClasses[0].parameters.fileSystemId | string | `"fs-xxxxxxxxxxxxxx"` |  |
| aws-efs-csi-driver.storageClasses[0].parameters.gidRangeEnd | string | `"2000"` |  |
| aws-efs-csi-driver.storageClasses[0].parameters.gidRangeStart | string | `"100"` |  |
| aws-efs-csi-driver.storageClasses[0].parameters.provisioningMode | string | `"efs-ap"` |  |
| aws-efs-csi-driver.storageClasses[0].reclaimPolicy | string | `"Delete"` |  |
| aws-efs-csi-driver.storageClasses[0].volumeBindingMode | string | `"Immediate"` |  |

