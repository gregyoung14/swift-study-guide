---
id: 1162
---
# `try?` (Converting Throwing Functions to Optionals)

Swift's error handling model is designed to be expressive. However, sometimes you don't need the detailed error information—you just want the result if the operation succeeded, or `nil` if it failed. This is exactly what `try?` provides.

## 1. How it Works
When you use `try?`, the following happens:
1. The function is executed.
2. If it succeeds, the return value is wrapped in an optional.
3. If it throws an error, the result of the entire expression is `nil`.

```swift
func parse(json: String) throws -> [String: Any] { ... }

let result = try? parse(json: "{...}")
// result is [String: Any]?
```

## 2. Simplifying Code
The alternative to `try?` is a full `do-catch` block, which is much more verbose.

```swift
// VERBOSE:
var data: [String: Any]?
do {
    data = try parse(json: "...")
} catch {
    data = nil
}

// CONCISE:
let data = try? parse(json: "...")
```

## 3. Combining with Optionals
Since `try?` returns an optional, you can use all the standard optional tools:
- `if let result = try? function() { ... }`
- `let value = (try? function()) ?? defaultValue`

## 4. Handling Nested Optionals
If the throwing function itself returns an optional (e.g., `throws -> Int?`), then `try?` will return a nested optional (`Int??`). In this case, you might need two unwraps or a `flatMap`.

## 5. Use Cases
- **Optional Feature**: Loading a user's avatar from disk. If it fails, just show a placeholder.
- **Graceful Degradation**: Trying to read a cache file. If it fails, fetch from the network.

> [!TIP]
> Use `try?` when the *fact* that an error occurred is important, but the *reason* for the error is not.
