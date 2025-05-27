---
mode: 'agent'
description: 'Create a GitHub issue for the EDP Cluster Add-ons repository'
---
# GitHub Issue Creator for EDP Cluster Add-ons

I'll help you create a GitHub issue in the epam/edp-cluster-add-ons repository following the appropriate template.

## Available Tools

The following tools are available for issue management:

**GitHub Tools:**
- `create_issue` - Creates a new issue in the repository
- `list_issues` - Lists existing issues (helpful for checking duplicates)
- `get_issue` - Gets details of a specific issue
- `add_issue_comment` - Adds a comment to an existing issue

**Filesystem Tools:**
- `read_file` - Reads the content of template files from the local filesystem
- `file_search` - Can be used to locate template files if needed

## Issue Types

The repository supports two types of issues:
1. **Bug Reports** - For reporting issues or unexpected behavior
2. **Feature Requests** - For suggesting new features or improvements

## Process for Creating Issues

1. I'll ask which type of issue you want to create
2. Based on your selection, I'll guide you through filling out the necessary information
3. I'll present a draft of the issue for your review
4. Upon your confirmation, I'll create the issue in the repository
5. I'll provide a link to the newly created issue

## Repository Information

- **Owner**: epam
- **Repository**: edp-cluster-add-ons

## Approach

I'll help you create a well-structured issue that follows the repository's templates and GitOps principles outlined in the repository's documentation. I'll ensure that:

1. The issue title is clear and descriptive
2. All required information from the template is included
3. The issue is appropriately labeled (if labels are provided)
4. Any specific requirements for the EDP Cluster Add-ons repository are addressed

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
