---
id: 36
---
# Popular DI Libraries (Swinject, Cleanse, etc.)

While manual Dependency Injection is often preferred, understanding the ecosystem of third-party DI libraries is important for working on large-scale modular projects.

## 1. Swinject (Runtime Container)
The most popular DI framework for iOS. It uses a registry-based approach where you register objects in a container and resolve them by type.

-   **Pros**: Very mature, great documentation, supports circular dependencies.
-   **Cons**: Runtime resolution is not type-safe (can crash), slight performance overhead.

```swift
let container = Container()
container.register(Persistence.self) { _ in CoreDataStack() }
// Resolve
let db = container.resolve(Persistence.self)!
```

## 2. Cleanse (Square's Framework)
Developed by Square, Cleanse is a "strongly typed" dependency injection framework inspired by Dagger (Android).

-   **Pros**: Catch errors at launch time instead of deep runtime, very architectural.
-   **Cons**: Extremely steep learning curve, verbose syntax.

## 3. Needle (Uber's Generator)
Needle is a "Generative" DI framework. It uses a build-time tool to analyze your code and generate the "wiring" logic.

-   **Pros**: **Absolute compile-time safety**, zero runtime lookup overhead, excellent for massive modular projects.
-   **Cons**: Requires a custom build step in Xcode, adds complexity to the build process.

## 4. Factory (Modern Swift)
A lightweight dependency injection library for Swift 5.1+, leveraging property wrappers and closures.

-   **Pros**: Very "Swifty," incredibly simple to set up, supports SwiftUI out of the box.
-   **Cons**: Still more "manual" than complex containers, relatively new.

```swift
extension Container {
    var apiService: Factory<APIService> { self { RealAPIService() }.singleton }
}

class ViewModel {
    @Injected(\.apiService) var service
}
```

## Side-by-Side Comparison

| Library | Type Safety | Resolution Time | Code Style | Best for |
| :--- | :--- | :--- | :--- | :--- |
| **Swinject** | Low | Runtime | Imperative | Most projects |
| **Needle** | High | Compile-time | Declarative | Large Scale / Modular |
| **Factory** | Medium | Runtime | Property Wrapper | SwiftUI / Micro-apps |
| **Cleanse** | High | Launch-time | Functional | Square/Enterprise |

## Which one to choose?
-   **Manual DI** is always the baseline.
-   If you need a framework, **Factory** is currently the best balance of simplicity and safety for modern Swift apps.
-   For "Uber-scale" projects with hundreds of modules, **Needle** is the only library that ensures the whole graph is correct at compile-time.

## Summary
The iOS DI landscape has shifted from runtime containers (Swinject) toward compile-time safe generators (Needle) and lightweight property wrapper systems (Factory). Choose the tool that matches your team's size and your app's complexity.
