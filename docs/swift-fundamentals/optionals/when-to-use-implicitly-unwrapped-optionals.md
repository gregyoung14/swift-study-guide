---
id: 1168
---
# When to Use Implicitly Unwrapped Optionals

Implicitly Unwrapped Optionals (IUOs) are declared with a `!` (e.g., `var name: String!`). They occupy a middle ground between safe optionals and forced-unwrapped variables.

## 1. The Main Use Case: UI Outlets
The most common use of IUOs is with Interface Builder outlets. Because these are initialized by the system after the `init` method of the view controller but before `viewDidLoad`, they are technically `nil` for a brief moment.

```swift
@IBOutlet var welcomeLabel: UILabel!
```
Using an IUO here avoids having to type `welcomeLabel?` everywhere in your view controller.

## 2. Two-Phase Initialization
Some class hierarchies require two objects to be initialized such that they refer to each other. Because neither can be "fully" initialized without the other, one property must be an optional (or IUO) to allow the first object to complete its init.

## 3. API Interoperability (Objective-C)
When Swift imports Objective-C code that has not been audited for nullability (no `_Nullable` or `_Nonnull` annotations), it often imports them as IUOs.

## 4. When NOT to use IUOs
- **Member Variables**: If a value is genuinely optional (can go from some value to nil and back), use `?`.
- **Function Parameters**: Never define a function that takes an IUO. Take a regular optional and unwrap it safely inside.
- **Local Variables**: Very rarely needed. Use `if let` or `guard let`.

## 5. Summary Table
| Scenario | Use IUO (`!`)? | Reason |
| :--- | :--- | :--- |
| @IBOutlet | **Yes** | Standard iOS pattern. |
| User Profile Bio | **No** | Bio can be legitimately missing. |
| Network Token | **No** | Auth can fail or expire. |
| Bundle Config File | **Maybe** | If essential for app survival. |

> [!IMPORTANT]
> An IUO is a **convenience**, not a safety feature. It tells the compiler to "pretend" the value is always there, even though it might not be. Use that power carefully.
