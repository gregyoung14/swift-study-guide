---
id: 1145
---
# Multiple Optional Bindings

You can unwrap multiple optionals in a single statement. This is much cleaner than nesting multiple `if let` blocks inside each other.

## 1. Using Commas
Use commas to separate multiple `let` (or `var`) bindings. All bindings must succeed for the block to execute.

```swift
let width: Double? = 5.0
let height: Double? = 10.0
let depth: Double? = 2.0

if let w = width, let h = height, let d = depth {
    let volume = w * h * d
    print("Volume is \(volume)")
} else {
    print("One or more dimensions are missing.")
}
```

## 2. Combining Bindings and Booleans
You can intersperse boolean conditions with your optional bindings. All parts must evaluate to `true` (and all optionals must have values).

```swift
if let w = width, w > 0, let h = height, h > 0 {
    print("Area is \(w * h)")
}
```

## 3. Scope of Variables
- Variables unwrapped in an `if let` are only available within the **if block**.
- Variables unwrapped in a `guard let` are available in the **rest of the scope** following the guard.

## 4. Dependency between Bindings
Later bindings can use variables created in earlier bindings of the same statement.

```swift
let json: [String: Any]? = ["id": 123]

if let data = json, let id = data["id"] as? Int {
    print("User ID: \(id)")
}
```

## 5. Comparison: Nested vs. Multi-Binding
```swift
// AVOID: "Pyramid of Doom"
if let a = optA {
    if let b = optB {
        if let c = optC {
            // Logic...
        }
    }
}

// PREFER: Multi-binding
if let a = optA, let b = optB, let c = optC {
    // Logic...
}
```

> [!TIP]
> If your `if let` statement becomes too long (e.g., more than 3-4 bindings), consider using a `guard` statement at the top of the function to maintain a "fail-fast" architectural pattern.
