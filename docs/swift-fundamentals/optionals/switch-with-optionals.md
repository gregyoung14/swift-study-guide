---
id: 1160
---
# `switch` with Optionals

Using a `switch` statement with optionals is a safe and exhaustive way to handle both the presence (`.some`) and absence (`.none`) of a value. It is particularly useful when you need to handle multiple possible states of an optional beyond just "exists or doesn't exist."

## 1. Basic Optional Switch
```swift
let result: Int? = 10

switch result {
case .some(let value):
    print("Received value: \(value)")
case .none:
    print("No value received.")
}
```

## 2. Shorthand Syntax
Swift allows you to use `nil` and the `?` pattern for cleaner switch statements.

```swift
switch result {
case let value?:
    print("Value is \(value)")
case nil:
    print("Result was nil")
}
```

## 3. Matching Specific Optional Values
You can combine optional checking with specific value matching in a single case.

```swift
switch result {
case 0?:
    print("Result was exactly zero")
case let value? where value > 0:
    print("Positive result: \(value)")
case let value?:
    print("Negative result: \(value)")
case nil:
    print("Nothing to report")
}
```

## 4. Handling Multiple Optionals
You can switch over a tuple of optionals to handle their combined state matrix compactly.

```swift
let status: Int? = 200
let message: String? = "OK"

switch (status, message) {
case (let s?, let m?):
    print("Success: \(s) - \(m)")
case (let s?, nil):
    print("Status \(s) received without a message")
case (nil, let m?):
    print("Message '\(m)' received without a status")
case (nil, nil):
    print("Complete failure")
}
```

## 5. Why use Switch?
- **Exhaustiveness**: Ensures you haven't forgotten the `nil` case.
- **Complex Logic**: Cleaner than nested `if let ... else if let` chains.
- **Filtering**: Easily add `where` clauses to specific cases.

> [!TIP]
> For simple "exists or not" checks, `if let` is better. Use `switch` when your logic branches based on the **specific value** of the unwrapped data.
