---
id: 43
---
# The Problem with Tight Coupling

Tight coupling is a software design flaw where components are highly dependent on each other's internal implementation details. Robert C. Martin (Uncle Bob) identified three major consequences of this: **Rigidity**, **Fragility**, and **Immobility**.

## 1. Rigidity
**Rigidity** occurs when a simple change in one part of the system forces a cascade of changes in other parts.
-   **Example**: You decide to change your database primary key from an `Int` to a `UUID`. Because every View Model is hard-coded to a concrete `Database` class, you now have to update 50 files instead of one.

## 2. Fragility
**Fragility** is the tendency of the software to break in many places every time it is changed. Often, these breaks happen in areas that seem completely unrelated to the change.
-   **Example**: You fix a bug in the `PaymentService` login logic. Suddenly, the `AnalyticsTracker` starts crashing because it was implicitly sharing a hidden state with the payment singleton.

## 3. Immobility
**Immobility** is the inability to reuse software from other projects or parts of the same project because of the internal dependencies.
-   **Example**: You want to move your beautiful `CustomChart` view into a new app. However, the chart has a hard link to `RealtimeNetworkFeed`. To reuse the chart, you'd have to drag the entire network layer and its dependencies into the new project.

## Coupling Matrix

| Characteristic | Tightly Coupled (Bad) | Loosely Coupled (Good) |
| :--- | :--- | :--- |
| **Change** | Cascades (Rigid) | Isolated (Flexible) |
| **Stability** | Brittleness (Fragile) | Robustness (Stable) |
| **Reuse** | Impossible (Immobile) | Easy (Portable) |
| **Unit Testing** | Integration only | True unit tests |

## Visualizing the Spiral of Decay
```mermaid
graph TD
    Change[Simple Feature Request] --> R[Rigidity: 10 files need updating]
    R --> F[Fragility: Unrelated bug appears in QA]
    F --> I[Immobility: "We can't reuse that code"]
    I --> Debt[Technical Debt Increases]
```

## How DI specifically addresses these:
-   **DI + Protocols** solve **Immobility** by allowing you to inject a mock or lightweight implementation in a new project.
-   **DI + Composition Root** solve **Rigidity** by centralizing all configuration changes.
-   **DI + Explicit Requirements** solve **Fragility** by eliminating hidden side-effects.

## Summary
Tight coupling is the enemy of long-term software health. As a Senior Engineer, your job is to recognize when a codebase is becoming rigid, fragile, or immobile and to use Dependency Injection to "cut" those ties, restoring the system's flexibility.
