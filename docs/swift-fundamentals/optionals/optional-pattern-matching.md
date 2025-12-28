---
id: 1152
---
# Optional Pattern Matching

Since Optionals are implemented as an enumeration (`.some(T)` and `.none`), you can use Swift's powerful pattern matching syntax to work with them.

## 1. Matching in a `switch`
You can switch directly over an optional and match the specific cases.

```swift
let optionalInt: Int? = 42

switch optionalInt {
case .some(let value):
    print("Value is \(value)")
case .none:
    print("No value")
}
```

## 2. The `?` Pattern
Swift provides a shorthand syntax for matching the `.some` case in a property or variable pattern.

```swift
switch optionalInt {
case let value?:
    print("Value is \(value)")
case nil:
    print("No value")
}
```

## 3. Filtering in Loops
Use `for case let ... in` to iterate over an array of optionals while ignoring the `nil` entries.

```swift
let scores: [Int?] = [10, nil, 20, 30]

for case let score? in scores {
    print("Score: \(score)")
}
```

## 4. Matching with `if case`
Use `if case let` to unwrap an optional and check an additional condition in one line.

```swift
if case let value? = optionalInt, value > 40 {
    print("\(value) is greater than 40")
}
```

## 5. Using `where` with Optional Patterns
Pattern matching allows for fine-grained control using `where` clauses.

```swift
switch optionalInt {
case let value? where value % 2 == 0:
    print("Even number: \(value)")
case let value?:
    print("Odd number: \(value)")
case nil:
    break
}
```

> [!IMPORTANT]
> Pattern matching with optionals is often cleaner than using `if let` when you have complex conditions or are already inside a `switch` statement.
