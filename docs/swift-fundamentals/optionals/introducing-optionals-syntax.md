---
id: 1143
---
# Introducing Optionals (`?` syntax)

Optionals are Swift's solution to the problem of "missing data." In many languages, a variable can be `null` or `nil`, leading to dangerous "Null Pointer Exceptions." Swift handles this by making the absence of a value a first-class type.

## 1. Declaration
To make a variable optional, append a `?` to its type.

```swift
var middleName: String? = "John"
var suffix: String? = nil // Valid
```

## 2. Type System Clarity
In Swift, `String` and `String?` are **different types**.

```swift
let name: String = "Alice"
let optName: String? = "Bob"

// name = optName // Error: Cannot assign value of type 'String?' to type 'String'
```
This forces you to acknowledge the possibility of a missing value before you can use it.

## 3. The Logic of `?`
Think of an optional as a "box".
- If the box is full, it contains a value (e.g., `"Alice"`).
- If the box is empty, it is `nil`.

To get the value out, you must "open the box" (unwrap it).

## 4. Initialization
If you define an optional variable without an initial value, it is automatically set to `nil`.

```swift
var status: Int? 
print(status) // nil
```

## 5. Summary
| Syntax | Meaning |
| :--- | :--- |
| `Type` | Must always have a value. |
| `Type?` | May have a value OR be empty (`nil`). |

> [!NOTE]
> Swift was designed with "Safety First" in mind. Optionals are the primary tool used by the compiler to ensure that you have considered every edge case where data might not be available.
