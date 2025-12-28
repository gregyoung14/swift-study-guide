---
id: 1199
---
﻿# Protocol Conformance

Protocol conformance is the process of a type (struct, class, or enum) adopting a protocol and implementing its required properties, methods, and initializers.

## Declaring Conformance

Conformance can be declared at the type's definition or in an extension.

### At Definition
```swift
struct Book: Equatable {
    let isbn: String
    let title: String
}
```

### Via Extension
It is common practice (and a best practice) to add protocol conformance in an extension. This helps organize your code by separating the core logic of the type from its protocol requirements.

```swift
extension Book: CustomStringConvertible {
    var description: String {
        return "\(title) (ISBN: \(isbn))"
    }
}
```

## Conditional Conformance

Conditional conformance allows a generic type to conform to a protocol only when its generic parameters satisfy certain requirements.

```swift
struct Box<T> {
    var content: T
}

// Box only conforms to Equatable if T also conforms to Equatable
extension Box: Equatable where T: Equatable {}
```

## Synthesized Conformance

Swift can automatically generate (synthesize) protocol conformance for certain standard protocols if all of a type's properties also conform to those protocols.

*   **`Equatable`**: Synthesized for structs and enums.
*   **`Hashable`**: Synthesized for structs and enums.
*   **`Comparable`**: Synthesized for enums without associated values.
*   **`Codable`**: Synthesized if all properties are `Codable`.

```swift
struct User: Hashable {
    let id: UUID
    let name: String
    // No implementation needed; Swift synthesizes Hashable (and Equatable)
}
```

## Adding Conformance to External Types

One of the most powerful features of Swift is that you can make types you don't own (like `Int`, `String`, or `UIView`) conform to your own protocols using extensions.

```swift
protocol Reversible {
    func reversed() -> String
}

extension String: Reversible {
    // String already has a reversed() method, so it satisfies the protocol automatically
}
```

## Checking and Casting Conformance

You can check if an instance conforms to a protocol using the `is` and `as` keywords.

```swift
if let reversibleItem = someValue as? Reversible {
    print(reversibleItem.reversed())
}
```

## Best Practices

*   **One protocol per extension.** When adding conformance via extensions, use a separate extension for each protocol. This makes the code easier to read and navigate.
*   **Favor synthesized conformance.** Don't implement `Equatable` or `Hashable` manually unless you need custom behavior (e.g., comparing only specific fields).
*   **Use conditional conformance** to make your generic types more powerful and flexible.
*   **Document why a type conforms to a protocol**, especially if the conformance is added in a separate file.

---

> [!NOTE]
> Types in Swift can conform to any number of protocols, but they can only inherit from one superclass.

