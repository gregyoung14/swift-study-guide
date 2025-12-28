---
id: 939
---
﻿# Introduction to Error Handling

Error handling is the process of responding to and recovering from error conditions in your program. Swift provides first-class support for throwing, catching, propagating, and manipulating recoverable errors at runtime.

## The Core Philosophy

Unlike some languages that use exceptions for everything (including logic flow), Swift's error handling is designed for **recoverable errors**. This means errors that a program can reasonably handle, such as:
*   A file not being found.
*   A network connection being lost.
*   Invalid user input.

For developer mistakes (like out-of-bounds array access), Swift uses **assertions** and **preconditions** which terminate the program, rather than the error handling system.

## The Four Ways to Handle Errors

When a function throws an error, you have four ways to deal with it:

1.  **Propagate the error** from a function to the code that calls that function.
2.  **Handle the error** using a `do-catch` statement.
3.  **Convert the error to an optional** value using `try?`.
4.  **Assert that the error will not occur** using `try!`.

## Basic Syntax Preview

You mark a function that can throw an error with the `throws` keyword. When calling it, you must use the `try` keyword.

```swift
func checkStatus() throws {
    // ... logic that might fail ...
}

do {
    try checkStatus()
} catch {
    print("An error occurred: \(error)")
}
```

## Comparisons with Other Languages

| Feature | Swift | Java/C++/Python |
| :--- | :--- | :--- |
| **Keyword** | `throws` / `try` | `throws` / `throw` / `try-catch` |
| **Type Safety** | Errors are often Enums | Errors are usually Classes |
| **Logic Flow** | Not recommended for flow | Sometimes used for flow |
| **Performance** | High (comparable to return) | Can be expensive (stack unwinding) |

---

> [!NOTE]
> Swift's error handling is often called "checked exceptions" in other languages, but it doesn't require you to declare exactly *which* errors a function throws, only that it *can* throw.

