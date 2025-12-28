---
id: 1153
---
# Optional States

Under the hood, every Optional in Swift is an instance of the `Optional<Wrapped>` enumeration. This enum has exactly two states (cases).

## 1. The `.some(Wrapped)` State
This state represents the presence of a value. It "wraps" the actual value inside the enum case.

```swift
let name: String? = .some("Swift")
```
When you unwrap an optional, you are essentially extracting the data from the `.some` case.

## 2. The `.none` State
This state represents the absence of a value. This is what the `nil` keyword maps to.

```swift
let name: String? = .none
// name == nil // true
```

## 3. Why This Matters
Because optionals are enums, they follow the same rules as other value types:
- They can have methods.
- They are copied when passed around.
- They are type-safe.

## 4. Visual Anatomy
```mermaid
graph TD
    subgraph Optional[Optional<String>]
        direction TB
        S{State} --> SOME[.some]
        S --> NONE[.none]
        SOME --> V["Swift" (Value)]
        NONE --> N[Empty]
    end
```

## 5. Generic Nature
The `Optional` type is generic, meaning it can wrap any type `T`.
- `Optional<Int>`
- `Optional<UserAccount>`
- `Optional<[String]>`

> [!NOTE]
> Even though we usually use the syntax `T?` and `nil`, keeping the underlying enum structure in mind explains why we can use functional methods like `map` and `flatMap` on them.
