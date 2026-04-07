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
