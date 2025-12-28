---
id: 904
---
# Initializing from Raw Values (`init?(rawValue:)`)

When an enum conforms to `RawRepresentable` (which it does automatically if you give it a raw value type), Swift provides a built-in failable initializer: `init?(rawValue:)`.

## 1. How it Works
This initializer takes a value of the enum's raw value type and attempts to find a matching case. If a match is found, it returns that case; otherwise, it returns `nil`.

```swift
enum Planet: Int {
    case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
}

let earth = Planet(rawValue: 3) // Optional(Planet.earth)
let planetX = Planet(rawValue: 10) // nil
```

## 2. Handling the Result
Since the result is an optional, you should use `if let` or `guard` to safely unwrap it.

```swift
let input = 5
if let planet = Planet(rawValue: input) {
    print("Welcome to \(planet)")
} else {
    print("Planet not found.")
}
```

## 3. Overriding `init(rawValue:)`
While rarely needed, you can override this behavior if you need custom mapping logic. This is essentially what happens when you manually conform to `RawRepresentable`.

```swift
enum Day: Int {
    case mon = 1, tue, wed, thu, fri, sat, sun

    // Custom logic could go here if manually conforming
}
```

## 4. Use Cases
- **Data Parsing**: Converting integer codes from a JSON API into type-safe enums.
- **User Input**: Mapping menu index numbers to internal application states.
- **Persistence**: Reconstructing an enum instance after reading its raw value from `UserDefaults`.

> [!IMPORTANT]
> The `init?(rawValue:)` initializer is always **failable**. Even if you think you've covered all values, you must handle the case where the raw value doesn't map to a member of the enum.
