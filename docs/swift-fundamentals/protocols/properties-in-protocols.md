---
id: 1196
---
﻿# Properties in Protocols

Protocols can require specific properties to be implemented by any type that conforms to them. A protocol doesn't specify whether a property should be a stored property or a computed property—it only specifies the required name, type, and whether the property must be readable or readable and writable.

## Defining Property Requirements

Property requirements are always declared as variable properties, prefixed with the `var` keyword. Readable and writable properties are indicated by writing `{ get set }` after their type declaration, and gettable properties are indicated by writing `{ get }`.

### Get-Only Properties
A protocol can require a property to be at least gettable. The conforming type can implement this as a constant (`let`), a stored variable (`var`), or a computed property.

```swift
protocol FullyNamed {
    var fullName: String { get }
}
```

### Get and Set Properties
If a protocol requires a property to be gettable and settable, it **must** be implemented as a variable (`var`) stored property or a computed property with both a getter and a setter. It cannot be a constant (`let`).

```swift
protocol Adjustable {
    var value: Double { get set }
}
```

## Type Property Requirements

Protocols can also define type property requirements (static properties) by prefixing the property declaration with the `static` keyword. 

```swift
protocol IdentifiableType {
    static var typeIdentifier: String { get }
}
```

When a class conforms to a protocol with a static property, it can use the `static` or `class` keyword. `class` allows the property to be overridden by subclasses.

## Examples of Conformance

### Conforming with Stored Properties
```swift
struct Person: FullyNamed {
    let fullName: String // Satisfies { get }
}

struct Slider: Adjustable {
    var value: Double = 0.0 // Satisfies { get set }
}
```

### Conforming with Computed Properties
```swift
struct Employee: FullyNamed {
    var firstName: String
    var lastName: String
    
    var fullName: String { // Satisfies { get } via computation
        return "\(firstName) \(lastName)"
    }
}
```

## Why Property Requirements Matter

1.  **Interface Consistency**: Ensures that different types provide the same data interface, allowing them to be treated interchangeably (e.g., in a collection of `FullyNamed` objects).
2.  **Data Flow**: Declaring `{ get set }` explicitly signals that an object's state can be modified through that protocol, which is crucial for data binding and state management.
3.  **Encapsulation**: Using `{ get }` in a protocol allows you to expose read-only data from an object that might internally use a private mutable property.

## Best Practices

*   **Be restrictive with `{ get set }`.** If a property doesn't need to be modified by the protocol consumer, only require `{ get }`. This provides more flexibility for the implementation.
*   **Use static properties for constants or metadata** that apply to the type as a whole rather than specific instances.
*   **Avoid complex computed logic in protocol properties.** Keep them as simple data accessors where possible, and use methods for complex operations.

---

> [!IMPORTANT]
> A protocol property requirement cannot have a default value. Initial values must be provided by the conforming types.

