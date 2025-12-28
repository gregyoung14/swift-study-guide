---
id: 902
---
# Implicitly Assigned Raw Values

In Swift, if you use integers or strings as raw values, you don't have to explicitly assign a raw value for every case. The compiler will automatically assign them for you.

## 1. Integer Raw Values
When integers are used for raw values, the implicit value for each case is one more than the previous case. If the first case doesn't have a value, its implicit value is `0`.

```swift
enum Planet: Int {
    case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
}
// venus is 2, earth is 3, mars is 4...
```

## 2. String Raw Values
When strings are used for raw values, the implicit value for each case is the text of that case's name.

```swift
enum CompassPoint: String {
    case north, south, east, west
}

let direction = CompassPoint.north.rawValue
// direction is "north"
```

## 3. Benefits of Implicit Assignment
- **Reduces Boilerplate**: You don't have to type `case north = "north"` repeatedly.
- **Maintainability**: If you reorder cases in an integer-based enum, the values will automatically shift (be careful if these values are persisted!).
- **Readability**: Keeps the enum declaration clean and focused on the cases themselves.

## 4. Mixing Explicit and Implicit
You can explicitly assign a value to any case, and the compiler will continue the sequence from there.

```swift
enum HTTPError: Int {
    case badRequest = 400
    case unauthorized // 401
    case paymentRequired // 402
    case forbidden = 403
}
```

> [!CAUTION]
> If you are saving raw values to a database or user defaults, avoid reordering integer-based enums, as it will change the values associated with your data.
