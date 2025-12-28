---
id: 45
---
# Mandatory Dependencies and Immutability

As a Senior iOS Engineer, one of your primary responsibilities is to ensure the **stability** and **thread-safety** of your code. Using DI to enforce mandatory dependencies and immutability is the most effective way to achieve this.

## 1. When to use Mandatory Dependencies
A dependency is mandatory if the class **cannot exist** or **cannot perform its basic function** without it.
-   **Example**: A `LoginViewModel` *must* have an `AuthService`. Without it, the class is useless.

### Enforcement via Initializer
By requiring mandatory dependencies in the `init` method, you use the Swift compiler to prevent "partial initialization" states.

```swift
class PaymentViewModel {
    init(service: PaymentService) { ... } // Compiler forces you to provide 'service'
}
```

## 2. The Power of Immutability (`let`)
When a dependency is mandatory, you should store it as a `let` constant.

### Benefits of Immutable Injection:
1.  **Thread Safety**: A constant can be read by multiple threads simultaneously without fear of it being swapped out or changed (No data races).
2.  **Predictability**: The object's behavior won't change after it has been created.
3.  **Local Reasoning**: When debugging, you don't have to wonder "Did someone change the API client in the middle of this function?"

```swift
class DataManager {
    // Immutable dependencies
    private let storage: Storage
    private let network: Network
    
    init(storage: Storage, network: Network) {
        self.storage = storage
        self.network = network
    }
}
```

## 3. Comparison with Optional Injection

| Feature | Mandatory (Initializer) | Optional (Property) |
| :--- | :--- | :--- |
| **Declaration** | `let` | `var` |
| **Availability** | Always | May be `nil` |
| **Swift Type** | Non-optional (`Service`) | Optional (`Service?`) |
| **Best For** | Core Logic / ViewModels | Delegates / Add-on features |

## Visualizing Lifecycle Stability
```mermaid
graph LR
    subgraph "Unstable Lifecycle (Optional)"
        C1[Create] --> U1[Use]
        U1 -.->|Dependency Swapped| U2[Unexpected behavior]
    end
    
    subgraph "Stable Lifecycle (Mandatory)"
        C2[Create + Inject Constants] --> U3[Use]
        U3 --> U4[Use]
        Note over C2, U4: Dependencies are locked
    end
```

## Summary
Immutability is a powerful feature of the Swift language. By using Initializer Injection for mandatory dependencies, you leverage the compiler to ensure that your objects are always correctly configured and thread-safe, significantly reducing the surface area for bugs.
