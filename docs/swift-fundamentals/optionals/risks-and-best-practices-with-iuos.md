---
id: 1156
---
# Risks and Best Practices with Implicitly Unwrapped Optionals (IUOs)

Implicitly Unwrapped Optionals (`Type!`) are a powerful but dangerous feature in Swift. Because they behave like non-optional values but can still be `nil`, they are a common source of runtime crashes.

## 1. The Core Risk: Runtime Crashes
The biggest risk is that the compiler will not warn you when you use an IUO. If the variable is `nil` at the moment of access, your app will crash instantly.

```swift
var database: Database! = nil
database.save(data) // CRASH!
```

## 2. Best Practice: Avoiding IUOs in Models
Never use IUOs in your data models or business logic. If a value can be missing, use a standard optional (`?`).

```swift
// AVOID THIS
struct User {
    var id: String!
}

// PREFER THIS
struct User {
    var id: String 
}
```

## 3. Best Practice: Safe Initialization
If you use an IUO (e.g., for an `@IBOutlet`), ensure it is populated as early as possible. If it can't be populated during `init`, use `guard let` to verify its existence before use if you have any doubt.

## 4. When to Use IUOs
Only use IUOs when:
1. **Interoperating with Objective-C**: When the nullability of a return value is unknown to Swift.
2. **Interface Builder**: For outlets that are guaranteed to be connected.
3. **Broken Circular Dependencies**: When two objects must point to each other and neither can exist without the other.

## 5. Transitioning Away from IUOs
If you find yourself frequently checking if an IUO is `nil`, it should probably be a regular optional.

```swift
// If you do this:
if myIuo != nil { ... }

// You should just do this:
let myOptional: String? = ...
if let value = myOptional { ... }
```

> [!CAUTION]
> Treat every `!` in your code as a potential crash site. Aim for a codebase where `!` is used only in well-defined, system-level patterns like `@IBOutlet`.
