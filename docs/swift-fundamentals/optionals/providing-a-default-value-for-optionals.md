---
id: 1155
---
# Providing a Default Value for Optionals

Providing a default value is a common defensive programming technique to ensure that your application always has valid data to work with, even when an expected optional value is missing.

## 1. Nil-Coalescing Operator (`??`)
The most idiomatic way to provide a default.

```swift
let userInput: String? = nil
let name = userInput ?? "Guest"
```

## 2. Dictionary `default` Parameter
When accessing a dictionary, you can specify a default value directly in the subscript. This returns a non-optional value.

```swift
let counts = ["apples": 5]
let orangeCount = counts["oranges", default: 0]
// orangeCount is Int (0), not Int?
```

## 3. UI Defaulting
When displaying data to the user, you should always provide a fallback for optional strings to avoid showing "nil" or empty labels.

```swift
label.text = user.displayName ?? "Unknown User"
```

## 4. Defaulting through Computed Properties
You can encapsulate defaulting logic inside your models to keep your UI code clean.

```swift
struct Profile {
    private var bio: String?
    
    var displayBio: String {
        return bio ?? "No bio provided yet."
    }
}
```

## 5. Defaulting in Initializers
You can use nil-coalescing during initialization to ensure internal state is always valid.

```swift
init(id: String?, name: String?) {
    self.id = id ?? UUID().uuidString
    self.name = name ?? "New User"
}
```

> [!TIP]
> Always ask: "What is a sensible default for this context?" 
> - For numbers, it's often `0`.
> - For strings, it might be `"Unknown"` or `""`.
> - For booleans, it's usually `false`.
