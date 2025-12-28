---
id: 1183
---
# Defining Protocols (`protocol MyProtocol { ... }`)

Defining a protocol is the first step in creating a modular, "Protocol-Oriented" architecture in Swift.

## 1. Basic Declaration
A protocol is declared using the `protocol` keyword followed by its name.

```swift
protocol Greetable {
    func sayHello()
}
```

## 2. Rules for Naming
- **UpperCamelCase**: Like all types in Swift.
- **Capability-Based**: Use suffixes like `-able`, `-ible`, or `-ing` (e.g., `Equatable`, `Convertible`, `Loading`).
- **Nouns**: Use nouns if the protocol describes "what something is" (e.g., `Collection`, `Iterator`).

## 3. Protocol Content
Inside a protocol, you define the "signatures" of requirements. You **do not** provide implementations (except in extensions).

- **Properties**: Name and type + `{ get }` or `{ get set }`.
- **Methods**: Name, parameters, and return type.
- **Initializers**: Full initializer signature.
- **Associated Types**: Placeholder generic types.

## 4. No Storage
A protocol cannot store data. It only describes the interface.

```swift
protocol Player {
    // var score: Int = 0 // ERROR: Protocols cannot have stored properties
    var score: Int { get set } // VALID: Requirement for a property
}
```

## 5. Example Blueprint
```swift
protocol Vehicle {
    var brand: String { get }
    var engineState: Bool { get set }
    func startEngine()
    func stopEngine()
    init(brand: String)
}
```

> [!TIP]
> Keep your protocols small. A protocol with 20 methods is often a sign that it should be broken into 5 smaller, more specific protocols.
