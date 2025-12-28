---
id: 33
---
# Method Injection (Parameter Injection)

**Method Injection** (also known as Parameter Injection) is a pattern where a dependency is passed as an argument directly to the method that needs it, rather than being stored in an initializer or a property.

## When to use Method Injection

Method injection is ideal for **ephemeral** dependencies—tools that an object needs only for a specific task, not for its entire lifetime.

### Use Case 1: Tightly Scoped Tasks
If a class only needs a database to "save" but not to "load" or "observe," passing the database to the `save` method is cleaner.

```swift
class OrderProcessor {
    func process(order: Order, using db: DBConnection) {
        // Logic...
        db.save(order)
    }
}
```

### Use Case 2: External State
Injecting a value that varies constantly, such as a `Date` or a `User` object.

```swift
func calculateAge(on date: Date = Date()) {
    // Injecting the date allows us to test "what will my age be in 2040?"
}
```

## Advantages of Method Injection

1.  **Granular Control**: You only provide the dependency when it is actually needed.
2.  **Statelessness**: The object doesn't need to store the dependency, making it lighter and thread-safe.
3.  **Explicit Context**: It makes the requirements of a specific action obvious.

## Disadvantages

1.  **Dependency Tunneling**: If `Method A` calls `Method B` which needs a dependency, `Method A` must also accept that dependency just to pass it along.
2.  **API Noise**: Public methods can become cluttered with many parameters.

## Comparison with Initializer Injection

| Feature | Initializer Injection | Method Injection |
| :--- | :--- | :--- |
| **Storage** | Persists for object life | Exists only for the call |
| **When to use** | Core Services (API, DB) | One-off helpers (Formatter, Context) |
| **Testability** | Excellent | Excellent |
| **API Cleanliness** | Cleaner methods | Potentially messy methods |

## Visualizing Method Injection Flow
```mermaid
graph LR
    C[Caller] -->|Method Call + Dependency| O[Object]
    O -->|Uses| D[Dependency]
    Note over O: Logic happens here
    O -- Returns Result --> C
    Note over D: Dependency is dropped
```

## Pro-Tip: Default Parameters
In Swift, you can use default parameters with method injection to keep the call-site clean while still allowing for testing.

```swift
func fetchData(session: URLSession = .shared) { ... }

// Production: fetchData()
// Test: fetchData(session: mockSession)
```

## Summary
Method Injection is a precision tool. Use it for utilities, data contexts, or specific operations that don't define the identity of the class. For core services that the class relies on for most of its work, stick to **Initializer Injection**.
