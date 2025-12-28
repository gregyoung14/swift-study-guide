---
id: 1136
---
# Accessing Properties, Methods, and Subscripts Through Optionals

When working with optionals, you often need to access the members of the underlying type. Swift provides **Optional Chaining** to do this safely and concisely.

## 1. Optional Chaining (`?.`)
Optional chaining allows you to call properties, methods, and subscripts on an optional that might be `nil`. If the optional is `nil`, the entire expression returns `nil`.

```swift
struct Residence {
    var numberOfRooms = 1
}

struct Person {
    var residence: Residence?
}

let john = Person()

// This would crash if residence was nil and we used !
// Instead, roomCount is of type Int?
let roomCount = john.residence?.numberOfRooms

if let count = roomCount {
    print("John has \(count) rooms.")
} else {
    print("John has no residence.")
}
```

## 2. Calling Methods Safely
You can call methods using the same syntax. If the method returns a value, that value will be wrapped in an optional. If the method returns `Void`, the expression returns `Void?`.

```swift
class Order {
    func cancel() { print("Order cancelled") }
}

var currentOrder: Order? = Order()
currentOrder?.cancel() // Prints "Order cancelled"

currentOrder = nil
currentOrder?.cancel() // Silently does nothing
```

## 3. Accessing Subscripts
To access a subscript on an optional value, place the `?` before the opening bracket.

```swift
var scores: [String: [Int]]? = ["Math": [90, 85, 95]]

// Accessing the first score of "Math"
let firstMathScore = scores?["Math"]?[0]
// firstMathScore is Int?
```

## 4. Deep Chaining
You can chain multiple levels of optionals. If any part of the chain is `nil`, the whole chain fails.

```swift
let city = user?.profile?.address?.city
// If user OR profile OR address is nil, city is nil.
```

> [!TIP]
> Optional chaining is almost always preferred over forced unwrapping (`!`) because it turns a potential crash into a manageable `nil` result.
