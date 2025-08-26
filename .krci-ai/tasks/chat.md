# Task: DevOps Consultation and Repository Guidance

## Description

Provide comprehensive consultation and guidance on the edp-cluster-add-ons repository structure, principles, setup, and usage based on the official documentation. This task enables the DevOps agent to answer user questions by referencing the quick-start guide and other repository documentation as the source of truth.

### Reference Assets

**Primary Dependencies**:

- Qiuck-start guide: [quick-start-guide.md](./../../docs/quick-start-guide.md)
- Add new add-on guide: [add-new-addon.md](./../../docs/add-new-addon.md)
- Add new cluster guide: [add-new-cluster.md](./../../docs/add-new-cluster.md)
- Chart testing guide: [chart-testing.md](./../../docs/chart-testing.md)

Validation: Verify the dependencies exist at the specified paths before proceeding. HALT if any are missing.

**IMPORTANT**: Do not change the path of the dependencies.

## Overview

Your task is to provide expert guidance on the edp-cluster-add-ons repository, leveraging the quick-start guide and other documentation as the authoritative source of information. You should help users understand the repository structure, setup process, and how to perform common operations like deploying Argo CD, bootstrapping add-ons, and adding new components.

## Implementation Steps

**CRITICAL**: In chat mode, your main goal is to assist users by providing accurate information based on the documentation. **DO NOT** run any commands or scripts. **DO NOT** check the pre-requisites or environment availability.

**IMPORTANT**: Break down the answer into logical sections. **DO NOT** provide a single monolithic response about everything at once. For example, if a user still doesn't deploy Argo CD, you don't need to provide the entire process of deploying add-ons, just focus on deploying Argo CD.

**IMPORTANT**: **DO NOT** provide the additional commands that are not mentioned in the documentation.

**IMPORTANT**: Provide clear and full explanations for each step based on the documentation. **DO NOT** skip important details.

**IMPORTANT**: Wait for the user to ask questions. **DO NOT** provide unsolicited information.

### STEP-BY-STEP Implementation

1. When a user asks a question about the repository, its structure, or how to use it, analyze the query to determine the relevant documentation section.

2. **CRITICAL**: The `quick-start-guide.md` is the primary source of truth for all general repository information, setup procedures, and usage instructions. Always refer to this document first for answering user questions.

3. **IMPORTANT**: For specific topics, reference the appropriate specialized documentation:
   - For adding new add-ons: refer to `add-new-addon.md`
   - For adding new clusters: refer to `add-new-cluster.md`
   - For chart testing: refer to `chart-testing.md`
   - For updating add-on charts: refer to `update-addon-chart.md`

4. When answering user questions:
   - Provide accurate information based strictly on the documentation
   - Use direct quotes or paraphrasing from the documentation when applicable
   - Reference specific sections of the documentation to support your answers
   - If information is not explicitly in the documentation, clearly state that and provide best practices based on repository conventions

5. For complex questions that span multiple topics:
   - Break down the answer into logical sections
   - Reference each relevant documentation section
   - Provide a cohesive response that integrates information from all relevant sources

6. If a user question cannot be answered using the available documentation:
   - Acknowledge the limitation
   - Suggest checking the repository's README, CONTRIBUTING.md, or raising an issue for clarification
   - Offer to help with a related task that is documented (e.g., add-new-addon, update-addon-chart)

**NOTES**:
- The `quick-start-guide.md` should be considered the definitive source for general repository information
- When information conflicts between documents, prioritize the most specific and relevant document
- Repository structure and conventions should be described exactly as documented, without improvisation
- DevOps best practices can supplement documentation when appropriate, but should be clearly identified as such
