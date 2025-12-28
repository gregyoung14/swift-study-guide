---
id: 912
---
# Raw Values in Enums

**Raw Values** are literal values associated with each case of an enumeration. They are defined at compile-time and remain constant for the lifetime of the application.

## 1. Supported Types
Raw values can be strings, characters, or any of the integer or floating-point number types. All cases in the enum must have a raw value of the same type.

```swift
enum Grade: Character {
    case a = "A"
    case b = "B"
    case c = "C"
}
```

## 2. Defining and Accessing
To define an enum with raw values, specify the type in the declaration. Access the value using the `.rawValue` property.

```swift
enum HTTPStatus: Int {
    case ok = 200
    case notFound = 404
}

let code = HTTPStatus.ok.rawValue // 200
```

## 3. Immutability
Raw values are immutable. Once defined in the source code, they cannot be changed at runtime.

## 4. Uniqueness Requirement
Each raw value must be unique within its enumeration declaration. You cannot have two cases that map to the same raw value.

```swift
enum DuplicateError: Int {
    case first = 1
    // case second = 1 // Error: Raw value for 'second' is not unique
}
```

## 5. Summary Table
| Feature | Description |
| :--- | :--- |
| **Type** | Single type for all cases |
| **Value** | Literal value set in code |
| **Access** | Via `.rawValue` property |
| **Mutability** | Constant (Immutability) |

> [!NOTE]
> Raw values are different from associated values. Raw values are like "labels" attached to the cases, while associated values are "containers" for data.
