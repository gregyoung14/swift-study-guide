---
id: 6
---
# Common Pitfalls and Best Practices

Implementing Dependency Injection (DI) incorrectly can sometimes lead to more complexity rather than less. As a Senior iOS Engineer, avoiding these common traps is essential for a clean, scalable architecture.

## Common Pitfalls

### 1. The Service Locator "Anti-Pattern"
Passively fetching dependencies from a global registry *inside* a class is often called the Service Locator pattern. While it uses a container, it creates hidden dependencies.

-   **Wrong**: `init() { self.api = Container.shared.resolve(API.self) }`
-   **Right**: `init(api: API) { self.api = api }` (Let the caller resolve it).

### 2. Over-Engineering (DI for the sake of DI)
Injecting every tiny helper (like a simple math utility or a date formatter that doesn't change) can add unnecessary boilerplate.
-   **Rule of Thumb**: If it doesn't represent data, a stateful service, or something you need to mock for tests, you might not need to inject it.

### 3. Tight Coupling to the DI Framework
If you import your DI library (like Swinject or Needle) into every file, your code is now dependent on that framework.
-   **Best Practice**: Keep the DI framework logic limited to the **Composition Root**. Your business logic should be pure Swift.

## Best Practices

### 1. Favor Constructor Injection
It is the only pattern that guarantees your object is always in a valid state with all its mandatory requirements met at compile-time.

### 2. Use Protocols as Boundaries
Never inject concrete classes (unless they are simple data holders). Always inject protocols.
-   `init(service: NetworkServiceProtocol)` is better than `init(service: NetworkService)`.

### 3. Keep the "Composition Root" High
The instantiation and wiring of your objects should happen as high up in the call stack as possible (e.g., in the `AppDelegate`, `SceneDelegate`, or a `Coordinator`).

### 4. Grouping for Readability
If you find yourself passing the same 5 dependencies to 10 different ViewModels, create a specialized `ServiceRegistry` or `Environment` object to group them.

## Comparison: Clean vs. Messy DI

| Feature | Messy DI | Clean DI |
| :--- | :--- | :--- |
| **Location** | Injected everywhere | Restricted to Composition Root |
| **Visibility** | Hidden via Service Locators | Explicit in Initializers |
| **Dependencies** | Hard-coded concrete types | Protocols / Abstractions |
| **Frameworks** | Framework imports in ViewModels | PURE Swift in ViewModels |

## Pro-Tip: Interface Segregation
Don't pass a giant protocol that contains 50 methods if the class only needs 2. Break protocols down into smaller, focused interfaces (ISP from SOLID).

```swift
protocol UserLoader { func load() }
protocol UserSaver { func save() }

// Class only gets what it needs
class ProfileEditor {
    init(loader: UserLoader, saver: UserSaver) { ... }
}
```

## Summary
The goal of DI is to make your code more "honest" about what it needs. By avoiding service locators and keeping framework-specific logic isolated, you ensure that your business logic remains testable, portable, and easy to understand.
