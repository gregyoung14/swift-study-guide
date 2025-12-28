---
id: 1189
---
# Initializers in Protocols

Protocols can define specific initializers that conforming types must implement. This ensures that you can create instances of any conforming type in a consistent way.

## 1. Syntax
Define the initializer signature just as you would in a class or struct, but without any body braces.

```swift
protocol Account {
    init(username: String)
}
```

## 2. Implementing in Structs
Structs satisfy the requirement by providing the matching initializer.

```swift
struct UserAccount: Account {
    init(username: String) { ... }
}
```

## 3. Implementing in Classes (`required`)
When a class implements a protocol initializer, it must use the `required` keyword. This ensures that all subclasses also implement the initializer, maintaining protocol conformance.

```swift
class BaseAccount: Account {
    required init(username: String) { ... }
}
```

## 4. Initializers and Inheritance
If a subclass overrides a required initializer from a superclass, it must mark it with both `override` and `required`.

```swift
class SpecialAccount: BaseAccount {
    required override init(username: String) { ... }
}
```

## 5. Dependency Injection
Protocol initializers are very useful for dependency injection and factory patterns.

```swift
func createAccount<T: Account>(type: T.Type, user: String) -> T {
    return T(username: user)
}

let newAccount = createAccount(type: UserAccount.self, user: "john_doe")
```

> [!IMPORTANT]
> Protocol initializers are why we use `.self` and `.Type` when working with meta-programming in Swift. They give the compiler a guarantee that a specific `init` exists on the type object itself.
