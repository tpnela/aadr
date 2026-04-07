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
