---
id: 1002
---
﻿# `Any` (Any Type) and `AnyObject` (Any Class Type)

Swift provides two special type aliases for working with non-specific types: `Any` and `AnyObject`. Knowing the difference between them is essential for writing safe and idiomatic Swift code.

## 1. `Any` (Any Type)

`Any` is the most general type in Swift. It can represent an instance of **any type at all**, including:
*   Standard library types (`Int`, `String`, `Array`, etc.)
*   Custom structs, enums, and classes
*   Function types
*   Optional types
*   Tuples

### Example
```swift
var things: [Any] = []

things.append(0)
things.append(3.14159)
things.append("hello")
things.append((3.0, 5.0))
things.append({ (name: String) -> String in "Hello, \(name)" })
```

## 2. `AnyObject` (Any Class Type)

`AnyObject` is more specific than `Any`. It can represent an instance of **any class type**. It is essentially the protocol that all classes implicitly conform to.

### Characteristics
*   **Reference Types Only**: You cannot store a `struct` or `enum` in an `AnyObject` type.
*   **ARC Management**: `AnyObject` is managed by Automatic Reference Counting (ARC).
*   **Objective-C Interop**: `AnyObject` is used to bridge with Objective-C's `id` type.

### Example
```swift
class MyClass {}
struct MyStruct {}

let classInstance: AnyObject = MyClass()
// let structInstance: AnyObject = MyStruct() // Compile-time error
```

## Notable Nuances

### `AnyObject` and Property Access
In certain contexts (primarily when dealing with Objective-C APIs), Swift allows you to call any `@objc` method or property on an `AnyObject` instance without casting. This returns an optional.

```swift
import Foundation

let myObject: AnyObject = NSArray(object: "Hello")
let count = myObject.count // This works and returns an optional Int?
```

### `Any` and Optionals
A common pitfall is that `Any` can hold optionals. If you pass an optional to a parameter of type `Any`, Swift will wrap the optional in the `Any` box, which can lead to unexpected behavior if you don't check for `nil`.

```swift
let optionalValue: String? = nil
let wrapped: Any = optionalValue
print(wrapped) // Prints: "nil" (but it's of type Any!)
```

## Comparisons

| Feature | `Any` | `AnyObject` |
| :--- | :--- | :--- |
| **Capacity** | Values, Classes, Functions, etc. | Classes (Reference types) only |
| **Implicit Conformance** | All types | All class types |
| **Common Use Case** | Legacy APIs, raw data parsing | Casting from Objective-C `id`, weak delegate pointers |
| **Memory Allocation** | Stack or Heap (via boxing) | Heap (Reference) |

## Best Practices

*   **Avoid `[Any]` collections** whenever possible. Use protocols or enums with associated values to maintain better type safety.
*   **Use `AnyObject` for protocol requirements** that must only be adopted by classes.
*   **Explicitly cast away from `Any`** as early as possible to regain type safety.

---

> [!WARNING]
> Excessive use of `Any` and `AnyObject` can make your code harder to understand and maintain, as it hides the true shape of your data and disables many compiler safety checks.

