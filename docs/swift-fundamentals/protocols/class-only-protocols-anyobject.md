---
id: 1175
---
# Class-Only Protocols (`: AnyObject`)

Sometimes you want to define a protocol that can **only** be adopted by classes, and not by structs or enums. 

## 1. Syntax
To define a class-only protocol, add `AnyObject` to the protocol's inheritance list.

```swift
protocol CameraDelegate: AnyObject {
    func didCaptureImage(_ image: UIImage)
}
```

## 2. Why Use Class-Only Protocols?

### Reference Semantics
If the protocol's requirements assume that the conforming type is a reference type (e.g., identity matters), then it should be class-only.

### Weak References (The primary reason)
In the Delegate pattern, you often want to hold a `weak` reference to the delegate to avoid **Retain Cycles**. You can only use the `weak` keyword on reference types. If the protocol is not marked `AnyObject`, the compiler won't allow `weak`.

```swift
class CameraManager {
    weak var delegate: CameraDelegate? // This works!
}
```

### Mutating Expectations
If a protocol method changes the state of the object, classes (reference types) don't need the `mutating` keyword, whereas structs (value types) do. A class-only protocol simplifies method signatures in these cases.

## 3. Adoption Error
If you try to make a struct conform to a class-only protocol, you will get a compile-time error.

```swift
// Error: Non-class type 'MyStruct' cannot conform to class-protocol 'CameraDelegate'
struct MyStruct: CameraDelegate { ... } 
```

## 4. Comparison
| Property | Regular Protocol | Class-Only Protocol |
| :--- | :--- | :--- |
| **Adoptable by** | Class, Struct, Enum | **Class only** |
| **Weak Reference** | Not Allowed | **Allowed** |
| **Indirection** | Tagged Pointer | Direct Pointer |

> [!TIP]
> If your protocol ends with the word "Delegate", it should almost certainly be an `AnyObject` protocol.
