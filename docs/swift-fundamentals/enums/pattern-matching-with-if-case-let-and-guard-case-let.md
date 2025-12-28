---
id: 910
---
# Pattern Matching with `if case let` and `guard case let`

While `switch` is the standard tool for handling enums, sometimes you only care about a **single case**. Using `switch` in these situations can be verbose and require an annoying `default: break` clause. Swift provides `if case let` and `guard case let` as more concise alternatives.

## 1. `if case let` (Conditional Execution)
Use this when you want to execute code only if an enum matches a specific case and extract its values.

```swift
enum ValidationResult {
    case success
    case failure(reason: String, code: Int)
}

let result = ValidationResult.failure(reason: "Invalid Email", code: 400)

// Instead of a switch with default: break
if case let .failure(error, code) = result {
    print("Failed with error: \(error) (Code: \(code))")
}
```

## 2. Matching Specific Values with `if case`
You can also include specific value requirements without extraction.

```swift
if case .failure(_, 400) = result {
    print("Specific 400 error occurred.")
}
```

## 3. `guard case let` (Early Exit)
Use this within functions or loops to ensure an enum matches a specific case before proceeding. If it doesn't match, you must exit the scope.

```swift
func processSuccess(result: ValidationResult) {
    guard case .success = result else {
        print("Not a success, aborting.")
        return
    }
    
    print("Proceeding with success logic...")
}
```

## 4. Why use these over `switch`?
- **Conciseness**: Avoids the broad structure and required `default` case of `switch`.
- **Clarity**: Highlighting that the logic only applies to one specific state.
- **Nesting**: Easier to use within other control flow structures without deep indentation.

## 5. Combining with Conditions
You can add commas to include other boolean conditions.

```swift
if case let .failure(reason, _) = result, reason.contains("Email") {
    print("There was an issue with the email address.")
}
```

> [!NOTE]
> `if case let` is essentially a "conditional pattern match". It reads as "If the case of `result` matches `.failure`, then bind the associated values to these constants and execute the block."
