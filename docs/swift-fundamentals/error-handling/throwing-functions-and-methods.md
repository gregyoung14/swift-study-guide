---
id: 953
---
﻿# Throwing Functions and Methods

To indicate that a function, method, or initializer can throw an error, you write the `throws` keyword in its declaration after its parameters.

## Declaration Syntax

A function marked with `throws` is called a **throwing function**. If the function specifies a return type, you write the `throws` keyword before the return arrow (`->`).

```swift
func canThrowErrors() throws -> String {
    // ...
}

func cannotThrowErrors() -> String {
    // ...
}
```

## Propagating Errors

Only throwing functions can propagate errors. Any error thrown inside a non-throwing function must be handled inside that function.

```swift
func fetchData() throws {
    let data = try loadFromNetwork() // loadFromNetwork is a throwing function
    process(data)
}
```

In the example above, if `loadFromNetwork()` throws an error, `fetchData()` will stop executing and propagate that same error to its own caller.

## Throwing Initializers

Initializers can also throw errors. This is useful when the initialization of an object depends on external resources that might not be available.

```swift
struct MyFile {
    let content: String
    
    init(path: String) throws {
        guard let data = FileManager.default.contents(atPath: path) else {
            throw FileError.notFound
        }
        self.content = String(decoding: data, as: UTF8.self)
    }
}
```

## Rethrowing Functions

A function can be marked with `rethrows` if it only throws an error when one of its function parameters throws an error. This is a common pattern in the Swift Standard Library (e.g., `map`, `filter`).

```swift
func perform(action: () throws -> Void) rethrows {
    try action()
}
```

## Best Practices

*   **Be explicit with naming**: Sometimes it's helpful to include "Throwing" or "CanFail" in the name if the context isn't obvious, though Swift's `try` keyword usually makes this clear enough.
*   **Documentation**: Always document the possible errors a function can throw using the `- Throws:` markup in your comments.
*   **Keep scopes small**: Don't put too much unrelated logic inside a single throwing function.

---

> [!IMPORTANT]
> When you call a throwing function, you **must** use the `try` keyword (or `try?` or `try!`) to acknowledge that the function can throw an error. This makes error-prone code paths explicitly visible.

