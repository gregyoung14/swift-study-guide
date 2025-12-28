---
id: 1217
---
﻿# What Are Protocols?

A **protocol** is one of the most fundamental and powerful building blocks of the Swift programming language. It defines a blueprint of methods, properties, and other requirements that suit a particular task or piece of functionality.

## The Essence of Protocols

Think of a protocol as a **contract**. Any type (struct, class, or enum) that "signs" this contract (conforms to the protocol) promises to provide the specific implementation for the requirements outlined in the blueprint.

```swift
protocol Describable {
    var description: String { get }
}
```

In the example above, any type that conforms to `Describable` **must** provide a `description` property. How it provides that description—whether as a stored property or a computed one—is up to the type.

## Key Concepts

1.  **Abstraction**: Protocols allow you to focus on *what* a type can do rather than *how* it does it. This decouples your code and makes it more modular.
2.  **Composition over Inheritance**: Swift encourages using protocols and protocol extensions to share behavior across diverse types, rather than relying on a deep class inheritance hierarchy. This is the heart of **Protocol-Oriented Programming**.
3.  **Flexibility**: Unlike classes, both value types (structs, enums) and reference types (classes) can conform to protocols.
4.  **First-Class Citizens**: Protocols are types in their own right. They can be used as parameter types, return types, and elements in collections.

## Why Use Protocols?

*   **Interoperability**: Protocols like `Equatable`, `Hashable`, and `Codable` allow your custom types to work seamlessly with the Swift Standard Library and frameworks.
*   **Testability**: By depending on protocols instead of concrete classes, you can easily swap real implementations with **mocks** or **stubs** in your unit tests.
*   **Safety**: The compiler enforces protocol conformance. If you say a type conforms to a protocol but forget to implement a requirement, your code won't compile.

## Analogy

Imagine a protocol called `Drivable`. It requires a `startEngine()` method and a `steer()` method.
*   A `Car` conforms to `Drivable`.
*   A `Truck` conforms to `Drivable`.
*   A `Motorcycle` conforms to `Drivable`.

Even though a car's engine starts differently than a motorcycle's, any code that knows how to interact with a `Drivable` object can operate all three without needing to know the specific details of each.

---

> [!NOTE]
> Swift is often called a "Protocol-Oriented" language because its Standard Library is heavily built using protocols.

