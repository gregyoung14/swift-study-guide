---
id: 1187
---
# Failable Initializers (`init?`) in Protocols

Protocols can define failable initializers, ensuring that any conforming type provides a way to initialize that might result in `nil`.

## 1. Protocol Requirement
```swift
protocol AuthenticatedUser {
    init?(token: String)
}
```

## 2. Implementing in a Struct
For structs, the implementation is straightforward.

```swift
struct User: AuthenticatedUser {
    let id: String
    
    init?(token: String) {
        if token.count < 10 { return nil }
        self.id = "valid_user"
    }
}
```

## 3. Implementing in a Class
Classes must use the `required` keyword to satisfy protocol initializer requirements.

```swift
class Admin: AuthenticatedUser {
    required init?(token: String) {
        if token != "admin_secret" { return nil }
    }
}
```

## 4. Satisfaction Rules
- A protocol requirement for `init?` can be satisfied by a non-failable `init`.
- A protocol requirement for `init` **cannot** be satisfied by a failable `init?`.

| Protocol Requirement | Implementation Option | Result |
| :--- | :--- | :--- |
| `init?` | `init?` | OK |
| `init?` | `init` | OK (Stronger guarantee) |
| `init` | `init?` | **ERROR** |

## 5. Why Use Failable Inits in Protocols?
Useful for types that are constructed from unreliable external data:
- **JSON Parsing**: `init?(json: [String: Any])`
- **File Loading**: `init?(filePath: String)`
- **Validation**: `init?(age: Int)` where only adults are allowed.

> [!NOTE]
> Failable initializers in protocols are key to building factory patterns or generic serialization systems where creation can fail gracefully.
