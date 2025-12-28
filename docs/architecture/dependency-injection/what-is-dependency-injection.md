---
id: 44
---
# What is Dependency Injection? (Executive Summary)

Dependency Injection (DI) is a structural design pattern that facilitates **Inversion of Control**. It is the standard approach for managing object creation and dependencies in high-quality professional iOS applications.

## At a Glance
Instead of an object being responsible for creating its own dependencies, those dependencies are **injected** into it (provided from the outside).

## The Core Elements

1.  **The Client**: The class that needs work done.
2.  **The Service**: The dependency that does the work.
3.  **The Interface (Protocol)**: The contract that describes the work.
4.  **The Injector**: The component that connects the Client to the Service.

## Why it's the Industry Standard

### 1. Radical Testability
By injecting protocols, we can replace real dependencies with mocks, allowing for 100% test coverage of business logic.

### 2. High Maintainability
Changes to the network layer, database, or analytics don't "leak" into the UI or Business logic.

### 3. Modular Architecture
DI is required for breaking large apps into separate Swift Packages or Frameworks.

## The Most Common Style: Initializer Injection
```swift
class ReportViewModel {
    private let api: APIProtocol
    
    // Dependencies are explicitly declared and mandatory
    init(api: APIProtocol) {
        self.api = api
    }
}
```

## Comparison: The Before and After

| Feature | Legacy Approach (Singletons) | Modern Approach (DI) |
| :--- | :--- | :--- |
| **Philosophy** | "Pull" from global scope | "Push" from parent/injector |
| **Visibility** | Hidden | Explicit |
| **Testing** | Hard / Integrated only | Easy / Isolated unit tests |
| **Coupling** | Tight | Loose |

## summary
Dependency Injection is not about making your code more complex; it's about making it **honest**. By externalizing dependencies, you ensure your app is built from small, focused, and testable components that can evolve independently over time.
