---
id: 1194
---
﻿# Opaque Types (`some Protocol`)

Opaque types, introduced in Swift 5.1, allow a function to return a specific, concrete type while hiding that type's identity from the caller. Instead of specifying the exact return type, you use the `some` keyword followed by a protocol.

## What is an Opaque Type?

When a function returns an opaque type, it is essentially saying: "I will return *some* type that conforms to this protocol, but I'm not going to tell you exactly which one it is."

Crucially, while the type's identity is hidden from the caller, it is **known to the compiler**. This allows the function to remain performant and maintain type identity throughout its lifecycle.

### Basic Syntax
```swift
func makeWidget() -> some Widget {
    return CircularWidget() // The compiler knows this is a CircularWidget
}
```

## Opaque Types vs. Existential Types

It's common to confuse Opaque Types (`some Protocol`) with Existential Types (`any Protocol`).

| Feature | Opaque Type (`some P`) | Existential Type (`any P`) |
| :--- | :--- | :--- |
| **Type Identity** | Preserved (Static) | Lost (Dynamic) |
| **Performance** | High (Direct dispatch) | Lower (Indirect dispatch/boxing) |
| **Return Value** | Must be a single consistent type | Can be different types at runtime |
| **Usage** | Return types, property types (since Swift 5.7) | Parameters, Variables, Collections |

### Example Comparison
```swift
// Opaque Type: Must return the SAME type every time
func getSomeShape() -> some Shape {
    return Circle() 
    // error: return Square() // Cannot return a different type here
}

// Existential Type: Can return DIFFERENT types
func getAnyShape(isCircle: Bool) -> any Shape {
    if isCircle {
        return Circle()
    } else {
        return Square()
    }
}
```

## Why Use Opaque Types?

1.  **API Abstraction**: You can hide internal implementation details (e.g., a specific internal struct) while still providing a type that conforms to a public protocol.
2.  **SwiftUI Foundations**: Opaque types are the backbone of SwiftUI. Every view's `body` property is of type `some View`. This allows the complex tree of nested views to be treated as a single return type without exposing the exact, deeply nested generic type.
3.  **Performance**: Since the compiler knows the underlying type, it can optimize the code just as if you had returned the concrete type directly.
4.  **Generic Requirements**: Unlike existential types, opaque types can be used with protocols that have associated types or `Self` requirements.

## Examples in Action

### Hiding Complex Types
```swift
protocol Shape {
    func draw() -> String
}

struct JoinedShape<T: Shape, U: Shape>: Shape {
    var top: T
    var bottom: U
    func draw() -> String { return "\(top.draw())\n\(bottom.draw())" }
}

// Without 'some', the return type would be JoinedShape<Circle, Square>
func makeComplexShape() -> some Shape {
    return JoinedShape(top: Circle(), bottom: Square())
}
```

## Best Practices

*   **Prefer `some` over `any` when possible.** If you know a function will always return the same type, use `some` for better performance and type safety.
*   **Use `some` for return types in internal modules** to avoid exposing private implementation details.
*   **Remember that `some` is "reverse generics".** Instead of the caller deciding the type, the function implementation decides the type.

---

> [!IMPORTANT]
> A function returning `some Protocol` must return a single concrete type across all possible execution paths. You cannot return a `Circle` in one branch and a `Square` in another.

