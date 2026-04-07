# Title
AADR-006 - Logging practises
# Applies
- ALL

# Summary
To normalise syntax and semantics of application logs, we follow these guidelines

# Conceptual
Logging supports various aspects of the software cycle. We use logs to debug, to profile and to monitor applications. We use log messages for post-mortem analysis and to understand the behaviour of the application in production.

# Instructions and conventions
- By default, an implementation logs to STDOUT
- Log statements are always **one line** of well formed JSON
- The log statement follows this structure: `{timestamp} {level} {service} ({correlationId}) {message}`
  - `timestamp` is the ISO 8601 timestamp of the log statement
  - `level` is the log level (INFO, WARN, ERROR, DEBUG, TRACE)
  - `service` is the name of the service that generated the log statement
  - `correlationId` (Optional) is the correlation ID of the log statement
  - `message` is the log message
- If a business process requires tracing across multiple services, the implementation needs to be instrumented in such a way that the correlation ID is propagated through the call stack
- A log statement should be narrative by nature and contaion a reasonable amount of context information.
  - Example: `Tried to create a salesorder for customer {custId} but failed because we don't ship to {country}`
- We use log levels to express semantics. Verbosity between log levels varies. Content between log levels should be different in nature.
  - TRACE (Verbosity very high) represents statechanges for relevant business objects. TRTACE statements are issued for each iteration in a loop, recordset, tree traversal etc. It is important to pick varying business relevant values. Logging an unchanged value across a loop doesn't make sense.
  - DEBUG (Verbosity still high) This statement focusses on control flow like class instantiation, method entry and exit, loop iterations, conditional branches etc. DEBUG statements give insight into the implementation's control flow.
  - INFO (Verbosity medium) This statement focusses on business relevant events like order creation, order update, order deletion etc. INFO statements give insight into the business process.
  - WARN (Verbosity low) This statement focusses on warnings like order update failed, order deletion failed etc. WARN statements give insight into potential issues that don't prevent the application from continuing to run or have been fixed by corrective action like retries etc.
  - ERROR (Verbosity very low) This statement focusses on errors like order update failed, order deletion failed etc. ERROR statements give insight into issues that could result in data loss or loss of functionality.
  - FATAL (Verbosity very low) This statement focusses on errors that cause the termination of the application.
  
# Exclusions and antipatterns
- A log statement should be as short as possible, ideally not exceed 200 characters
- A log statement should not contain any sensitive information
- A log statement should not contain any PII
- A log statement should not contain any secrets (neither hashed nor encoded)
- A log statement should not contain any credentials (neither hashed nor encoded)
- A log statement should not contain any passwords (neither hashed nor encoded)
- A log statement should not contain any API keys (neither hashed nor encoded)
- A log statement should not contain any tokens (neither hashed nor encoded)
- A log statement should not contain any session IDs (neither hashed nor encoded)
- A log statement should not contain any user IDs (neither hashed nor encoded)
- A log statement should not contain any email addresses (neither hashed nor encoded)
- A log statement should not contain any phone numbers (neither hashed nor encoded)
- A log statement should not contain any addresses (neither hashed nor encoded)
- A log statement should not contain any credit card numbers (neither hashed nor encoded)
- A log statement should not contain any social security numbers (neither hashed nor encoded)
- A log statement should not contain any other sensitive information (neither hashed nor encoded)

# Agent instructions
- When generating the application configuration, make sure log levels can be configured for various environments by a simple configuration change.
- When generating code that produces log statements, make sure the log statements are well formed JSON and follow the structure defined in the instructions.

---

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
