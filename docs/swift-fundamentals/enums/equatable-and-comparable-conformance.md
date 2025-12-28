---
id: 899
---
# Equatable and Comparable Conformance

Making your enums conform to `Equatable` and `Comparable` allows them to be compared using standard operators like `==`, `!=`, `<`, and `>`.

## 1. Automatic Equatable Synthesis
Swift can automatically synthesize `Equatable` conformance for an enum if:
1. You declare the conformance.
2. All cases have no associated values OR all associated values themselves are `Equatable`.

```swift
enum Status: Equatable {
    case success(message: String)
    case failure(code: Int)
}

let s1 = Status.success(message: "Done")
let s2 = Status.success(message: "Done")
print(s1 == s2) // true
```

## 2. Automatic Comparable Synthesis
Standard enums (those without associated values) can get automatic `Comparable` conformance if they also have `RawRepresentable` conformance with a comparable raw value (like `Int`).

```swift
enum Priority: Int, Comparable {
    case low = 0
    case medium = 1
    case high = 2

    static func < (lhs: Priority, rhs: Priority) -> Bool {
        return lhs.rawValue < rhs.rawValue
    }
}
```

## 3. Manual Implementation
If your associated values are not `Equatable`, or you want custom logic, you must implement the requirement manually.

```swift
enum Measurement: Equatable {
    case length(Double)
    case weight(Double)

    static func == (lhs: Measurement, rhs: Measurement) -> Bool {
        switch (lhs, rhs) {
        case (.length(let l), .length(let r)): return l == r
        case (.weight(let l), .weight(let r)): return l == r
        default: return false
        }
    }
}
```

## 4. Synthesized Comparable (Swift 5.3+)
Swift 5.3 introduced the ability to synthesize `Comparable` for enums that have no associated values, based on the order of their declaration.

```swift
enum Grade: Comparable {
    case f, d, c, b, a
}

print(Grade.a > Grade.f) // true
```

> [!IMPORTANT]
> When `Comparable` is synthesized, the comparison is based on the **source order** of cases. The case defined first is considered "less than" the cases defined later.
