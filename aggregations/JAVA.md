# Title
AADR-001 - Java interfaces

# Applies
- JAVA

# Summary
Describes the way we use interfaces and implementations in Java.

# Conceptual
Despite the theoretical approach that an interface represents capabilities, we prefer the pragmatic approach.
We use interfaces...

- If we want to be prepared to swap implementations in the future

  ```mermaid
  flowchart TD
      IFoo(("«interface» IFoo")) --> DatabaseFooImpl
      IFoo --> FileFooImpl
      IFoo --> ETC["..."]
  ```

- If we want to be able to mock the implementation for testing purposes
- If we expect to use multiple interfaces (This is as close as Java gets to multiple inheritance)
- If we want to hide the implementation details from the caller and provide a clean contract
- If we actually want o express a reak capability like ISerializable

# Instructions and conventions
- An interface sits in its own file in the same directory as the implementation
- The name of an interface always starts with a capital I, followed by a capitalised identifier. Example: `IPersistenceService`
- The implementation for a single interface uses the naming convention `FooImpl` Example: `PersistenceServiceImpl.java`
- If an implementation implements multiple Interfaces there is no naming convention, general naming conventions as stated in `AADR-002` apply
- We are pragmatic in the use of interfaces. Only if we detect a meaningful use case for an interface we will create one. We do not create interfaces for the sake of it.

# Exclusions and antipatterns
- We do not create interfaces for the sake of it.

# Agent instructions
n/a

---

# Title
AADR-009 - The use of JavaDoc to document Java implementations

# Applies
- JAVA

# Summary
This record describes the way we use JavaDoc to document Java implementations.

# Conceptual
We want to use JavaDoc comments for two different purposes. The actual comment in the code should support the developer in understanding the code  "in-situ". The JavaDoc comments should as well allow us to generate a conclusive documentation of the code.

# Instructions and conventions
- Whenever the implementation is changed, all JavaDoc comments need to be verified against the actual code and all JavaDoc comments need to be updated if necessary. Stale and outdated JavaDoc comments are not acceptable.
-  We add JavaDoc comments in the following locations:
    - Class definitions
    - Public constructors
    - Public methods
    - Public fields
    - Interface definitions
- Class definitions should explain the intent of the class and the responsibilities of the class. The JavaDoc comments should be narrative in nature and should allow a developer to understand the class without having to read the code. Relevant internal and external dependencies should be mentioned and justified.
- For each public field, each input parameter of a method, and for the return value of a method call, the following details need to be given:
    - The intent of the parameter/return value ideally in an narrative form
    - An example usage of the parameter/return value
    - Any constraints on the parameter/return value
    - Any special values of the parameter/return value
- For each method all possible exceptions need to be described, as well as the circumstances that can lead to these exceptions.

# Exclusions and antipatterns
- JavaDoc comments should not be used to describe intent or implementation details of a method. This information should be contained in the code comments of the implementation itself.

# Agent instructions
- Upon each modification of the actual implementation, it is the agent's responsibility to verify and update all JavaDoc comments that are affected by the modification.
