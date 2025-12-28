---
id: 944
---
﻿# Representing Errors

In Swift, errors are represented by values of types that conform to the `Error` protocol. This empty protocol indicates that a type can be used for error handling.

## The `Error` Protocol

The `Error` protocol itself doesn't have any requirements. Conforming to it is a way of telling the compiler (and other developers) that this type is intended to represent an error condition.

```swift
enum VendingMachineError: Error {
    case invalidSelection
    case insufficientFunds(coinsNeeded: Int)
    case outOfStock
}
```

## Why Use Enumerations?

Enums are the most common way to represent errors in Swift because:
1.  **Grouping**: They allow you to group related error conditions together.
2.  **Associated Values**: They can carry additional context about the error (e.g., how many coins are missing).
3.  **Exhaustiveness**: When handling errors with a `switch` statement, the compiler ensures you've considered every possible error case.

### Example with Associated Values
```swift
enum NetworkError: Error {
    case timeout(seconds: Int)
    case serverError(statusCode: Int)
    case unauthorized
}

func fetchData() throws {
    throw NetworkError.serverError(statusCode: 404)
}
```

## Other Types as Errors

While Enums are the default choice, any type can conform to the `Error` protocol, including `structs` and `classes`.

```swift
struct FileError: Error {
    let path: String
    let reason: String
}

throw FileError(path: "/usr/bin", reason: "Permission denied")
```

## Key Benefits

*   **Type Safety**: Errors are part of the type system, not just random integers or strings.
*   **Self-Documenting**: Looking at the error enum provides a clear overview of what can go wrong in a particular module.
*   **Compile-Time Verification**: The compiler helps ensure that throwing functions are called with appropriate error management.

---

> [!TIP]
> Use `enums` for a fixed set of error conditions and `structs` when you need to store significant amounts of metadata about an error.

