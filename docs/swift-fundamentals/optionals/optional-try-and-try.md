---
id: 1154
---
# Optional `try?` and `try!`

Swift's error handling interoperates neatly with Optionals. You can convert a "throwing" call into an optional value using `try?` or `try!`.

## 1. Using `try?`
`try?` attempts to execute a throwing function. 
- If the function succeeds, it returns the result wrapped in an optional.
- If the function throws an error, it returns `nil` (and the error is discarded).

```swift
func fetchData() throws -> Data { ... }

let data = try? fetchData()
// data is Data?
```

## 2. Chaining with Nil-Coalescing
`try?` is often combined with `??` to provide a fallback result for a failed operation.

```swift
let settings = (try? loadSettings()) ?? defaultSettings
```

## 3. Forced Try (`try!`)
`try!` is used when you are certain a function will not throw, or you want the app to crash if it does. It returns the unwrapped result.

```swift
let url = Bundle.main.url(forResource: "config", withExtension: "json")!
let data = try! Data(contentsOf: url)
// If this throws, the app CRASHES.
```

## 4. When to Use Which?
- **`try?`**: Use when you don't care *why* an operation failed, only *that* it failed, and you can handle a `nil` result.
- **`try!`**: Use only for resources that are guaranteed to be in your app bundle and whose absence indicates a catastrophic programmer error.
- **`do-catch`**: Use when you need to inspect the specific error to decide how to respond to the user.

## 5. Comparison
| Feature | `try?` | `try!` | `do-catch` |
| :--- | :--- | :--- | :--- |
| **Result Type** | Optional `T?` | Unwrapped `T` | Direct `T` |
| **OnError** | Returns `nil` | **Crashes** | Executes `catch` block |
| **Verbosity** | Low | Low | High |

> [!WARNING]
> Use `try!` with extreme caution. It is equivalent to forced unwrapping an optional and carries the same risk of runtime crashes.
