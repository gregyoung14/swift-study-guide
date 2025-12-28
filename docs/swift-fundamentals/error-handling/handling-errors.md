---
id: 935
---
﻿# Handling Errors

Swift provides three main keywords for handling errors: `try`, `try?`, and `try!`. Each serves a different purpose depending on how you want to respond to a potential failure.

## 1. Using `do-catch`

The `do-catch` statement allows you to handle errors by running a block of code and catching any errors that occur.

```swift
do {
    try performTask()
    print("Success!")
} catch let error as MyError {
    print("Caught a specific error: \(error)")
} catch {
    print("Caught an unknown error: \(error)")
}
```

## 2. Converting to Optionals (`try?`)

You can use `try?` to handle an error by converting it to an optional value. If an error is thrown, the result of the expression is `nil`.

```swift
let result = try? fetchData() // Returns optional data or nil if it failing
```

This is particularly useful when you don't care about the specific error and just want to know if the operation succeeded.

## 3. Disabling Propagation (`try!`)

You use `try!` when you know that a throwing function will **never** throw an error at runtime. If an error *is* thrown, the program will crash.

```swift
let photo = try! loadStandardIcon() // Only use if you are 100% sure it survives
```

## Comparison Table

| Method | Syntax | Return Type | Failure Outcome |
| :--- | :--- | :--- | :--- |
| **Do-Catch** | `do { try ... } catch { ... }` | Actual type | Executes `catch` block |
| **Optional Try** | `try? ...` | `Optional<Type>` | Returns `nil` |
| **Forced Try** | `try! ...` | Actual type | **Runtime Crash** |

## Best Practices

*   **Prefer `do-catch`** when you need to provide feedback to the user or recover from specific errors.
*   **Use `try?`** for simple operations where failure is expected and doesn't require complex handling (e.g., parsing an optional field).
*   **Avoid `try!`** in most production code. It should be reserved for cases where failure represents a logic error in your code (like missing bundled assets).

---

> [!CAUTION]
> Using `try!` is like using forced unwrapping (`!`). It's a "backdoor" that disables Swift's safety checks. Only use it when you can prove that failure is impossible.

