---
id: 1142
---
# Implicitly Unwrapped Optionals (`!`)

**Implicitly Unwrapped Optionals** (IUOs) are optionals that are declared with a `!` instead of a `?`. They are technically optionals but can be accessed as if they were non-optional values.

## 1. Syntax and Behavior
```swift
let assumedString: String! = "An implicitly unwrapped optional string."
let implicitString: String = assumedString // No need for '!' here
```
Behind the scenes, it is still an optional. If you try to access it when it is `nil`, the app will crash, just like forced unwrapping.

## 2. Common Use Cases

### @IBOutlet and @IBAction
UI components in Storyboards are often nil until the view is loaded, but once loaded, they are guaranteed to exist. Declaring them as IUOs avoids cluttering code with `?` or `!`.

```swift
@IBOutlet var label: UILabel!
```

### Dependency Injection
When a value cannot be set during initialization but is guaranteed to be set before any other methods are called.

### Two-Phase Initialization
Solving circular dependencies between two class instances where neither can be initialized without the other.

## 3. Risks
The convenience of IUOs comes with the same risk as forced unwrapping: **Runtime Crashes**. If the assumption that the value "will always be there" is broken, your app will fail.

## 4. Best Practices
- **Use Sparingly**: Default to regular optionals (`?`) whenever possible.
- **Verify Assumptions**: Only use `!` if there is a fundamental structural reason why the value cannot be `nil` at the point of use.
- **Check if Nil**: You can still check an IUO for `nil` just like a normal optional.

```swift
if assumedString != nil {
    print(assumedString!)
}
```

> [!WARNING]
> If a variable has any chance of becoming `nil` during its lifetime after being set, **do not** use an Implicitly Unwrapped Optional.
