---
id: 40
---
# Service Locator Pattern

The **Service Locator** is a design pattern that provides a centralized registry to look up services. In the context of Dependency Injection, it is often considered an **Anti-Pattern** when misused, as it tends to hide dependencies.

## How it Works
A global `ServiceLocator` object holds references to all your services. Any class in the app can reach out to the locator to "find" what it needs.

```swift
class ServiceLocator {
    static let shared = ServiceLocator()
    private var services: [String: Any] = [:]
    
    func addService<T>(service: T) { ... }
    func getService<T>() -> T { ... }
}
```

## The Anti-Pattern: Hidden Dependencies
The main reason senior engineers avoid Service Locators is that they hide a class's requirements.

### Using Service Locator (Hidden)
```swift
class HomeViewModel {
    let api: API
    
    init() {
        // HIDDEN: You don't know it needs an API until you read this line!
        self.api = ServiceLocator.shared.getService()
    }
}
```

### Contrast: Pure DI (Explicit)
```swift
class HomeViewModel {
    let api: API
    init(api: API) { self.api = api } // TRANSPARENT
}
```

## Why Service Locator is tempting but problematic:

1.  **Convenience**: It's easy to deep-dive into a locator instead of passing parameters through 5 levels of coordinators.
2.  **Testing Friction**: To test a class using a locator, you must first configure a global state (`ServiceLocator.shared`). This can lead to flaky tests if state leaks between test runs.
3.  **Encapsulation**: The class is no longer independent; it is hard-coupled to the `ServiceLocator` class itself.

## When is it acceptable?
In very large, legacy Objective-C codebases or when working with system-level services that are truly global and never change, a service locator can be used as a last resort. However, even then, a **DI Container** used at the **Composition Root** is usually a better choice.

## Comparison: Service Locator vs. DI

| Feature | Service Locator | Dependency Injection |
| :--- | :--- | :--- |
| **Object Role** | Active (Pulls dependencies) | Passive (Receives dependencies) |
| **Visibility** | Opaque (Hidden) | Transparent (Explicit) |
| **Coupling** | High (To the locator) | Low (To protocols) |
| **State** | Global (Hard to manage) | Local (Easy to manage) |

## Summary
The Service Locator pattern is the "easy path" to dependency management, but it leads to "dishonest" classes and brittle architectures. As a senior developer, you should strive for **Explicit Dependency Injection** because it results in code that is more predictable, easier to test, and fundamentally safer.
