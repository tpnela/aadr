# Title
AADR-008 - Git Usage, Branching Strategy, and Commit formatting

# Applies
- ALL

# Summary
Define the overarching goal of using Git: maintaining a clean, linear, and searchable history that acts as continuous documentation of intent.

# Conceptual


# Instructions and conventions
- main and develop are protected branches and can only be modified by merging pull requests.
- All feature branches must be created from develop.
- Feature branching follow a naming schema starting with a prefix indicating the type of work followed by a short description of the work. Example: `feature/add-user-authentication`
- The following prefixes are possible:
    - feat: for new features
    - fix: for bug fixes
    - docs: for documentation
    - refactor: for refactoring
    - test: for test changes
    - release: for release branches
- We strictly enforce atomicity of commits. Each commit should represent a single logical change.
- We follow Conventional Commits specification for commit messages. using these prefixes:
    - feat: for new features
    - fix: for bug fixes
    - docs: for documentation
    - refactor: for refactoring
    - perf: for performance improvements
    - chore: for other changes
- Commit messages (after the CC prefix) are short and meaningful (max 50 characters).
- To sync with changes from github actions or other automated processes, we use `git pull --rebase` instead of `git pull`.

# Exclusions and antipatterns
- No secret leaks: Never commit `.env` files, credentials, or API keys
- Do not commit compilation artifacts (like .jar or /target directories) unless explicitly required by a specific use case.


# Agent instructions
- When executing a commit on behalf of the user, the agent MUST automatically format the message using Conventional Commits.
- The agent MUST default to adding files individually (`git add <file>`) rather than using a blanket `git add .`, to minimize the risk of committing unintended files.
- The agent MUST NOT automatically merge into or commit to the main or develop branches unless explicitly instructed by a verified user workflow (or previously marked as safe).