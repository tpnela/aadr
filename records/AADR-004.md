# Title
AADR-004 - Documenting the application (INCOMPLETE)

# Applies
- ALL

# Summary
Documentation satisfies varies needs
- A developer needs to understand implementation details
- An architect needs to understand the overall application architecture
- A DevOps engineer needs to understand how to deploy, configure, monitor and troubleshoot an application
- A business user needs a user manual
This AADR describes the various facets of documentation and the resulting artefacts

# Conceptual
We will need to ceate the following artefacts in compliance with a basic set of ground rules
- Documentation directly in the source code i.e. code comments
- An architecture documentation that is maintained in `docs/archbook.md`
- If we expose a REST interface, an OpenAPI spec (https://spec.openapis.org/oas/v3.1.0.html)
- A runbbok for DevOps engineers that is maintained in `docs/runbook.md`
- A user manual that is maintained in `docs/handbook.md`

# Instructions and conventions
- All 4 facets of documentation (comments, archbook.md, runbook.md, handbook.md) are updated upon *each change* to implementation or configuration
- Documentation updates need to make sure to fully represent the *current implementation* this means that all outdated and stale content needs to be removed. I.e. do not only add documentation *always* check existing documentation for relevance.
- Rules for code comments
  - If we already have custom comments for document generation (like JavaDoc) we do not add duplicate comments
  - Methods and functions are documented with a short summary of functionality, a list of all input parameters with type and a short example, the return value with type and a short example
  - Functional blocks like loops, if-else branches, switches, lambdas, etc are preceeded with a short explanation.
  - Each optional execution (if-else, switch, ...) carries an explanation on *each* turn why and when this turn is taken.
  - In general, comments are done in active tense and in a narrative style, akin to a devloper explaining execution in a sort of "running commentary"
- General rules for markdown generation
  - Visualisations should be added when meaningful. Visualisations can take the following forms:
    - Mermaid charts (preferrably pick an appropriate UML standard chart)
    - ASCII art visualisation sitting in a code block 
- Rules for `docs/archbook.md`
  - The archbook documents the existing implementation concepts but, as part of the "loop of structural integrity (See AADR-010)" ensures as well uniformity and repeatability
  - The archbook is structured into the following chapters
    - Executive summary - Describing in narrative form the overall architecture, uses mermaid charts to clarify structuer and concept
    - Structural breakdown - In a consecutive hierarchy of blackbox/whitebox descriptions we dig into the complete architecture (See: https://faq.arc42.org/questions/B-9/)
    - Dependencies - A *full list* of all external and internal dependencies of the application
    - Models - a *full list* of all business object entities (database tables, messages, files). Main focus is on uniformity of different instances of business objects.
- Rules for `docs/runbook.md`
  -    

# Exclusions and antipatterns

# Agent instructions
This section is directed towards an AI agent in a software development environment.
All other parts of the record should be relevant for humans as well as for AI coding agents.
This section is only relevant for AI agents.
