---
id: 908
---
# Optional Chaining with Enums

Optional chaining is a process for querying and calling properties, methods, and subscripts on an optional that might currently be `nil`. While typically associated with classes and structs, it also applies to enums when they are used as optionals.

## 1. Enum Instance Properties
If an enum has a computed property, you can access it via optional chaining.

```swift
enum UserRole {
    case admin, member, guest

    var permissions: [String] {
        switch self {
        case .admin:  return ["write", "delete", "read"]
        case .member: return ["write", "read"]
        case .guest:  return ["read"]
        }
    }
}

var currentRole: UserRole? = .admin
let canWrite = currentRole?.permissions.contains("write")
// canWrite is of type Bool?
```

## 2. Associated Values and Optional Chaining
You can't directly "chain" into an associated value via dot syntax, but you can chain onto an optional enum instance before performing a match.

```swift
func getRoleName(role: UserRole?) -> String? {
    // If role is nil, this entire expression becomes nil
    return role?.description 
}
```

## 3. Chaining Methods
You can call instance methods using the same `?.` syntax.

```swift
enum PlayerState {
    case idle, active
    func logState() { print("State is \(self)") }
}

var state: PlayerState? = .active
state?.logState() // Prints "State is active"

state = nil
state?.logState() // Nothing happens, no crash.
```

## 4. Deep Chaining
You can chain multiple levels deep. If any link in the chain is `nil`, the entire chain fails gracefully.

```swift
struct User {
    var role: UserRole?
}

let user: User? = User(role: .admin)
let firstPermission = user?.role?.permissions.first
// firstPermission is String?
```

> [!NOTE]
> Optional chaining always returns an **Optional** value, even if the property or method it calls returns a non-optional type.
