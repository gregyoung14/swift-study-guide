---
id: 1185
---
# Delegation with Optional Methods

In most Swift protocols, all methods are required. However, sometimes you want delegate methods that are "nice to have" but not strictly mandatory for every implementer.

## 1. The `@objc` Approach
To define optional methods in a protocol, you must use Objective-C interoperability.

```swift
import Foundation

@objc protocol MediaPickerDelegate {
    func didPickPhoto(_ photo: UIImage) // Required by default
    @objc optional func didCancelSelection() // Optional
}
```

## 2. Limitations of `@objc`
- **Class-Only**: The protocol can only be adopted by classes (reference types).
- **No Value Types**: Structs and Enums cannot conform to `@objc` protocols.
- **Availability**: Requires importing `Foundation` or `UIKit`.

## 3. Calling Optional Methods
When calling an optional method, you must use **Optional Chaining** because the method itself might not be implemented by the delegate.

```swift
delegate?.didCancelSelection?() 
// Note the extra ? after the method name
```

## 4. The "Swift-Native" Alternative
If you want to stay in pure Swift (and support structs), use **Protocol Extensions** to provide a "do nothing" default implementation. This makes the method effectively optional.

```swift
protocol GameDelegate {
    func gameDidStart()
    func gameDidEnd() 
}

extension GameDelegate {
    func gameDidEnd() {} // Default implementation makes it optional!
}
```

## 5. Comparison
| Feature | `@objc optional` | Default Extension |
| :--- | :--- | :--- |
| **Type Support** | Classes only | Class, Struct, Enum |
| **Introspection** | Can check `responds(to:)` | Hard to tell if it's default or not |
| **Performance** | Runtime dynamic lookup | Static/Witness dispatch |

> [!TIP]
> Prefer the **Default Extension** approach in modern Swift code. It is more flexible and doesn't rely on the legacy Objective-C runtime.
