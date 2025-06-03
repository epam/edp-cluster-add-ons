# GitHub Copilot Integration for EDP Cluster Add-ons Repository

This directory contains files that enhance GitHub Copilot's ability to assist with development in this repository. These files provide context-aware instructions and reusable prompts tailored specifically for working with EDP Cluster Add-ons.

## Features

### 1. Global Instructions

- `copilot-instructions.md`: Global instructions that apply to all Copilot interactions in this repository

### 2. Context-Specific Instructions

The `instructions/` directory contains specialized instruction files that Copilot uses when working with specific file types:

- `addon-development.instructions.md`: Guidelines for developing add-ons
- `helm-best-practices.instructions.md`: Best practices for Helm charts
- `custom-addon-development.instructions.md`: Guidelines for creating custom add-ons

### 3. Reusable Prompts

The `prompts/` directory contains pre-defined prompts for common tasks:

- `create-new-addon.prompt.md`: Create a new add-on from scratch
- `update-existing-addon.prompt.md`: Update an existing add-on
- `integrate-third-party-chart.prompt.md`: Integrate a third-party Helm chart
- `customize-addon-config.prompt.md`: Customize an add-on's configuration
- `troubleshoot-addon-deployment.prompt.md`: Troubleshoot deployment issues
- `getting-started.prompt.md`: Get started with the repository
- `create-github-issue.prompt.md`: Create a GitHub issue following repository standards
- `create-github-pr.prompt.md`: Create a pull request with proper formatting and workflow

## Using Copilot with This Repository

### Automatic VS Code Configuration

This repository includes a `.vscode` directory with configuration files that automatically set up VS Code for optimal use with GitHub Copilot:

- `settings.json`: Configures VS Code to enable Copilot features with language-specific guidance:
  - General Kubernetes and Helm chart expertise

When you open this repository in VS Code, you'll be prompted to install recommended extensions and the appropriate settings will be applied automatically.

The provided debug configuration helps with validating Helm templates directly from VS Code. To use it:

1. Open any file within a Helm chart
2. Press F5 or use the Run and Debug panel
3. Select "Helm Template Debug"

This will execute `helm template` and `helm lint` commands for the chart and display the results in the debug console.

### Enabling Instructions and Prompts

1. Enable instructions and prompts in VS Code settings:
   - Set `chat.promptFiles` to `true`
   - Set `github.copilot.chat.codeGeneration.useInstructionFiles` to `true`

2. VS Code will automatically apply these instructions when you're working with files in this repository.

### Using Pre-defined Prompts

To use a pre-defined prompt:

1. In the VS Code Copilot Chat panel, type `/` followed by the prompt name, e.g.:

   ```bash
   /create-new-addon
   ```

2. Alternatively, run the "Chat: Run Prompt" command from the command palette and select a prompt file.

3. Follow the interactive guidance provided by the prompt.

### Benefits of Using These Prompts and Instructions

- **Consistency**: All add-ons will follow repository standards and patterns
- **Efficiency**: Reduce time spent on repetitive setup tasks
- **Best Practices**: Automatically incorporate project guidelines and best practices
- **Documentation**: Generate comprehensive and standardized documentation

## Customizing Instructions and Prompts

Feel free to improve these instructions and prompts as the repository evolves:

1. Update the instruction files when best practices change
2. Add new prompt files for additional common tasks
3. Refine existing prompts based on user feedback

Remember to keep instructions concise, specific, and aligned with the repository's standards.
