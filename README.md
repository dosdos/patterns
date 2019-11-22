# Patterns

A collection of design patterns with an explanatory implementation in Python.

## Gang of Four (GoF) design pattern
The definition Gang of Four (GoF) comes from the book Design Patterns: Elements of Reusable Object-Oriented Software, Addison-Wesley Professional Computing Series, by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.
These 23 GoF patterns are generally considered the foundation for all other patterns.
They are categorized in three groups: Creational, Structural, and Behavioral.

### Creational Patterns
- [ ] Abstract Factory
- [ ] Builder
- [ ] Factory Method
- [ ] Prototype
- [x] Singleton

### Structural Patterns
- [x] Adapter
- [ ] Bridge
- [ ] Composite
- [ ] Decorator
- [ ] Facade
- [ ] Flyweight
- [ ] Proxy

### Behavioral Patterns
- [ ] Chain of Responsibility
- [ ] Command
- [ ] Interpreter
- [ ] Iterator
- [ ] Mediator
- [ ] Memento
- [ ] Observer
- [ ] State
- [ ] Strategy
- [ ] Template
- [ ] Visitor


# GRASP patterns
source: [Wikipedia](https://en.wikipedia.org/wiki/GRASP_%28object-oriented_design%29)

General Responsibility Assignment Software Patterns (or Principles), abbreviated GRASP, consist of guidelines for assigning responsibility to classes and objects in object-oriented design.
It is not related to the SOLID design principle. (see below)
All these 9 patterns answer some software problems, and have not been invented to create new ways of working, but to better document and standardize old, tried-and-tested programming principles in object-oriented design.

1. Controller
2. Creator
3. Indirection
4. Information expert
5. High cohesion
6. Low coupling
7. Polymorphism
8. Protected variations
9. Pure fabrication

# SOLID principles
source: [Wikipedia](https://en.wikipedia.org/wiki/SOLID)

1. **Single responsibility principle**: every module or class should have responsibility over a single part of the functionality provided by the whole software.
2. **Open-closed principle**: software entities (classes, modules, functions, etc.) should be open for extensions, but closed for modification.
3. **Liskov substitution principle**: Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program (see also design by contract).
4. **Interface segregation principle**: Many client-specific interfaces are better than one general-purpose interface (in other words: do not add additional functionality to an existing interface by adding new methods, instead, create a new interface and let your class implement multiple interfaces if needed).
5. **Dependency inversion principle**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
