---
id: 1170
---
# Adding Conformance to Types

In Swift, you can make a type conform to a protocol either in its initial declaration or by using an extension. This allows you to add protocol conformance to types that you didn't write, such as those from Apple's frameworks.

## 1. Conformance in Declaration
The most common way is to list the protocols after the type name (and after any superclass if it's a class).

```swift
struct MyType: ProtocolA, ProtocolB {
    // Implementation of requirements...
}
```

## 2. Using Extensions (Recommended)
You can use an **Extension** to add protocol conformance. This is considered a best practice because it groupings all the protocol-related code in one place.

```swift
extension MyType: ProtocolC {
    func requiredMethod() {
        // Implementation
    }
}
```

## 3. Conforming to Foreign Types
You can make standard Swift types or library types conform to your own protocols.

```swift
protocol Describable {
    var descriptionSnippet: String { get }
}

extension Int: Describable {
    var descriptionSnippet: String {
        return "This is the number \(self)"
    }
}

print(42.descriptionSnippet) // Works!
```

## 4. Why Use Extensions for Conformance?
- **Separation of Concerns**: Keeps your main type definition clean.
- **Organization**: If a type conforms to 5 protocols, you can have 5 separate extensions.
- **Retroactive Modeling**: Adding behavior to types you don't control (like `String` or `UIView`).

## 5. Summary Table
| Method | Use Case | Benefits |
| :--- | :--- | :--- |
| **Declaration** | Simple types | Concise for small implementations |
| **Extension** | Most production code | Better organization, retroactive conformance |

> [!TIP]
> Use a separate extension for each protocol conformance. This makes it much easier to find and maintain the implementation of each "contract."
