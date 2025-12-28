---
id: 895
---
# Defining Enums with Raw Values

**Raw Values** are pre-populated values of a specific type that are assigned to enum cases. Unlike Associated Values, Raw Values must be the same type for all cases and are literal values.

## 1. Basic Syntax
You specify the raw value type after the enum name.

```swift
enum ASCIIControlCharacter: Character {
    case tab = "\t"
    case lineFeed = "\n"
    case carriageReturn = "\r"
}
```

## 2. Implicitly Assigned Raw Values
When you use integers or strings as raw values, Swift can often assign them automatically.

### Integer Raw Values
By default, the first case is `0`, and each subsequent case is incremented by 1.

```swift
enum Planet: Int {
    case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
}
// venus is 2, earth is 3, etc.
```

### String Raw Values
The implicit raw value for each case is the string name of the case itself.

```swift
enum CompassPoint: String {
    case north, south, east, west
}
// CompassPoint.north.rawValue == "north"
```

## 3. Initializing from a Raw Value
If you define an enum with a raw value type, it automatically receives an initializer that takes a value of that type and returns either an enum case or `nil`.

```swift
let possiblePlanet = Planet(rawValue: 7)
// possiblePlanet is of type Planet?, and its value is .uranus

let unknownPlanet = Planet(rawValue: 11)
// unknownPlanet is nil
```

## 4. Comparison Table: Raw vs. Associated Values

| Feature | Raw Values | Associated Values |
| :--- | :--- | :--- |
| **Data Type** | Pre-defined (Int, String, etc.) | Any type, unique per case |
| **Timing** | Defined at compile-time | Set at runtime when creating instance |
| **Exclusivity** | Fixed for each case | Can change per instance |
| **Number** | Exactly one per case | Multiple values allowed |

> [!WARNING]
> Raw values must be **unique** within the enum declaration. You cannot have two cases with the same raw value.
