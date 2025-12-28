---
id: 1148
---
# Optional Binding (`if let`, `guard let`)

**Optional Binding** is the standard, safe way to check if an optional contains a value and, if so, make that value available as a temporary constant or variable.

## 1. `if let`
The value is only available inside the braces of the `if` statement.

```swift
let username: String? = "swift_wizard"

if let name = username {
    print("Successfully logged in as \(name)")
} else {
    print("No username found.")
}
// 'name' is NOT available here
```

## 2. `guard let`
The value is available for the remainder of the function/scope after the `guard` statement.

```swift
func processUser(id: Int?) {
    guard let userId = id else {
        print("Id required")
        return
    }
    
    print("Processing user \(userId)")
    // 'userId' IS available here!
}
```

## 3. Shadowing
It is common practice (and idiomatic) to name the local constant the same as the optional variable. This is called **shadowing**.

```swift
if let username = username {
    // Inside here, 'username' refers to the non-optional string
}
```

## 4. Conditional Scoping
You can add extra conditions to your binding:

```swift
if let age = userAge, age >= 21 {
    print("Access granted")
}
```

## 5. Optional Binding Comparison

| Feature | `if let` | `guard let` |
| :--- | :--- | :--- |
| **Availability** | Inside block only | Remainder of scope |
| **Intent** | Conditional logic | Requirement / Precondition |
| **Logic Flow** | Nested | Flat |
| **Else Required?** | Optional | Always |

> [!IMPORTANT]
> Unwrapping using optional binding is the **"Golden Rule"** of Swift safety. It turns a potential runtime crash (from a missing value) into a compile-time logic check.
