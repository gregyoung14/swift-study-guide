---
id: 1003
---
﻿# Applying `where` Clauses to Functions and Types

Generic `where` clauses allow you to define requirements for the type parameters associated with a generic function, structure, class, or enumeration. This enables you to write highly specialized code that only works when certain conditions are met.

## Using `where` with Functions

For functions, the `where` clause is placed after the function's parameter list and before the opening brace of its body.

### Basic Requirements
```swift
func allItemsEqual<C1: Container, C2: Container>(_ container1: C1, _ container2: C2) -> Bool
    where C1.Item == C2.Item, C1.Item: Equatable {
        
    if container1.count != container2.count { return false }
    
    for i in 0..<container1.count {
        if container1[i] != container2[i] { return false }
    }
    
    return true
}
```

In the example above, the `where` clause ensures:
1.  Both containers store the **same type** of items (`C1.Item == C2.Item`).
2.  The items being stored conform to `Equatable` (`C1.Item: Equatable`).

## Using `where` with Types

You can also apply `where` clauses to the definition of structures, classes, and enumerations.

```swift
struct Stack<Element> where Element: Equatable {
    private var items: [Element] = []
    
    func isTop(_ item: Element) -> Bool {
        return items.last == item
    }
}
```

## Comparisons: `:` vs `where`

Simple constraints can often be written using the colon syntax, but `where` is more powerful for complex requirements.

| Complexity | Colon Syntax (`:`) | `where` Clause |
| :--- | :--- | :--- |
| **Simple** | `T: Equatable` | `T where T: Equatable` |
| **Multiple Protocols** | `T: P1 & P2` | `T where T: P1, T: P2` |
| **Associated Types** | *Not Possible* | `T where T.Item == String` |
| **Type Relationships** | *Not Possible* | `T1, T2 where T1.Item == T2.Item` |

## Specialized Extensions

The `where` clause is most commonly used in extensions to provide functionality only to specific instances of a generic type.

```swift
extension Array where Element: Numeric {
    func sum() -> Element {
        return reduce(0, +)
    }
}

let numbers = [1, 2, 3]
print(numbers.sum()) // Works

let names = ["Alice", "Bob"]
// names.sum() // Compile-time error: 'String' is not 'Numeric'
```

## Best Practices

*   **Use the colon syntax for simple protocol constraints.** It's more concise and readable.
*   **Use `where` for relationships between types** (e.g., matching associated types) or for multiple complex requirements.
*   **Put each requirement on a new line** in the `where` clause if there are many of them, to improve readability.
*   **Leverage extensions with `where` clauses** to keep your base generic types clean while providing powerful specialized functionality.

---

> [!TIP]
> Since Swift 5.3, you can use `where` clauses on members of a generic type (like methods or properties) individually, rather than requiring an extension.

