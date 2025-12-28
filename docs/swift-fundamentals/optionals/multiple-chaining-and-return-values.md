---
id: 1144
---
# Multiple Chaining and Return Values

Optional chaining can be applied to complex hierarchies and multiple levels of properties. Understanding how return values are wrapped is key to using this pattern effectively.

## 1. Hierarchy Chaining
You can link multiple optional properties together. If any part of the chain is `nil`, the entire chain stops and returns `nil`.

```swift
class University { var name: String = "Harvard" }
class Student { var university: University? }
class Group { var leader: Student? }

let mathGroup = Group()
let uniName = mathGroup.leader?.university?.name
// uniName is of type String?
```

## 2. Return Values of Methods
When you call a method through optional chaining, the return value of that method automatically becomes an optional (if it wasn't already).

```swift
class Calculator {
    func add(_ a: Int, _ b: Int) -> Int { return a + b }
}

var calc: Calculator? = Calculator()
let sum = calc?.add(5, 5) 
// sum is Int?, because calc might have been nil
```

## 3. Methods with No Return Value (`Void`)
If a method returns `Void`, calling it via optional chaining returns `Void?`. This allows you to check if the method was actually called.

```swift
if calc?.clearAll() != nil {
    print("Successfully cleared")
} else {
    print("Calculator was nil, nothing happened")
}
```

## 4. Chaining into Subscripts
When chaining into a result that returns an optional itself (like a Dictionary lookup), you may need multiple question marks.

```swift
var scores: [String: [Int]]? = ["Math": [90, 80]]

// The 'scores' dict is optional, and the lookup result is optional
let firstScore = scores?["Math"]?[0]
// result is Int?
```

## 5. Result Flattening
Interestingly, if you chain a property that is already optional, Swift does not "double wrap" it in multiple optionals.

```swift
class Item { var price: Double? }
var optionalItem: Item? = Item()

let price = optionalItem?.price
// 'price' is Double?, NOT Double??
```

> [!NOTE]
> This behavior is sometimes called "optional flattening" or "sugared flatMap". It ensures that no matter how long the chain is, the result is only ever one level of optionality deep.
