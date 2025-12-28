---
id: 1163
---
# `try!` (Forced Try)

`try!` is the error-handling equivalent of forced unwrapping (`!`). It allows you to call a throwing function without using a `do-catch` block, under the assumption that the function will never actually throw an error.

## 1. Syntax
```swift
let data = try! Data(contentsOf: localFileURL)
```

## 2. The Danger
If the function called with `try!` actually throws an error at runtime, **your application will crash**.

```swift
// This will crash if the file is missing or unreadable
let config = try! String(contentsOfFile: "missing_file.txt")
```

## 3. Appropriate Use Cases
`try!` should be avoided in most production code, but is acceptable when:
- **Immutable Bundle Resources**: Loading an icon or localized string file that you have verified exists in your app bundle during development.
- **Unit Testing**: When testing a function with inputs that you know are valid and should not throw.
- **Prototyping**: Skipping error handling while sketching out initial logic.

## 4. Comparison with `try?`
- **`try?`**: Safely returns `nil` on error.
- **`try!`**: Catastrophically crashes on error.

## 5. Best Practice
If an operation has any realistic chance of failing (e.g., network calls, database writes, user-generated file reads), **never use `try!`**. Use `do-catch` or `try?` instead.

| Scenario | Recommendation |
| :--- | :--- |
| Network Request | `do-catch` (need error status) |
| JSON Parsing | `try?` (if failure is handled by default) |
| App Asset Load | `try!` (if failure means the app is incomplete) |

> [!CAUTION]
> Treat `try!` as a programmer assertion: "If this line ever fails, my entire mental model of how the app works is wrong, and it is better to crash and find the bug than to continue in an undefined state."
