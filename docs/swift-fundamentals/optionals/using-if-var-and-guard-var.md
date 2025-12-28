---
id: 1165
---
# Using `if var` and `guard var`

While `if let` and `guard let` create **constants** out of unwrapped values, you can use `if var` and `guard var` if you need the unwrapped value to be **mutable** within the subsequent scope.

## 1. `if var` Syntax
This is useful when you want to take a value, perform modifications on it, and then use the modified version—all without changing the original optional variable.

```swift
var optionalName: String? = "antigravity"

if var name = optionalName {
    name = name.uppercased()
    print(name) // "ANTIGRAVITY"
}

print(optionalName!) // still "antigravity"
```

## 2. `guard var` Syntax
Similar to `guard let`, this creates a mutable variable available for the rest of the function.

```swift
func process(input: String?) {
    guard var text = input else { return }
    
    text.append("!")
    print(text)
}
```

## 3. Important: No Side Effects
When you use `if var`, you are working with a **local copy** of the unwrapped value. Modifying this local variable **does not** update the original optional variable from which it was unwrapped.

## 4. When to Use
- **Formatting**: Preprocessing a string before displaying it.
- **Calculations**: Running intermediate math steps on an unwrapped number.
- **State Preparation**: Adjusting a struct's properties before passing it to another function.

## 5. Alternatives
Many developers prefer to use `if let` for the unwrap and then define a separate variable if mutation is needed, to keep the logic more explicit.

```swift
if let name = optionalName {
    var modifiedName = name
    modifiedName = modifiedName.uppercased()
}
```

> [!NOTE]
> `if var` is elegant but less commonly seen than `if let`. Use it when the mutation is central to the logic of the block.
