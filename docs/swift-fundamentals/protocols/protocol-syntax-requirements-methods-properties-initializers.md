---
id: 1202
---
﻿# Protocol Syntax (Requirements: Methods, Properties, Initializers)

A protocol defines a blueprint of requirements that a conforming type must implement. These requirements can include properties, methods, initializers, and even subscripts.

## 1. Property Requirements

A protocol can require a type to provide a property with a specific name and type. It specifies whether the property is gettable `{ get }` or gettable and settable `{ get set }`.

```swift
protocol MyProtocol {
    var mustBeSettable: Int { get set }
    var doesNotNeedToBeSettable: Int { get }
}
```

*   **Note**: Property requirements are always declared as `var`.
*   **Static Properties**: Use the `static` keyword for type properties.

## 2. Method Requirements

Protocols can require specific instance methods and type methods to be implemented.

```swift
protocol MethodProtocol {
    func random() -> Double
    static func reset()
    mutating func toggle() // Required for mutating value types
}
```

*   **Parameters**: Protocols define the method's name, return type, and parameters (including argument labels), but not the method's body.
*   **Default Values**: You **cannot** specify default values for method parameters within a protocol declaration.

## 3. Initializer Requirements

Protocols can require specific initializers to be implemented by conforming types.

```swift
protocol InitProtocol {
    init(token: String)
}
```

*   **Class Conformance**: When a class implements a protocol initializer, it must be marked with the `required` keyword to ensure all subclasses also implement it.
*   **Failable Initializers**: A protocol can define a failable initializer (`init?`), which can be satisfied by either a failable or non-failable initializer in the conforming type.

## 4. Subscript Requirements

Protocols can also require subscripts.

```swift
protocol Container {
    subscript(index: Int) -> Int { get set }
}
```

## Putting It All Together

```swift
protocol FullyFunctional {
    // Property
    var identifier: String { get }
    
    // Method
    func performAction()
    
    // Initializer
    init(id: String)
    
    // Type Method
    static func createNew() -> Self
}
```

## Best Practices

*   **Keep protocol requirements focused.** Avoid creating "fat" protocols with too many unrelated requirements.
*   **Use clear, descriptive names** for requirements to make the protocol's intent obvious.
*   **Consider using protocol extensions** to provide default implementations for some of these requirements, making the protocol easier to adopt.
*   **Use `Self`** in return types when you want the method to return an instance of the specific conforming type.

---

> [!NOTE]
> Protocols specify the *what* (the interface), while conforming types provide the *how* (the implementation).

