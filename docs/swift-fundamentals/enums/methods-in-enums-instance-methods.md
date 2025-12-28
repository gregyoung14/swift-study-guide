---
id: 907
---
# Methods in Enums (Instance Methods)

Enums in Swift can define **Instance Methods** to provide specific functionality for each value. This makes enums feel more like objects while maintaining the safety of value types.

## 1. Simple Instance Method
An instance method can use `self` to determine which logic to execute based on the current case.

```swift
enum TrafficLight {
    case red, yellow, green

    func message() -> String {
        switch self {
        case .red:    return "Stop"
        case .yellow: return "Caution"
        case .green:  return "Go"
        }
    }
}

let light = TrafficLight.red
print(light.message()) // "Stop"
```

## 2. Mutating Methods
By default, you cannot change the value of `self` inside an instance method. To do so, you must mark the method as `mutating`.

```swift
enum Switch {
    case off, on

    mutating func toggle() {
        if self == .off {
            self = .on
        } else {
            self = .off
        }
    }
}

var bedroomSwitch = Switch.off
bedroomSwitch.toggle() // bedroomSwitch is now .on
```

## 3. Using Associated Values in Methods
Instance methods can also interact with the associated values of the current case.

```swift
enum Account {
    case savings(balance: Double)
    case checking(balance: Double)

    mutating func deposit(amount: Double) {
        switch self {
        case .savings(let balance):
            self = .savings(balance: balance + amount)
        case .checking(let balance):
            self = .checking(balance: balance + amount)
        }
    }
}
```

## 4. Internal State Management
Methods allow enums to act as state machines, where the internal value changes according to defined rules.

> [!TIP]
> If a method doesn't need to change the enum value, keep it non-mutating. This ensures that callers don't accidentally modify their instances.
