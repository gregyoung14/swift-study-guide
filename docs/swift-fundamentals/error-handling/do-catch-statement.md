---
id: 926
---
﻿# `do-catch` Statement

The `do-catch` statement is the primary way to handle errors in Swift. It allows you to execute a block of code and catch any errors that are thrown, enabling graceful recovery.

## Basic Structure

The `do` block contains the code that might throw an error. The `catch` blocks follow, specifying which errors they handle.

```swift
do {
    try vendingMachine.vend(itemNamed: "Chips")
    print("Enjoy your chips!")
} catch {
    print("An error occurred: \(error)")
}
```

In the example above, if an error is thrown, the catch block captures it in a local constant named `error`.

## Specific Catch Clauses

You can use multiple `catch` blocks to handle different types of errors specifically.

```swift
do {
    try vendingMachine.vend(itemNamed: "Candy Bar")
} catch VendingMachineError.invalidSelection {
    print("That item doesn't exist.")
} catch VendingMachineError.outOfStock {
    print("We're out of that item.")
} catch VendingMachineError.insufficientFunds(let coinsNeeded) {
    print("You need \(coinsNeeded) more coins.")
} catch {
    print("Unknown error: \(error)")
}
```

## Pattern Matching in `catch`

Catch clauses can use the same pattern matching capabilities as `switch` statements.

```swift
do {
    try performNetworkRequest()
} catch NetworkError.timeout(let seconds) where seconds > 60 {
    print("Long timeout: \(seconds)s. Check your connection.")
} catch NetworkError.serverError(let code) where (500...599).contains(code) {
    print("Server-side error: \(code)")
} catch {
    print("Generic error: \(error)")
}
```

## Scoped catch

If a catch clause doesn't specify a pattern, it matches any error and binds the error to a local constant named `error`.

```swift
catch {
    // 'error' is available here
}
```

## Best Practices

*   **Be specific**: Catch specific error types first, then use a generic catch-all at the end if necessary.
*   **Don't ignore errors**: An empty `catch {}` block is usually a sign of poor error handling. At the very least, log the error.
*   **Keep it clean**: If your `do` block becomes too large or complex, consider breaking it into smaller throwing functions.

---

> [!NOTE]
> Swift's `catch` blocks are exhaustive. If you don't handle every possible error from a throwing function, you must ensure the surrounding function is also marked with `throws`.

