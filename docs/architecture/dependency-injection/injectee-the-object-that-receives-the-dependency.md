---
id: 27
---
# The Injectee (The object that receives the dependency)

In the vocabulary of Dependency Injection, the **Injectee** (also known as the **Client**) is the object that requires a dependency to perform its work. Understanding the role of the Injectee is crucial for maintaining the **Single Responsibility Principle**.

## The Passive Nature of the Injectee
The defining characteristic of a good Injectee is that it is **passive**. It does not know *how* its dependencies are created, *where* they come from, or *which* specific implementation it is using.

### The "Naughty" Injectee (Hard-coded)
This class is "active" because it creates its own tools. It's now harder to test and reuse.
```swift
class ReportGenerator {
    let printer = HPPrinter() // Active role: choosing the implementation
}
```

### The "Well-Behaved" Injectee (Passive)
This class is "passive." It just says "I need a Printer."
```swift
class ReportGenerator {
    let printer: PrinterProtocol // Passive role: receiving the implementation
    init(printer: PrinterProtocol) { self.printer = printer }
}
```

## Roles and Responsibilities of an Injectee

1.  **Declaring Requirements**: Clearly stating what it needs via an initializer or properties.
2.  **Using Abstractions**: Interacting with dependencies only through protocols, not concrete classes.
3.  **Core Logic**: Focusing 100% on its own business purpose, not on infrastructure.

## Identifying Injectees in your App

Almost any logic-heavy class in your app should be an Injectee:
-   **ViewModels**: Receiving services and data providers.
-   **Services**: Receiving network clients and database managers.
-   **Coordinators**: Receiving factories or parent storage.

## The Injectee's Perspective
From the perspective of a `UserViewModel`, the world looks like this:
```mermaid
graph LR
    I[Injectee: ViewModel] -->|Requests| P1[Protocol: AuthService]
    I -->|Requests| P2[Protocol: Analytics]
    Note right of I: "I don't care WHO provides these, <br/>as long as they follow the contract."
```

## Key Benefits for the Injectee
-   **Isolation**: Can be tested without its dependencies.
-   **Portability**: Can be moved to a different project or platform easily.
-   **Simplicity**: The code is cleaner because it's not cluttered with setup logic.

## Summary
The Injectee should be as "ignorant" as possible about its surroundings. By keeping your clients passive and focused, you ensure that your application's business logic remains decoupled from the infrastructure that supports it.
