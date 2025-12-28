---
id: 1201
---
﻿# Protocol Inheritance

A protocol can inherit from one or more other protocols and can add further requirements on top of the requirements it inherits. This is similar to class inheritance but works exclusively for protocols.

## Basic Syntax

You declare protocol inheritance by listing the protocols to inherit from after the protocol's name, separated by commas.

```swift
protocol InheritingProtocol: SomeProtocol, AnotherProtocol {
    // new requirements go here
}
```

## How It Works

When a protocol inherits from others, it effectively merges all their requirements into its own definition. Any type that conforms to the inheriting protocol **must** satisfy all requirements from the entire inheritance chain.

### Example: A Hierarchy of Protocols
```swift
protocol Printable {
    func printData()
}

protocol Sharable: Printable {
    func shareData()
}

// Conforming to Sharable requires implementing both printData() and shareData()
struct Document: Sharable {
    func printData() { print("Printing...") }
    func shareData() { print("Sharing...") }
}
```

## Why Use Protocol Inheritance?

1.  **Refinement**: You can create more specialized versions of a general protocol (e.g., `Equatable` -> `Comparable`).
2.  **Organization**: It helps group related requirements together into a logical hierarchy.
3.  **Flexibility**: You can define high-level interfaces that build upon low-level ones, allowing types to conform at the level of detail they need.

## Protocol Inheritance vs. Class Inheritance

*   **Classes**: A class can only inherit from **one** other class (single inheritance).
*   **Protocols**: A protocol can inherit from **multiple** other protocols.

```swift
protocol CombinedProtocol: ProtocolA, ProtocolB, ProtocolC {
    // Must satisfy A, B, and C
}
```

## Special Inheritance: Class-Only Protocols

You can limit a protocol's adoption to classes only by making it inherit from `AnyObject`.

```swift
protocol MyClassOnlyProtocol: AnyObject {
    // Requirements
}
```
If a `struct` or `enum` tries to conform to this protocol, it will result in a compiler error. This is essential when you need to use `weak` references to the protocol instance (e.g., for delegates).

## Best Practices

*   **Inherit when there is a true "is-a" relationship** or when one protocol truly refines another.
*   **Don't create deep inheritance hierarchies.** Keep your protocol trees shallow to avoid complexity.
*   **Use protocol composition (`&`)** instead of inheritance if you only need the combination of requirements in a single place (like a function parameter).
*   **Mark protocols as class-only (`AnyObject`)** if they are intended to be used as delegates to prevent retain cycles.

---

> [!TIP]
> Many standard library protocols use inheritance. For example, `Collection` inherits from `Sequence`, and `BidirectionalCollection` inherits from `Collection`.

