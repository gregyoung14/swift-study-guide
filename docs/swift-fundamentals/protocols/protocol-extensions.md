---
id: 1200
---
﻿# Protocol Extensions

Protocol extensions are a core component of **Protocol-Oriented Programming (POP)** in Swift. They allow you to provide implementations for methods, initializers, subscripts, and computed properties to any type that conforms to a protocol.

## Why Protocol Extensions?

1.  **Code Reuse**: Instead of having every conforming type implement the same logic, you can define it once in a protocol extension.
2.  **Default Implementations**: You can make protocol requirements optional by providing a default implementation.
3.  **Extended Functionality**: You can add new methods to a protocol that weren't even part of the original protocol definition.

## Basic Syntax
```swift
protocol Greeter {
    var greeting: String { get }
    func sayHello()
}

// Providing a default implementation for sayHello()
extension Greeter {
    func sayHello() {
        print("\(greeting)!")
    }
}
```

## How It Works

When a type conforms to a protocol, it can either use the default implementation provided in the extension or provide its own **custom implementation** which will override the default.

### Example: A Collection Extension
You can extend standard library protocols to add your own convenience methods.

```swift
extension Collection where Element: Equatable {
    func allItemsEqual() -> Bool {
        guard let firstItem = first else { return true }
        return allSatisfy { $0 == firstItem }
    }
}
```

## Static vs. Dynamic Dispatch in Protocol Extensions

Understanding dispatch is crucial when working with protocol extensions:

*   **Requirement in Protocol**: If a method is declared in the protocol **and** implemented in an extension, it uses **Dynamic Dispatch**. The implementation in the concrete type (if any) is called.
*   **Only in Extension**: If a method is ONLY defined in the extension (not declared in the protocol), it uses **Static Dispatch**. The implementation called depends on the type of the variable at compile time.

```swift
protocol P {
    func requirement()
}

extension P {
    func requirement() { print("Default Requirement") }
    func extensionOnly() { print("Extension Only") }
}

struct S: P {
    func requirement() { print("Custom S Requirement") }
    func extensionOnly() { print("Custom S Extension Only") }
}

let instance: any P = S()
instance.requirement()   // Prints: "Custom S Requirement"
instance.extensionOnly() // Prints: "Extension Only" (Static Dispatch)
```

## Adding Constraints to Extensions

You can use the `where` clause to limit the extension's availability to types that meet specific criteria.

```swift
protocol Stack {
    associatedtype Element
    mutating func push(_ item: Element)
}

// Only add this functionality if the Elements are Equatable
extension Stack where Element: Equatable {
    func isTop(_ item: Element) -> Bool {
        // implementation...
    }
}
```

## Best Practices

*   **Use extensions for default implementations** to make your protocols more powerful and easier to adopt.
*   **Be careful with methods defined ONLY in extensions.** Remember they won't be dynamically dispatched if the instance is cast to the protocol type.
*   **Organize your code with extensions.** Group related logic into protocol extensions to keep your concrete types clean.
*   **Use `where` clauses** to provide specialized functionality for specific type combinations.

---

> [!IMPORTANT]
> Protocol extensions cannot store state. You cannot add stored properties to a protocol via an extension; you can only add computed properties.

