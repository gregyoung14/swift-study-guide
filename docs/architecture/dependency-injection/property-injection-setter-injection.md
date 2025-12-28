---
id: 37
---
# Property Injection (Setter Injection)

**Property Injection** is a pattern where dependencies are assigned to an object's properties after it has been initialized. In iOS, this is often a necessity when working with system-instantiated classes like `UIViewController`.

## Why we use it in iOS
The primary reason for Property Injection in UIKit is **Storyboards and XIBs**. The system calls `init(coder:)`, and you cannot pass custom arguments to that initializer.

```swift
class ProfileViewController: UIViewController {
    // Requirements must be public 'var' and optional (or implicitly unwrapped)
    var userService: UserServiceProtocol! 
    
    override func viewDidLoad() {
        super.viewDidLoad()
        userService.load() // Crashes if not injected!
    }
}

// In the Coordinator/Router:
let vc = storyboard.instantiateViewController(...) as! ProfileViewController
vc.userService = RealUserService() // Property Injection
```

## Advantages
1.  **Framework Compatibility**: Works seamlessly with UIKit, Storyboards, and older Objective-C libraries.
2.  **Optional Dependencies**: Perfect for features that aren't strictly required (e.g., an optional `AnalyticsTracker`).
3.  **Circular Dependencies**: Can break loops where two objects need each other.

## Disadvantages
1.  **Mutability**: Dependencies must be `var`, allowing them to be changed at runtime (unsafe).
2.  **Safety Risk**: It's easy to forget to set a property, leading to runtime crashes.
3.  **Encapsulation Leak**: Dependencies must be `public` or `internal` so they can be set from outside.

## Comparison Table

| Feature | Initializer Injection | Property Injection |
| :--- | :--- | :--- |
| **Immutability** | `let` (Constant) | `var` (Mutable) |
| **Visibility** | `private` | `internal` / `public` |
| **Safety** | High (Compile-time) | Low (Runtime crashes) |
| **Usage** | ViewModels, Services | ViewControllers, Storyboards |

## Improving Property Injection Safety
To make property injection safer, use a combination of **Private Setters** and **Assertions**.

```swift
class OrderVC: UIViewController {
    // Visible for reading, but can only be SET within the module
    private(set) var api: API! 
    
    func inject(api: API) {
        self.api = api
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        assert(api != nil, "Forgot to inject API into OrderVC!")
    }
}
```

## Summary
Property Injection is a "necessary evil" in UIKit development. While **Initializer Injection** is always preferred, understanding how to use property injection safely is a vital skill for handling view controller life-cycles and legacy codebases.
