---
id: 897
---
# Enum Case Values (Distinct Cases)

In Swift, enumeration cases are distinct values in their own right. This distinguishes them from other languages where enums are often just wrappers around integers.

## 1. Type Safety
Because each case is a unique value of the enum type, the compiler can prevent you from providing an invalid value.

```swift
enum ConnectionState {
    case disconnected
    case connecting
    case connected
    case disconnecting
}

var currentStatus: ConnectionState = .connected
// currentStatus = 0 // Error: Cannot assign value of type 'Int' to type 'ConnectionState'
```

## 2. Memory Representation
Swift optimizes the memory footprint of enums based on their cases and associated values.

- **No Associated Values**: Usually represented by a single byte (tag) that identifies the case.
- **With Associated Values**: The size is determined by the largest associated value plus a small tag to identify the case.

## 3. The `case` Keyword
The `case` keyword introduces a new member of the enumeration.

```swift
enum Shape {
    case circle
    case square
    case triangle
}
```

## 4. Uniqueness
Even if two enums have cases with the same name, they are distinct because they belonging to different types.

```swift
enum FileStatus { case open, closed }
enum DoorStatus { case open, closed }

let file: FileStatus = .open
// let door: DoorStatus = file // Error: Different types
```

> [!NOTE]
> This uniqueness is what allows Swift enums to be used safely in large codebases without naming collisions between different domains.
