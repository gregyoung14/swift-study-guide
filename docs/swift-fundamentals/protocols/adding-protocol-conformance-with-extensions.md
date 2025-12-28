---
id: 1172
---
# Adding Protocol Conformance with Extensions

Extensions are the primary tool for adopting and conforming to protocols in a clean, modular way. They allow you to add protocol requirements to a type even if you don't have access to its original source code.

## 1. Basic Extension Conformance
When you add conformance via an extension, you must implement all the mandatory requirements of that protocol inside the extension block.

```swift
protocol Runnable {
    func run()
}

struct Robot {}

extension Robot: Runnable {
    func run() {
        print("Robot is moving...")
    }
}
```

## 2. Conditional Conformance with Extensions
You can use an extension to make a generic type conform to a protocol only if its underlying types also conform to that protocol.

```swift
extension Array: Runnable where Element == Robot {
    func run() {
        for robot in self { robot.run() }
    }
}
```

## 3. Adopting Protocols Retroactively
This is a core feature of Swift's architecture. You can give new abilities to types defined in other modules.

```swift
extension String: Runnable {
    func run() {
        print("Executing command: \(self)")
    }
}
"print_report".run()
```

## 4. Organizing Code via Extensions
Even if you define the type yourself, using extensions for protocol conformance is highly recommended for clarity.

```swift
class MyViewController: UIViewController {
    // Main lifecycle logic
}

extension MyViewController: UITableViewDataSource {
    // Table calculation logic
}

extension MyViewController: UITableViewDelegate {
    // Table interaction logic
}
```

## 5. Performance Note
Adding protocol conformance via extensions does not incur a performance penalty compared to adding it in the main declaration. Both use the same "witness table" mechanism for dynamic dispatch.

> [!IMPORTANT]
> You cannot declare a property (stored property) inside an extension. If a protocol requires a property, you must either define it in the main declaration or implement it as a **computed property** in the extension.
