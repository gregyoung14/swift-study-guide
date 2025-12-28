---
id: 1177
---
# Combining Protocols with `&`

Protocol composition allows you to define a type that satisfies the requirements of multiple protocols simultaneously. This is done using the protocol composition operator (`&`).

## 1. Basic Composition
You can use `&` whenever you would use a single type name.

```swift
protocol Named { var name: String { get } }
protocol Aged { var age: Int { get } }

func wishHappyBirthday(to person: Named & Aged) {
    print("Happy Birthday \(person.name), you are \(person.age)!")
}
```

## 2. Temporary Ad-hoc Types
Protocol composition creates a temporary, unnamed type. You don't need to define a new protocol that inherits from both just to use them together in one function.

```swift
// AVOID this if it's only for one function:
protocol NamedAndAged: Named, Aged {}

// PREFER this:
func handle(item: Named & Aged) { ... }
```

## 3. Multiple Protocols
You can list as many protocols as you need.

```swift
let object: ProtocolA & ProtocolB & ProtocolC
```

## 4. Properties and Methods
An object of a composed type has access to all members of all its constituent protocols.

## 5. Use Case: Interface Blueprinting
Composing protocols is a key part of **Dependency Injection**. By requiring an object that conforms to several small protocols rather than one large one, your functions become much easier to test and mock.

```swift
func processPayment(processor: Authable & Chargeable & Loggable) {
    // Has everything needed for the complex operation
}
```

## Summary Table
| Method | Syntax | Best For |
| :--- | :--- | :--- |
| **Inheritance** | `protocol C: A, B {}` | Permanent relationships |
| **Composition** | `A & B` | One-off requirements, function parameters |

> [!TIP]
> Protocol composition is the "Swiss Army Knife" of Swift typing. It allows you to build exactly the specific type constraints you need for a function without polluting your codebase with hundreds of tiny protocol definitions.
