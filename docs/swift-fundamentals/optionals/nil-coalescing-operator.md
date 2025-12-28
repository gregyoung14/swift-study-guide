---
id: 1146
---
# Nil-Coalescing Operator (`??`)

The **Nil-Coalescing Operator** (`??`) is a shorthand for providing a default value when an optional is `nil`. It is one of the most common ways to resolve an optional into a non-optional value.

## 1. Basic Syntax
```swift
let optionalValue: Int? = nil
let resolved = optionalValue ?? 0
// resolved is Int, not Int?
```
The expression `a ?? b` is equivalent to:
`a != nil ? a! : b`

## 2. Short-Circuit Evaluation
The default value (the right side) is only evaluated if the optional (the left side) is actually `nil`. This is useful if the default value comes from a complex function.

```swift
func expensiveFallback() -> String {
    print("Calculating...")
    return "Default"
}

let name: String? = "John"
let currentName = name ?? expensiveFallback()
// "Calculating..." is never printed because name is not nil.
```

## 3. Chaining Nil-Coalescing
You can chain multiple operators to provide a priority-based list of fallbacks.

```swift
let remoteValue: String? = nil
let cachedValue: String? = "Cache"
let hardcodedValue = "Default"

let finalValue = remoteValue ?? cachedValue ?? hardcodedValue
// finalValue is "Cache"
```

## 4. Use Case: Dictionary Lookups
Dictionaries return an optional when you look up a key. `??` is perfect for providing defaults.

```swift
let scores = ["Math": 100]
let scienceScore = scores["Science"] ?? 0
```

## 5. Use Case: Optional Chaining
A common pattern is to use optional chaining followed by a nil-coalescing operator.

```swift
let userCount = organization?.departments?.first?.staffCount ?? 0
```

> [!IMPORTANT]
> The type of the value on the right must match the underlying type of the optional on the left. You cannot coalesce a `String?` with an `Int`.
