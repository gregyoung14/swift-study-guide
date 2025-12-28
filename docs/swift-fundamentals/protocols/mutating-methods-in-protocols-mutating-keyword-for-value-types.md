---
id: 1193
---
# Mutating Methods in Protocols (`mutating` keyword for value types)

When a protocol includes a method that is intended to modify (mutate) the instance it belongs to, that method must be marked with the `mutating` keyword. This requirement ensures that any value type (struct or enum) that adopts the protocol can safely implement the method to modify its own properties.

## How it Works

In Swift, value types are immutable by default. To modify a property within an instance method of a struct or enum, the method must be explicitly marked as `mutating`. When a protocol defines such a method, it must also include the `mutating` keyword in its requirement.

### Protocol Requirement
```swift
protocol Toggleable {
    mutating func toggle()
}
```

### Implementation in Value Types
When a `struct` or `enum` conforms to the protocol, it **must** include the `mutating` keyword in its implementation.

```swift
struct LightSwitch: Toggleable {
    var isOn = false
    
    mutating func toggle() {
        isOn.toggle()
    }
}

enum PowerState: Toggleable {
    case on, off
    
    mutating func toggle() {
        self = (self == .on) ? .off : .on
    }
}
```

### Implementation in Reference Types
Classes are reference types and do not require the `mutating` keyword to modify their properties. When a class conforms to a protocol with a `mutating` requirement, it specifies the method **without** the `mutating` keyword.

```swift
class SmartBulb: Toggleable {
    var isOn = false
    
    func toggle() { // No 'mutating' needed for classes
        isOn.toggle()
    }
}
```

## Why it is Important

1.  **Safety**: It explicitly tells the compiler and the developer that the method will change the state of the instance.
2.  **Compatibility**: It allows a single protocol to be used by both value types and reference types, providing the necessary flexibility for structs while being transparent for classes.
3.  **Compiler Guarantees**: For value types, the compiler ensures that `mutating` methods are only called on `var` instances, preventing accidental mutation of constants (`let`).

## Example: A Bank Account Protocol

```swift
protocol BankAccount {
    var balance: Double { get }
    mutating func deposit(amount: Double)
    mutating func withdraw(amount: Double) -> Bool
}

struct SavingsAccount: BankAccount {
    private(set) var balance: Double = 0.0
    
    mutating func deposit(amount: Double) {
        balance += amount
    }
    
    mutating func withdraw(amount: Double) -> Bool {
        if balance >= amount {
            balance -= amount
            return true
        }
        return false
    }
}
```

## Best Practices

*   **Always mark protocol methods as `mutating` if they *might* modify the instance.** It's better to provide the flexibility for structs even if you primarily intend to use the protocol with classes.
*   **Don't use `mutating` if the protocol is class-only.** If you define a class-only protocol (`protocol MyProtocol: AnyObject`), you should not use the `mutating` keyword as it is redundant.
*   **Consider side effects.** Even for classes, a method marked as `mutating` in a protocol signals a state change, which is helpful for readability.

---

> [!NOTE]
> If you call a `mutating` method on a protocol type (e.g., `var item: Toggleable`), the compiler allows it because it knows the implementation (whether it's a struct or a class) safely handles the mutation.

