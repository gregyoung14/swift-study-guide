---
id: 1197
---
# Protocol As a Type

In Swift, protocols are first-class citizens. This means a protocol is not just a list of requirements; it's a type itself. You can use a protocol in many places where you would use any other type, such as a variable type, a function parameter, or a return type.

## Using Protocols as Types

When you use a protocol as a type, you are using it as an **existential type**. This allows for polymorphism, where a single variable or parameter can hold any instance of any type that conforms to that protocol.

### Variables and Constants
```swift
protocol Animal {
    func makeNoise()
}

struct Dog: Animal { func makeNoise() { print("Woof!") } }
struct Cat: Animal { func makeNoise() { print("Meow!") } }

let myPet: Animal = Dog() // The type of myPet is 'Animal'
myPet.makeNoise()
```

### Function Parameters and Return Types
```swift
func greet(pet: Animal) {
    print("The animal says: ")
    pet.makeNoise()
}

func getPet() -> Animal {
    return Cat()
}
```

### Collections of Protocols
You can create arrays or dictionaries that store types conforming to a specific protocol.

```swift
let zoo: [Animal] = [Dog(), Cat(), Dog()]
for animal in zoo {
    animal.makeNoise()
}
```

## Protocol Types vs. Concrete Types

| Feature | Concrete Type (e.g., `Dog`) | Protocol Type (e.g., `Animal`) |
| :--- | :--- | :--- |
| **Flexibility** | Limited to that type | Any conforming type |
| **Performance** | High (Direct dispatch) | Lower (Witness tables/dynamic dispatch) |
| **Member Access** | All members of `Dog` | Only members defined in `Animal` |

## Casting and Type Checking

When you have a value of a protocol type, you might need to check its underlying concrete type or cast it back to use specific functionality.

*   **`is`**: Check if a value is of a certain type.
*   **`as?`**: Attempt a conditional downcast (returns an optional).
*   **`as!`**: Force a downcast (crashes if it fails).

```swift
for animal in zoo {
    if let dog = animal as? Dog {
        print("This is specifically a dog.")
    }
}
```

## Limitations and The `any` Keyword

Since Swift 5.6, it is encouraged (and often required) to use the `any` keyword when using a protocol as a type. This makes it explicit that you are using an existential type rather than a concrete type.

```swift
let myAnimal: any Animal = Dog()
```

### Protocols with Associated Types (PATs)
Prior to Swift 5.7, protocols with associated types or `Self` requirements could **not** be used as types. With the introduction of `any Protocol`, many of these can now be used as types, although with some limitations (e.g., you can't access members that return an associated type).

## Best Practices

*   **Use protocol types to decouple your code.** Instead of depending on concrete implementations, depend on protocols to make your code more testable and modular.
*   **Use `any` explicitly** to differentiate between existential types and generics (which use `some` or generic parameters).
*   **Favor generics (`T: Protocol`) over protocol types (`any Protocol`)** for performance-critical code, as generics use static dispatch.

---

> [!TIP]
> Protocols as types are the foundation of the **Delegation Pattern** in iOS, where a `delegate` property is typed as a protocol (e.g., `var delegate: (any MyDelegate)?`).
