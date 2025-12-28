---
id: 1182
---
# Defining Associated Types (`associatedtype Item`)

Associated types give protocols a way to support generics. They act as a placeholder name for a type used within the protocol.

## 1. Syntax
You declare an associated type using the `associatedtype` keyword.

```swift
protocol Bag {
    associatedtype Element
    mutating func add(_ element: Element)
    var allItems: [Element] { get }
}
```

## 2. Setting the Type
When a type adopts the protocol, it provides the concrete type for the placeholder.

```swift
struct LaundryBag: Bag {
    typealias Element = Clothing // Explicitly naming it
    
    var allItems: [Clothing] = []
    mutating func add(_ element: Clothing) {
        allItems.append(element)
    }
}
```

## 3. Type Inference
Swift's compiler is smart enough to infer the associated type from the usage in methods and properties. You rarely need the `typealias` line in practice.

```swift
struct TrashBag: Bag {
    var allItems: [Waste] = []
    mutating func add(_ element: Waste) { // Compiler infers Element == Waste
        allItems.append(element)
    }
}
```

## 4. Constraints
You can restrict what types can fill the placeholder by adding a colon and a protocol constraint or a `where` clause.

```swift
protocol NumericBag: Bag where Element: Numeric {
    func sum() -> Element
}
```

## 5. Comparison: Generics vs. Associated Types
- **Generics (`Struct<T>`)**: The user of the type chooses what `T` is.
- **Associated Types (`Protocol P`)**: The implementation of the protocol chooses what the placeholder is.

> [!NOTE]
> Associated types allow for highly abstract code. For example, Swift's `Collection` protocol uses associated types for `Element`, `Index`, and `Iterator`, allowing a single protocol to describe everything from a simple `Array` to a complex `DatabaseCursor`.
