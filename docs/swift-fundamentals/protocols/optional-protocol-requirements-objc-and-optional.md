---
id: 1195
---
﻿# Optional Protocol Requirements (`@objc` and `optional`)

In Swift, all requirements in a protocol are mandatory by default. However, there are two main ways to define optional requirements: using the `@objc` attribute or providing default implementations via protocol extensions.

## 1. Using `@objc` and `optional`

Optional requirements can be defined for protocols that are compatible with Objective-C. These protocols must be marked with the `@objc` attribute.

### Syntax
```swift
@objc protocol DataSource {
    @objc optional func increment(by amount: Int) -> Int
    @objc optional var fixedIncrement: Int { get }
}
```

### Key Considerations for `@objc` Optional Requirements
*   **Attribute Requirement**: The protocol and the optional methods must be marked with `@objc`.
*   **Class-Only**: `@objc` protocols can only be adopted by classes (reference types), not by structs or enums.
*   **Optional Chaining**: When calling an optional method, you must use optional chaining because the method might not be implemented.

```swift
class MyDataSource: DataSource {
    // increment(by:) is not implemented, so it is optional
}

let dataSource: DataSource = MyDataSource()
let result = dataSource.increment?(by: 10) // 'result' is Int?
```

## 2. Using Protocol Extensions (The "Swift Way")

The modern Swift approach to optional requirements is to provide a **default implementation** in a protocol extension. This allows any conforming type to either use the default behavior or provide its own custom implementation.

### Syntax
```swift
protocol NetworkObserver {
    func didStartRequest()
    func didFinishRequest() // Optional-like
}

extension NetworkObserver {
    func didFinishRequest() {
        print("Request finished (default implementation)")
    }
}
```

### Benefits of Protocol Extensions
*   **Universal Compatibility**: Works with structs, enums, and classes.
*   **No Objective-C Dependency**: Pure Swift implementation.
*   **Flexible Default Behavior**: You can provide significant logic as a default, reducing boilerplate for conformers.

## Comparing Both Approaches

| Feature | `@objc optional` | Protocol Extension |
| :--- | :--- | :--- |
| **Type Support** | Classes Only | Classes, Structs, Enums |
| **Implementation** | Missing from conformer | Provided in extension |
| **Calls** | Must use optional chaining (`?`) | Direct call (safe) |
| **Interop** | Required for Cocoa APIs | Pure Swift |

## Use Cases

### When to Use `@objc`
*   When interacting with legacy Objective-C codebases.
*   When working with certain Cocoa/Cocoa Touch frameworks (e.g., `UITableViewDelegate`, `UIScrollViewDelegate`).

### When to Use Protocol Extensions
*   In pure Swift projects.
*   When you want to provide a default "do nothing" behavior or a common default logic.
*   When your protocol should be adopted by value types.

## Example: A Modern Logger Protocol

```swift
protocol Logger {
    func log(_ message: String)
    func logError(_ error: Error) // This will have a default implementation
}

extension Logger {
    func logError(_ error: Error) {
        log("ERROR: \(error.localizedDescription)")
    }
}

struct ConsoleLogger: Logger {
    func log(_ message: String) {
        print(message)
    }
    // No need to implement logError unless custom behavior is needed
}
```

## Best Practices

*   **Prefer Protocol Extensions** for pure Swift code to maintain compatibility with value types and avoid optional chaining overhead.
*   **Use `@objc` sparingly**, only when necessary for system framework integration.
*   **Document default implementations** clearly so developers know what functionality is provided "for free."

---

> [!TIP]
> Protocols with default implementations in extensions are still "mandatory" in the sense that the requirement exists, but since a default is provided, the compiler is satisfied even if the conforming type doesn't implement it.

