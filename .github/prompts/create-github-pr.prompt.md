---
mode: 'agent'
description: 'Create a GitHub pull request following repository standards'
---

# Create GitHub Pull Request

I'll help you create a PR with proper conventional commits and repository standards.

## Quick Commands

Use shorthand format: `/create-github-pr [option] [issue-number]`

**Options:**
- `c` - Create commit then PR
- `sc` - Create signed commit then PR
- `pr` - Create PR from latest commit

**Examples:**
- `/create-github-pr sc 343` (signed commit for issue #343)
- `/create-github-pr pr 401` (PR from latest commit for issue #401)

## What I'll Do

**For commits (c/sc):**
1. Check you're on a feature branch (not main)
2. Generate conventional commit message: `type(scope): description (#issue)`
3. Create commit and push to feature branch

**For PR creation (all options):**
1. Analyze changes using `git log -1 --patch`
2. Create PR description from repository template
3. Submit PR targeting `main` branch
4. Provide PR link

## Repository Standards

- Feature branches: `feat/gh-{issue}` or `fix/gh-{issue}`
- Always target `main` branch
- Never push directly to main
- PRs must reference issue numbers

Ready? Use the shorthand format or tell me your option and issue number.

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
