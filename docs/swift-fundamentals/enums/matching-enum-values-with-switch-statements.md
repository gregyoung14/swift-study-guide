---
id: 906
---
# Matching Enum Values with `switch` Statements

The most common and safest way to use an enum value is within a `switch` statement. Swift's `switch` is highly optimized for enums and provides several powerful features.

## 1. Basic Matching
A `switch` statement must cover every case of the enum.

```swift
enum Light {
    case on, off, dimmed(pct: Int)
}

let currentLight = Light.on

switch currentLight {
case .on:
    print("The light is bright.")
case .off:
    print("It is dark.")
case .dimmed(let pct):
    print("The light is at \(pct)%.")
}
```

## 2. Compound Cases
You can match multiple cases in a single branch by separating them with a comma.

```swift
switch currentLight {
case .on, .dimmed:
    print("There is some light.")
case .off:
    print("No light at all.")
}
```

## 3. Matching with Value Bindings
As seen in the first example, you can use `let` or `var` to bind associated values to local constants/variables for use within the case's body.

```swift
case .dimmed(let level) where level < 10:
    print("It's barely visible.")
```

## 4. The `where` Clause
You can refine your matching logic with a `where` clause to check for additional conditions.

```swift
enum Result {
    case success(score: Int)
    case failure(reason: String)
}

let myResult = Result.success(score: 85)

switch myResult {
case .success(let score) where score >= 90:
    print("Amazing! Score: \(score)")
case .success(let score):
    print("Passed with score: \(score)")
case .failure(let reason):
    print("Failed: \(reason)")
}
```

## 5. Handling Future Cases
If you are working with an enum that might get more cases in the future (from a library), use `@unknown default`.

```swift
switch someSystemEnum {
case .knownCase1:
    // ...
@unknown default:
    print("Handle unknown case gracefully")
}
```

> [!IMPORTANT]
> Swift's `switch` does not "fall through" by default. Once a case is matched and executed, the switch completes. Use the `fallthrough` keyword if you explicitly want to continue to the next case.
