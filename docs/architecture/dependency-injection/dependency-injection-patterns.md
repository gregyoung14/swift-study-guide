---
id: 14
---
# Dependency Injection Patterns

Dependency Injection is not a single tool but a set of patterns. Choosing the right pattern for the right situation is a key skill for a Senior iOS developer.

## The Big Three Patterns

### 1. Initializer Injection (Constructor Injection)
Dependencies are passed through the class initializer. This is the **preferred pattern** as it ensures the object is always valid and immutable.

-   **Pros**: Compile-time safety, immutability, thread-safety.
-   **Cons**: Can lead to "Initializer Bloat".

```swift
class ViewModel {
    let service: Service
    init(service: Service) { self.service = service }
}
```

### 2. Property Injection (Setter Injection)
Dependencies are assigned to public properties after the object is created.

-   **Pros**: Useful when you don't control the initializer (e.g., Storyboards, XIBs).
-   **Cons**: Mutability (`var`), no guarantee the dependency is set before use.

```swift
class ViewController: UIViewController {
    var service: Service? // Injected after instantiation
}
```

### 3. Method Injection (Parameter Injection)
The dependency is passed as a parameter to the specific method that needs it.

-   **Pros**: Keeps the dependency scope small; great for ephemeral tasks.
-   **Cons**: Caller must have the dependency available to pass it.

```swift
class DataManager {
    func save(user: User, using connection: DBConnection) {
        connection.execute("INSERT...")
    }
}
```

## Advanced Patterns

### Injected Property Wrappers
Modern Swift libraries often use property wrappers to hide the boilerplate of resolution.

```swift
class DetailViewModel {
    @Injected var network: NetworkClient
}
```

### Ambient Context
Providing a global but replaceable "Context" for low-level helpers like `Date()` or `UUID()`.

```swift
struct Current {
    static var date = { Date() }
}
// In tests: Current.date = { Date(timeIntervalSince1970: 0) }
```

## Pattern Selection Matrix

| Pattern | Best for | Primary Limitation |
| :--- | :--- | :--- |
| **Initializer** | 90% of your code | Parameter count bloat |
| **Property** | UIViewController / Delegates | Runtime nil checks |
| **Method** | DB Operations / Helpers | Passing burden on caller |
| **Wrappers** | Clean UI code | Testing difficulty |

## Summary
Most of the time, you should reach for **Initializer Injection**. It aligns best with Swift's safety-first philosophy. Use **Property Injection** as a backup for system-instantiated classes, and **Method Injection** for tightly scoped operations.
