---
id: 1174
---
# Associated Types in Protocols

Associated types are a way to use **Generics** within protocols. They act as a placeholder for a type that is used as part of the protocol, without specifying what that type is until the protocol is adopted.

## 1. Defining an Associated Type
Use the `associatedtype` keyword inside the protocol.

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
```

## 2. Specifying the Associated Type
When a type conforms to the protocol, it can explicitly specify the type using a `typealias`, or Swift can often infer it from the method implementations.

```swift
struct IntStack: Container {
    // Optional: typealias Item = Int
    var items: [Int] = []
    
    mutating func append(_ item: Int) { // Inference happens here
        items.append(item)
    }
    
    var count: Int { items.count }
    subscript(i: Int) -> Int { items[i] }
}
```

## 3. Constraints on Associated Types
You can add requirements to the associated type itself, ensuring that any type used must conform to certain protocols.

```swift
protocol SuffixableContainer: Container {
    associatedtype Suffix: SuffixableContainer where Suffix.Item == Item
    func suffix(_ size: Int) -> Suffix
}
```

## 4. Common Real-World Example: `IteratorProtocol`
Swift's own collection system uses associated types extensively.

```swift
protocol IteratorProtocol {
    associatedtype Element
    mutating func next() -> Element?
}
```

## 5. Key Concept: "Any" vs. Associated Types
Associated types are different from using `Any`. `Any` loses type safety and requires casting. Associated types maintain full compile-time type safety once the protocol is implemented.

> [!CAUTION]
> Protocols with associated types have historical limitations (they "could only be used as generic constraints"). Since Swift 5.7, you can use them as types using the `any` keyword (Existential types), but this comes with performance trade-offs.
