---
id: 17
---
# Disadvantages (Mutable State, Less Obvious Dependencies)

While Dependency Injection (DI) usually improves code clarity, certain styles of DI (like Property Injection) can introduce **Mutable State** and make dependencies **Less Obvious**, leading to potential bugs and confusion.

## 1. The Risk of Mutable State
When using **Property Injection**, your dependencies must be declared as `var`. This means they can be changed after the object has been initialized.

### The Consequences:
-   **Race Conditions**: One thread might be using a dependency while another thread swaps it out.
-   **Inconsistent State**: An object might start a task with `ServiceA` and end it with `ServiceB`.
-   **Nil Crashes**: If a mandatory dependency is injected via a property, you either have to use Force Unwrapping (`!`) or check for nil every time you use it.

```swift
class ProfileViewController: UIViewController {
    var apiService: APIService? // Mutable and potentially nil!
    
    func viewDidAppear() {
        apiService!.fetch() // CRASH if not injected correctly
    }
}
```

## 2. Less Obvious Dependencies (Implicit Injection)
When using **DI Containers** or **Property Wrappers**, dependencies are often "magically" resolved.

### The Problem:
-   **Hard to Discover**: You can't see the class's requirements just by looking at the `init` method. You have to hunt through the file for `@Injected` annotations.
-   **Indirection**: It's harder to trace where a specific instance is coming from.
-   **Testing Friction**: You might need to set up a global container just to run a simple unit test, rather than just passing a mock to an initializer.

```swift
class HiddenDependenciesViewModel {
    @Injected var network: NetworkClient // Where does this come from?
    @Injected var database: Database     // Is it a singleton or a new instance?
    
    init() {} // Init tells us NOTHING about the requirements
}
```

## Comparison: Explicit vs. Implicit DI

| Feature | Explicit (Initializer) | Implicit (Property Wrapper / Container) |
| :--- | :--- | :--- |
| **Transparency** | High (Clear at a glance) | Low (Hidden in variables) |
| **Immutability** | Fully supported (`let`) | Usually not supported (`var`) |
| **Setup Cost** | Higher (Manual passing) | Lower (Auto-resolution) |
| **Testability** | Excellent | Good (But requires setup) |

## Best Practices to Mitigate These Issues

1.  **Favor Initializer Injection**: Use it for all mandatory dependencies to ensure immutability and visibility.
2.  **Private Setters**: If you must use property injection, use `private(set)` to prevent outside classes from changing the dependency after injection.
3.  **Assertion Checks**: Use `assert(dependency != nil)` in `viewDidLoad` to catch injection failures early in development.
4.  **Avoid Global State**: Even when using containers, try to keep the resolution local to the Composition Root.

## Summary
The "magical" convenience of property wrappers and containers can be tempting, but it comes at the cost of transparency and thread-safety. A Senior Engineer knows when to accept these trade-offs and when to stick to the "boring" but safe path of explicit constructor injection.
