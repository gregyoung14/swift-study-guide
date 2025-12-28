---
id: 1198
---
﻿# Protocol Composition

Protocol composition allows you to combine multiple protocols into a single, temporary type requirement. This is useful when you want to require that a type conforms to more than one protocol simultaneously without defining a new, named protocol that inherits from all of them.

## Syntax

You compose protocols by combining them with the ampersand (`&`) operator.

```swift
func process(item: Named & Identifiable) {
    print("Processing \(item.name) with ID \(item.id)")
}
```

## How it Works

A composition of protocols behaves like a single type that has all the members of all the included protocols. Any type that conforms to **all** the protocols in the composition can be passed where that composition is required.

### Simple Composition
```swift
protocol Named { var name: String { get } }
protocol Aged { var age: Int { get } }

struct Person: Named, Aged {
    var name: String
    var age: Int
}

func wishHappyBirthday(to celebrant: Named & Aged) {
    print("Happy birthday, \(celebrant.name)! You are \(celebrant.age).")
}

let user = Person(name: "Alice", age: 30)
wishHappyBirthday(to: user)
```

### Composition with Classes
You can also compose a protocol with a specific class type. This requires that the value must be a subclass of the specified class **and** conform to the specified protocol.

```swift
class ViewController {}
protocol Refreshable { func refresh() }

func handle(viewController: ViewController & Refreshable) {
    viewController.refresh()
}
```

## Why Use Protocol Composition?

1.  **Loose Coupling**: It avoids creating a deep hierarchy of named protocols (e.g., `NamedAndAgedAndIdentifiable`).
2.  **Specificity**: It allows you to specify exactly what requirements a function has, following the **Interface Segregation Principle**.
3.  **Ad-hoc Requirements**: It's perfect for one-off requirements where creating a new protocol name would be overkill.

## Protocol Composition vs. Protocol Inheritance

*   **Inheritance**: `protocol C: A, B {}` creates a new, named type `C`. Types must explicitly conform to `C`.
*   **Composition**: `A & B` is an anonymous type. Any type conforming to both `A` and `B` automatically satisfies the composition `A & B`.

## Use Cases

### Dependency Injection
When injecting dependencies, you might want to require that a service conforms to multiple capabilities.

```swift
typealias StorageService = ReadableStorage & WritableStorage

class DataManager {
    let storage: StorageService
    init(storage: StorageService) { self.storage = storage }
}
```

### Delegation
Composing delegate protocols to require multiple sets of callbacks.

```swift
weak var delegate: (UITableViewDelegate & UITableViewDataSource)?
```

## Best Practices

*   **Use `typealias` for common compositions.** If you find yourself using `Named & Aged & Identifiable` in many places, give it a meaningful name.
*   **Keep compositions small.** If you are composing more than 3-4 protocols, consider if your function is doing too much or if your protocols are too granular.
*   **Use composition for class-protocol requirements** to ensure you have access to both inheritance-based and protocol-based features.

---

> [!NOTE]
> Protocol compositions can contain any number of protocols, but can only contain at most one class type.

