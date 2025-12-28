---
id: 901
---
# Extracting Associated Values

Associated values are "wrapped" inside an enum instance. To use the data they contain, you must "unwrap" or extract them using pattern matching.

## 1. The `switch` Statement (Most common)
You can extract values as constants (`let`) or variables (`var`).

```swift
enum Task {
    case urgent(String)
    case routine(days: Int)
}

let myTask = Task.urgent("Fix the server")

switch myTask {
case .urgent(let description):
    print("Priority: \(description)")
case .routine(let days):
    print("Complete in \(days) days")
}
```

## 2. Shorthand Pattern Placement
If all values in a case are extracted in the same way, you can put the `let` or `var` before the case name.

```swift
switch myTask {
case let .urgent(description):
    print("Task: \(description)")
case let .routine(days):
    print("Days: \(days)")
}
```

## 3. Extracting with `if case let`
Use this when you only care about one specific case.

```swift
if case let .urgent(desc) = myTask {
    print("Dealing with urgent: \(desc)")
}
```

## 4. Extracting with `guard case let`
Useful for early exits in functions when a condition depends on an enum case.

```swift
func processUrgentTask(_ task: Task) {
    guard case let .urgent(description) = task else {
        return
    }
    print("Processing: \(description)")
}
```

## 5. Ignoring Values
Use the underscore `_` to ignore specific parts of the associated data.

```swift
enum DeepLink {
    case profile(id: Int, tab: String)
}

let link = DeepLink.profile(id: 123, tab: "settings")

if case let .profile(id, _) = link {
    print("Navigating to profile \(id), ignoring tab.")
}
```

> [!IMPORTANT]
> Associated values can only be accessed via pattern matching. You cannot access them using dot syntax like `task.description` unless you define a custom computed property that performs the extraction internally.
