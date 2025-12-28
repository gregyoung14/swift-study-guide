---
id: 1158
---
# Single Optional Binding (`if let myValue = optionalValue`)

Single optional binding is the most fundamental way to safely access data within an optional. It combines a null check and a type-safe extraction into one operation.

## 1. Basic Syntax
```swift
let possibleName: String? = "John"

if let actualName = possibleName {
    // inside this block, 'actualName' is String, not String?
    print("The name is \(actualName)")
}
```

## 2. Shadowing (Standard Practice)
It is highly recommended to name the unwrapped constant exactly the same as the optional variable. This prevents you from accidentally using the optional version downstream.

```swift
var age: Int? = 25

if let age = age {
    print("User is \(age) years old.")
}
```

## 3. Use Case: Conditional UI
Only show a component if a value exists.

```swift
if let bio = user.bio {
    bioLabel.text = bio
    bioLabel.isHidden = false
} else {
    bioLabel.isHidden = true
}
```

## 4. Mutable Binding (`if var`)
If you need to change the unwrapped value within the block, use `if var`. Note that this only changes the local copy, not the original optional variable.

```swift
if var name = possibleName {
    name = name.uppercased()
    print(name)
}
```

## 5. Scope Warning
The unwrapped variable exists **only** within the curly braces of the `if` block. If you need the value to persist for the rest of your function, use `guard let` instead.

> [!TIP]
> Use `if let` when you have a small, specific block of code that should only run if the data is present. It keeps the "optionality check" coupled directly with the logic that uses the data.
