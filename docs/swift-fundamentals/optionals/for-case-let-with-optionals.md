---
id: 1139
---
# `for-case-let` with Optionals

The `for-case-let` loop is a powerful pattern matching tool that allows you to iterate over a collection while filtering for and unwrapping optional values in one step.

## 1. Iterating over Optional Collections
If you have an array containing optional values, a standard `for-in` loop will give you the optionals themselves.

```swift
let numbers: [Int?] = [1, nil, 3, 4, nil, 6]

for number in numbers {
    // 'number' is Int?
}
```

## 2. Using `for-case-let`
By using `for-case-let`, you can filter out the `nil` values and work directly with the unwrapped values.

```swift
for case let number? in numbers {
    print("Got a number: \(number)") // number is unwrapped Int
}
```
*Note: The `?` after `number` is shorthand for `.some(number)`.*

## 3. Longhand Syntax
The loop above is equivalent to matching against the `.some` case of the Optional enum.

```swift
for case .some(let number) in numbers {
    print(number)
}
```

## 4. Benefits
- **Clean Code**: No need for nested `if let` blocks inside your loops.
- **Improved Performance**: Skips the unwanted `nil` iterations concisely.
- **Combined Filtering**: You can add a `where` clause for even more control.

```swift
for case let number? in numbers where number > 3 {
    print("Found large number: \(number)")
}
```

## 5. Comparison
| Method | Code | Result |
| :--- | :--- | :--- |
| **Standard** | `for x in list { if let y = x { ... } }` | Verbose, 2 levels of indentation |
| **CompactMap** | `for x in list.compactMap({$0}) { ... }` | Creates a new array (memory overhead) |
| **for-case-let** | `for case let x? in list { ... }` | Concise, efficient, no extra allocation |

> [!NOTE]
> `for-case-let` works on any collection where the elements match the pattern. It's particularly useful for handling arrays of delegates or weakly held objects that might have become `nil`.
