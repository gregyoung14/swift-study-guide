---
id: 896
---
# Enum as a Data Type (Methods, Properties, Initializers)

In Swift, enumerations are first-class types. They share many features traditionally supported only by classes and structs, such as computed properties, methods, and initializers.

## 1. Computed Properties
Enums cannot have stored properties (except for their raw value), but they can have **computed properties**.

```swift
enum Device {
    case phone, tablet, watch, laptop

    var screenInches: Double {
        switch self {
        case .phone:  return 6.1
        case .tablet: return 11.0
        case .watch:  return 1.5
        case .laptop: return 14.2
        }
    }
}
```

## 2. Instance Methods
Enums can define methods that provide functionality relevant to the values.

```swift
enum TriStateSwitch {
    case off, low, high

    mutating func next() {
        switch self {
        case .off:  self = .low
        case .low:  self = .high
        case .high: self = .off
        }
    }
}

var ovenLight = TriStateSwitch.low
ovenLight.next() // ovenLight is now .high
```

## 3. Static Methods
You can also define static methods to provide utility functions related to the type.

```swift
enum Theme {
    case light, dark, system

    static func defaultTheme() -> Theme {
        return .system
    }
}
```

## 4. Custom Initializers
You can provide custom initializers to set up an enum instance from different input types.

```swift
enum Temperature {
    case boiling, freezing, normal

    init(celsius: Double) {
        if celsius >= 100 {
            self = .boiling
        } else if celsius <= 0 {
            self = .freezing
        } else {
            self = .normal
        }
    }
}

let currentTemp = Temperature(celsius: 25.0) // .normal
```

## 5. Extensions
Like classes and structs, enums can be extended to add new functionality or conform to protocols.

```swift
extension Device: CustomStringConvertible {
    var description: String {
        return "This is a \(self) device."
    }
}
```

> [!NOTE]
> Even though enums can have methods and properties, they remain **Value Types**. When you modify them inside a method, you must use the `mutating` keyword.
