---
id: 903
---
# Initializers in Enums

Swift enums can have custom initializers to provide more ways to create an instance beyond just choosing a case.

## 1. Basic Initializer
You can use an `init` method to perform logic and then assign a case to `self`.

```swift
enum Device {
    case phone, tablet, watch

    init(screenSize: Double) {
        if screenSize < 2.0 {
            self = .watch
        } else if screenSize < 7.0 {
            self = .phone
        } else {
            self = .tablet
        }
    }
}

let myDevice = Device(screenSize: 6.1) // .phone
```

## 2. Failable Initializers
Often, an initializer might fail if the input is invalid. You use `init?` to return an optional enum.

```swift
enum Intensity {
    case low, medium, high

    init?(string: String) {
        switch string.lowercased() {
        case "l", "low":    self = .low
        case "m", "medium": self = .medium
        case "h", "high":   self = .high
        default:           return nil
        }
    }
}

let level = Intensity(string: "High") // .high
let invalid = Intensity(string: "None") // nil
```

## 3. Delegating Initializers
Enums can have multiple initializers, and they can call each other using `self.init(...)`.

```swift
enum Color {
    case red, green, blue

    init(hex: Int) {
        // Complex hex logic...
        self = .red
    }

    init(name: String) {
        if name == "apple" {
            self.init(hex: 0xFF0000)
        } else {
            self = .green
        }
    }
}
```

> [!NOTE]
> Regardless of the logic inside the initializer, you must eventually assign a value to `self` before the initializer finishes.
