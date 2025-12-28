---
id: 1203
---
﻿# Protocol Types in Collections

In Swift, you can store multiple different types in a single collection if all those types conform to the same protocol. This is one of the most powerful uses of protocols as types, enabling **heterogeneous collections**.

## How It Works

By typing a collection as a protocol (e.g., `[any MyProtocol]`), you create a container that can hold any concrete instance that satisfies the protocol's requirements.

### Example: A List of Media Items
```swift
protocol MediaItem {
    var title: String { get }
    func play()
}

struct Song: MediaItem {
    let title: String
    func play() { print("Playing song: \(title)") }
}

struct Movie: MediaItem {
    let title: String
    func play() { print("Playing movie: \(title)") }
}

// Heterogeneous collection
let library: [any MediaItem] = [
    Song(title: "Shake It Off"),
    Movie(title: "Inception"),
    Song(title: "Bohemian Rhapsody")
]
```

## Accessing Members

When you iterate over a collection of protocol types, you only have access to the properties and methods defined in that protocol.

```swift
for item in library {
    print("Item: \(item.title)")
    item.play()
    // item.artist // Error: artist is not a member of MediaItem
}
```

## Filtering and Type Casting

If you need to perform actions specific to a concrete type within the collection, you can use type casting (`as?` or `as!`).

```swift
let songsOnly = library.compactMap { $0 as? Song }
for song in songsOnly {
    print("Found a song by \(song.title)")
}
```

## Performance Considerations

*   **Existential Boxing**: Storing protocol types involves "boxing" the values in an existential container. This allows the compiler to handle types of different sizes but introduces a small performance overhead compared to collections of a single concrete type.
*   **Dynamic Dispatch**: Methods called on protocol types in a collection use dynamic dispatch (witness tables), which is slightly slower than static dispatch used for concrete types.

## When to Use Protocol Collections

1.  **UI Components**: Storing a list of different views that all conform to a common layout protocol.
2.  **Plugin Architectures**: Maintaining a list of active plugins or modules that conform to a `Plugin` interface.
3.  **Command Pattern**: Keeping a queue of diverse command objects that all conform to a `Command` protocol.

## Best Practices

*   **Use `any`** for readability when declaring collections of protocols (e.g., `var observers: [any NetworkObserver]`).
*   **Avoid over-casting.** If you find yourself constantly casting items in a collection back to their concrete types, consider if you should use a more specific protocol or an enum with associated values instead.
*   **Prefer generics for single-type collections.** If a collection will only ever hold *one* type (even if that type is a protocol conformer), use generics `[T]` where `T: MyProtocol` for better performance.

---

> [!TIP]
> Protocols with associated types (PATs) can be used in collections since Swift 5.7 using the `any` keyword (e.g., `[any Identifiable]`).

