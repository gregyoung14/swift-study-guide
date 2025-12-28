---
id: 914
---
# Using `default` Case in Enums

The `default` case in a `switch` statement acts as a catch-all for any enum cases that aren't explicitly handled in earlier branches.

## 1. When to Use `default`
You should use `default` when:
- You only care about a few specific cases and want to handle the rest with a generic action.
- You are switching over an enum with a very large number of cases.

```swift
enum AppState {
    case starting, running, background, suspended, terminated
}

let state = AppState.running

switch state {
case .running:
    print("App is active")
default:
    print("App is not active")
}
```

## 2. Drawbacks of `default`
While convenient, `default` has a major downside: it disables **Exhaustiveness Checking**. If you add a new case to your enum later, the compiler will not warn you that your `switch` statement doesn't handle it explicitly; it will just fall into the `default` block.

## 3. The Better Alternative: Explicit Cases
For enums you control, it is often better to list all cases, even if some have the same implementation.

```swift
switch state {
case .running:
    print("Active")
case .starting, .background, .suspended, .terminated:
    print("Inactive")
}
```
Now, if you add a `.locked` case, the compiler will flag this code as an error, forcing you to decide how `.locked` should be handled.

## 4. Handling Library Enums with `@unknown default`
When using enums from Apple's frameworks or external libraries, use `@unknown default` to handle future cases without losing warnings for current ones.

> [!TIP]
> Use `default` only when the number of cases is truly unmanageable or when the logic for "all other cases" is fundamentally different and unlikely to change with new additions.
