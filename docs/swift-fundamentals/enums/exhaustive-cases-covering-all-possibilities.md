---
id: 900
---
# Exhaustive Cases (Covering All Possibilities)

One of the most powerful features of Swift enums is **Exhaustiveness Checking**. The compiler ensures that when you switch over an enum, you have handled every possible case.

## 1. Compiler Enforcement
If you miss a case in a `switch` statement, the code will not compile.

```swift
enum PowerState {
    case on, off, sleep
}

let state = PowerState.on

// Error: Switch must be exhaustive
switch state {
case .on:
    print("Power is on")
case .off:
    print("Power is off")
}
```

To fix this, you must add `case .sleep:` or a `default:` case.

## 2. Default Case
Use `default` to catch any cases not explicitly mentioned.

```swift
switch state {
case .on:
    print("Working...")
default:
    print("Not working")
}
```

## 3. Non-Frozen Enums and `@unknown default`
For enums defined in library frameworks (like Apple's SDKs), new cases might be added in the future. These are called **Non-Frozen Enums**.

To handle future cases gracefully while still getting warnings for existing unhandled cases, use `@unknown default`.

```swift
import UIKit

let userInterfaceStyle = UITraitCollection.current.userInterfaceStyle

switch userInterfaceStyle {
case .light:
    print("Light mode")
case .dark:
    print("Dark mode")
case .unspecified:
    print("Unspecified")
@unknown default:
    print("A new style was added to UIKit!")
}
```

## 4. Why Exhaustiveness Matters
1. **Safety**: You won't forget to handle a new state after refactoring.
2. **Logic Verification**: It forces you to think about every possible state of your system.
3. **Clarity**: It documents the intent of the code clearly.

> [!TIP]
> Avoid using `default` for enums you own. Instead, list every case explicitly. This way, if you add a new case later, the compiler will alert you to every place that needs an update.
