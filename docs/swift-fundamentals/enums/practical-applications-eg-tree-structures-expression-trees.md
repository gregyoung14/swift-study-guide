---
id: 911
---
# Practical Applications (Tree Structures, Expression Trees)

Enumerations with associated values and the `indirect` keyword allow search to represent complex, recursive data structures like trees and graphs in a very concise, type-safe way.

## 1. Recursive Enums (Tree Structures)
A recursive enum is an enumeration that has another instance of the enumeration as the associated value for one or more of its cases. You must use the `indirect` keyword to tell the compiler to use a layer of indirection (pointer) for memory management.

```swift
indirect enum BinaryTree<T> {
    case empty
    case node(value: T, left: BinaryTree<T>, right: BinaryTree<T>)
}

let tree = BinaryTree.node(
    value: 10,
    left: .node(value: 5, left: .empty, right: .empty),
    right: .node(value: 15, left: .empty, right: .empty)
)
```

## 2. Expression Trees (Calculator)
Enums are perfect for modeling mathematical expressions, where an expression can be a single number or a combination of two smaller expressions.

```swift
indirect enum ArithmeticExpression {
    case number(Int)
    case addition(ArithmeticExpression, ArithmeticExpression)
    case multiplication(ArithmeticExpression, ArithmeticExpression)
}

// Represents (5 + 4) * 2
let five = ArithmeticExpression.number(5)
let four = ArithmeticExpression.number(4)
let sum = ArithmeticExpression.addition(five, four)
let product = ArithmeticExpression.multiplication(sum, .number(2))

func evaluate(_ expression: ArithmeticExpression) -> Int {
    switch expression {
    case let .number(value):
        return value
    case let .addition(left, right):
        return evaluate(left) + evaluate(right)
    case let .multiplication(left, right):
        return evaluate(left) * evaluate(right)
    }
}

print(evaluate(product)) // 18
```

## 3. Network Response Modeling
A very common real-world use case is modeling the state of a network request.

```swift
enum ViewState<T> {
    case loading
    case success(T)
    case error(message: String)
    case empty
}
```

## 4. Strategy Pattern
Enums can replace certain uses of the Strategy pattern, where different "strategies" are just different cases of an enum with associated parameters.

```swift
enum SortOrder {
    case ascending
    case descending
    case custom((String, String) -> Bool)
}
```

> [!IMPORTANT]
> When using recursive enums, always ensure you have a "base case" (like `.empty` or `.number`) to prevent infinite recursion and stack overflow errors during processing.
