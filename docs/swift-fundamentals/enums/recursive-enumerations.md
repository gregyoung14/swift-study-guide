---
id: 913
---
# Recursive Enumerations

A **Recursive Enumeration** is an enumeration that has another instance of the enumeration as the associated value for one or more its cases.

## 1. Why Recusion is Tricky for Enums
Normally, the compiler needs to know exactly how much memory an enum instance will take. Because a recursive enum could theoretically contain itself infinitely, its size could be infinite. 

## 2. The `indirect` Solution
To solve this, Swift uses the `indirect` keyword. This tells the compiler to store the associated data behind a pointer (on the heap) rather than directly in the enum instance (on the stack).

```swift
enum ArithmeticExpression {
    case number(Int)
    indirect case addition(ArithmeticExpression, ArithmeticExpression)
    indirect case multiplication(ArithmeticExpression, ArithmeticExpression)
}
```

## 3. Applying `indirect` to the Entire Enum
If all cases that have associated values need indirection, you can place the `indirect` keyword before the `enum` keyword.

```swift
indirect enum LinkedList<T> {
    case end
    case node(value: T, next: LinkedList<T>)
}
```

## 4. Usage Example: Linked List
Recursive enums are an elegant way to implement data structures like linked lists or trees.

```swift
let list = LinkedList.node(value: 1, next: .node(value: 2, next: .end))

func printList<T>(_ list: LinkedList<T>) {
    switch list {
    case .end:
        print("End")
    case .node(let value, let next):
        print("\(value) -> ", terminator: "")
        printList(next)
    }
}

printList(list) // 1 -> 2 -> End
```

> [!IMPORTANT]
> Always ensure your recursive structure has a "base case" (like `.end` or `.empty`) that does not contain the enum itself, otherwise operations on it will never terminate.
