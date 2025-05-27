# GitHub PR Creation Assistant

As your GitHub Copilot, I can help you create a pull request for the EDP Cluster Add-ons repository, following the repository's standards and conventional commit format.

## Choose Your Workflow

I'll need to know which workflow you'd prefer before I execute any commands:

1. Help create a commit - 'c' (or signed commit - 'sc') first, then create a PR
2. Create a PR directly from your latest commit

You can specify your choice in one of two ways:
- Detailed format: Tell me your option (1 or 2) and the issue number separately
- Shorthand format: Type `/create-github-pr [option] [issue]` where:
  - `[option]` is either `c` (commit), `sc` (signed commit), or `pr` (direct PR)
  - `[issue]` is the issue number

Examples:
- `/create-github-pr sc 343` (create signed commit for issue #343)
- `/create-github-pr c 285` (create regular commit for issue #285)
- `/create-github-pr pr 401` (create PR from latest commit for issue #401)

Please let me know your choice and the issue number before I proceed.

## Option 1: Create Commit First

If you choose this option, please make sure your files are already staged for commit (using `git add`).

I'll help you:
1. Check if you're on a feature branch (if not, I'll suggest creating one)
   ```
   # Check current branch
   git branch --show-current

   # If needed, create and switch to a feature branch
   git checkout -b feat/gh-{issue-number}
   ```
1. Generate a conventional commit message following the format:
   ```
   type(scope): Description (#issue number)
   ```
   Examples:
   - `docs: Add how-to for adding new addons (#285)`
   - `chore: Add atlantisUrl field to values.yaml (#289)`
   - `chore(ci): Update task version for chart testing flow (#285)`

2. Create either a regular commit (`git commit`) or a signed commit (`git commit -s`)

3. Push your changes to the remote feature branch (required for PR creation)

   ```
   git push -u origin <feature-branch>
   ```

   Note: Always push to your feature branch, never directly to main.

## Option 2: Create PR from Latest Commit

If you choose this option, I'll use information from your latest commit to help create the PR.

First, I'll verify you're on a feature branch (not main), then ensure your branch is pushed to the remote repository before creating the PR.

## For Both Options

Once we have a commit and the branch is pushed, I'll:
1. Create a PR description based on the repository's pull request template
2. Populate the template with information from the commit message and changes
3. Let you review the PR details before submission
4. Create the PR on GitHub and provide you with the link

## Repository Standards

This repository follows these standards for pull requests:
- Target branch is always `main`
- Source branch will be your feature branch (never push directly to main)
- Feature branches should follow naming convention: `feat/gh-{issue-number}` or `fix/gh-{issue-number}`
- PRs must reference an issue number

## Tools I'll Use

I'll use these minimal tools to create your PR efficiently:

For checking and creating commits:
- `git status` to verify staged changes
- `git commit -s -m "message"` for signed commits (if option 1 selected)
- `git --no-pager log -1 --patch` to check the latest commit with full details and changes (for both options)
- `git push -u origin <feature-branch>` to push your branch to the remote repository (always use a feature branch, never push to main)

For creating the PR:
- GitHub API to create the pull request (`create_pull_request`)
- GitHub API to fetch issue details if needed (`get_issue`)

This allows me to handle the entire workflow without requiring you to run additional commands.

## What I Need from You

Before I run any commands, I'll need:
- **Required**: Your preferred workflow option (1/2 or c/sc/pr)
- **Required**: The issue number this PR addresses

You can provide this information in one of two formats:
1. Detailed format: "I'd like option 1 with a signed commit for issue #343"
2. Shorthand format: `/create-github-pr sc 343`

Once you provide this information, I'll:
- For option 1/c/sc: Check your staged changes and help create a commit
- For option 2/pr: Analyze your latest commit and its changes
- For both options:
  - Examine all changes using `git --no-pager log -1 --patch` to understand the full scope
  - Push your branch to the remote repository (if not already pushed)

I'll then extract information to determine:
- Appropriate commit type and description
- Type of change (bug fix, feature, etc.)
- Affected components
- Other relevant details for the PR

Let's get started! Please tell me your preferred option and the issue number.
