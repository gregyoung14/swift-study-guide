---
id: 26
---
# Initializer Injection (Constructor Injection)

**Initializer Injection** (often called Constructor Injection) is the most robust and recommended pattern for Dependency Injection in Swift. It involves passing an object's dependencies directly into its `init` method.

## Why it's the Gold Standard

### 1. Immutability
You can declare dependencies as `let` constants. This ensures that once the object is created, its behavior remains stable and thread-safe.

### 2. Compile-Time Safety
The compiler guarantees that the object cannot be instantiated without its mandatory dependencies. No more runtime "force-unwrap" crashes.

### 3. Clear Intent
The requirements of the class are immediately obvious to anyone reading the code.

```swift
class OrderViewModel {
    private let api: APIServiceProtocol
    private let database: DatabaseProtocol
    
    // Explicitly declaring what we need
    init(api: APIServiceProtocol, database: DatabaseProtocol) {
        self.api = api
        self.database = database
    }
}
```

## Handling Default Values
A common trick to reduce boilerplate while maintaining testability is to provide a default value in the initializer.

```swift
init(api: APIServiceProtocol = RealAPI.shared) {
    self.api = api
}
```
*Note: While convenient, some architects prefer leaving defaults out to ensure the Composition Root has full control.*

## Initializer Injection in the UI Layer
For `UIView` subclasses, Initializer Injection is preferred over setting properties after the fact.

```swift
class CustomHeaderView: UIView {
    let title: String
    
    init(title: String) {
        self.title = title
        super.init(frame: .zero)
        setupUI()
    }
    
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }
}
```

## Comparison with other Patterns

| Feature | Initializer Injection | Property Injection |
| :--- | :--- | :--- |
| **Safest?** | Yes | No |
| **Immutability?** | Yes (`let`) | No (`var`) |
| **Self-Documenting?** | Yes | No |
| **Storyboard Support?** | No | Yes |

## Common Pitfalls
-   **Parameter Count**: If you have more than 5-6 parameters, consider grouping them into a `Configuration` struct.
-   **Required Inits**: Apple's `required init?(coder:)` can be annoying but is a small price to pay for the safety of custom initializers.

## Summary
In any professional iOS codebase, **Initializer Injection** should be your default choice. It leverages Swift's powerful type system to prevent bugs and ensure that your software components are honest, thread-safe, and easy to test.
