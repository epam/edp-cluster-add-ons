---
mode: 'agent'
description: 'Create a GitHub issue for the EDP Cluster Add-ons repository'
---

# Create GitHub Issue

I'll help you create a well-structured GitHub issue in the epam/edp-cluster-add-ons repository.

## Issue Types

Choose one:
- **Bug Report**: Report issues or unexpected behavior
- **Feature Request**: Suggest new features or improvements

## My Process

1. Determine issue type
2. Read appropriate template from `.github/ISSUE_TEMPLATE/`
3. Collect required information based on template
4. Check for duplicate issues
5. Create issue with proper formatting
6. Provide issue link

## What I Need

Just tell me:
- Issue type (bug or feature)
- Brief description of what you want to report/request

I'll guide you through the rest step by step.

**Repository**: epam/edp-cluster-add-ons

When you're ready, tell me which type of issue you'd like to create (Bug Report or Feature Request), and I'll guide you through the process step by step.

## Instructions for GitHub Copilot Agent

When helping a user create an issue:

1. First, determine whether they need a bug report or feature request

2. Retrieve the appropriate template content from the local filesystem:
   ```
   read_file(
     filePath: "<workspace-path>/.github/ISSUE_TEMPLATE/bug_report.md", // or feature_request.md
     startLineNumber: 1,
     endLineNumber: 100 // Adjust as needed
   )
   ```

3. For Bug Reports, collect information matching all sections in the template:
   - A clear description of the bug
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Kubernetes cluster type and version (if applicable)
   - Screenshots or additional context (if available)

3. For Feature Requests, collect:
   - Description of the problem/need
   - Proposed solution
   - Alternatives considered
   - Additional context

4. Draft the issue content using the template structure
5. Present the draft for user review and await confirmation
6. Upon confirmation, use create_issue to create the issue:
   ```
   create_issue(
     owner: "epam",
     repo: "edp-cluster-add-ons",
     title: <issue-title>,
     body: <formatted-body>,
     labels: [<optional-labels>]
   )
   ```
7. Get the issue details and provide the link to the user:
   ```
   get_issue(
     owner: "epam",
     repo: "edp-cluster-add-ons",
     issue_number: <created-issue-number>
   )
   ```

Remember to format the issue body in proper markdown and consider the repository's GitOps principles when suggesting solutions.

## Template References

The issue templates are available in the local filesystem:

- Bug Report Template: `.github/ISSUE_TEMPLATE/bug_report.md`
- Feature Request Template: `.github/ISSUE_TEMPLATE/feature_request.md`

These templates should be read directly from the filesystem using the `read_file` tool, rather than fetching them from GitHub. This ensures you're working with the actual templates in the user's workspace.

## Determining Workspace Path

Since the prompt refers to files in the local filesystem, you'll need to determine the workspace path first. You can identify the workspace path by:

1. Looking at the context provided in the conversation
2. Using the file paths from the editor context
3. Checking the repository structure from file_search results

Once you have identified the workspace path (e.g., `/Users/username/projects/edp-cluster-add-ons`), you can construct absolute file paths to read the templates:

```
// Example of constructing an absolute path
const workspacePath = "/Users/username/projects/edp-cluster-add-ons";
const templatePath = `${workspacePath}/.github/ISSUE_TEMPLATE/bug_report.md`;

read_file(
  filePath: templatePath,
  startLineNumber: 1,
  endLineNumber: 100
)
```

Make sure to replace placeholder paths with the actual workspace path from the user's environment.

## Example Workflow

Here's an example interaction flow to help guide the conversation:

1. Ask which type of issue the user wants to create

2. First, retrieve the appropriate template to see its structure:
   ```
   // For a bug report
   read_file(
     filePath: "<workspace-path>/.github/ISSUE_TEMPLATE/bug_report.md",
     startLineNumber: 1,
     endLineNumber: 100 // Adjust as needed
   )

   // For a feature request
   read_file(
     filePath: "<workspace-path>/.github/ISSUE_TEMPLATE/feature_request.md",
     startLineNumber: 1,
     endLineNumber: 100 // Adjust as needed
   )
   ```

3. Based on the template structure, collect all required information from the user

4. For a bug report, ask questions that match the template sections:
   - "Can you describe the bug you're experiencing?"
   - "What steps can someone follow to reproduce this issue?"
   - "What did you expect to happen?"
   - "What actually happened instead?"
   - "What type of Kubernetes cluster are you using? (vanilla, OpenShift, etc.)"
   - "Can you share the output of `kubectl version`?"
   - "Do you have any screenshots or additional context to share?"

4. For a feature request, ask questions that match the template sections:
   - "Is this feature request related to a problem? Can you describe it?"
   - "What solution would you like to see implemented?"
   - "Have you considered any alternative solutions or features?"
   - "Is there any additional context that would help understand your request?"

5. Before creating the issue, check for potential duplicates using:
   ```
   list_issues(
     owner: "epam",
     repo: "edp-cluster-add-ons",
     state: "open"
   )
   ```

6. You might also want to locate additional template files or documentation in the workspace if needed:
   ```
   file_search(
     query: "**/*.md"
   )
   ```
