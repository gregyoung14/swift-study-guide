---
id: 892
---
# Custom Conformance in Enums

Swift provides automatic protocol synthesis for enums in many cases, but sometimes you need **Custom Conformance** to control how an enum behaves when it is compared, hashed, or represented as a raw value.

## 1. Custom Equatable Conformance
By default, enums with no associated values (or those with `Equatable` associated values) get automatic `Equatable` conformance. However, if you want specific comparison logic (e.g., ignoring certain associated values), you must implement it manually.

```swift
enum SearchResult: Equatable {
    case success(id: Int, data: String)
    case failure(Error)

    static func == (lhs: SearchResult, rhs: SearchResult) -> Bool {
        switch (lhs, rhs) {
        case (.success(let lid, _), .success(let rid, _)):
            // Only compare IDs, ignore data
            return lid == rid
        case (.failure, .failure):
            return true
        default:
            return false
        }
    }
}
```

## 2. Custom RawRepresentable
You can make an enum conform to `RawRepresentable` even if it doesn't use the standard `enum Name: Type` syntax. This is useful for complex mapping logic.

```swift
enum Level: RawRepresentable {
    case low, medium, high, extreme

    typealias RawValue = Int

    init?(rawValue: Int) {
        switch rawValue {
        case 0...1: self = .low
        case 2...5: self = .medium
        case 6...9: self = .high
        case 10:    self = .extreme
        default:    return nil
        }
    }

    var rawValue: Int {
        switch self {
        case .low:     return 1
        case .medium:  return 5
        case .high:    return 9
        case .extreme: return 10
        }
    }
}
```

## 3. Custom Comparable
For enums to be sorted or used with `<` and `>`, they must conform to `Comparable`.

```swift
enum Rank: Int, Comparable {
    case bronze = 1
    case silver = 2
    case gold = 3

    static func < (lhs: Rank, rhs: Rank) -> Bool {
        return lhs.rawValue < rhs.rawValue
    }
}

let myRank = Rank.silver
let yourRank = Rank.gold
print(myRank < yourRank) // true
```

> [!TIP]
> Use Custom Conformance sparingly. Automatic synthesis is faster and less prone to developer error. Only override when the default behavior doesn't match your business logic.
