---
id: 909
---
# Pattern Matching with Associated Values

Pattern matching is the primary mechanism for interacting with the data stored in an enum's associated values. Swift provides deep pattern matching capabilities that go beyond simple equality.

## 1. Single Value Extraction
The most basic form extracts a single associated value.

```swift
enum Media {
    case book(title: String)
    case movie(title: String, director: String)
}

let myMedia = Media.movie(title: "Inception", director: "Nolan")

switch myMedia {
case .book(let title):
    print("Reading \(title)")
case .movie(let title, let director):
    print("Watching \(title) by \(director)")
}
```

## 2. Using Underscores to Ignore Values
If you only need some of the associated values, use `_` to discard the rest.

```swift
switch myMedia {
case .movie(let title, _):
    print("Movie Title: \(title)")
default:
    break
}
```

## 3. Matching Specific Values
You can match only when an associated value equals a specific literal.

```swift
switch myMedia {
case .movie(title: "Inception", let director):
    print("Found Inception! Directed by \(director)")
case .movie(let title, let director):
    print("Other movie: \(title) by \(director)")
default:
    break
}
```

## 4. Nested Pattern Matching
You can even match patterns inside patterns if the associated values are themselves enums or tuples.

```swift
enum Status {
    case online, offline
}
enum User {
    case registered(id: Int, status: Status)
}

let user = User.registered(id: 1, status: .online)

switch user {
case .registered(_, .online):
    print("The user is currently online.")
case .registered(let id, .offline):
    print("User \(id) is offline.")
}
```

## 5. Control Flow with Patterns
Pattern matching isn't just for `switch`. It can be used in `for` loops, `if`, and `guard`.

```swift
let mediaList: [Media] = [.book(title: "Swift"), .movie(title: "Coco", director: "Unk")]

for case let .movie(title, _) in mediaList {
    print("Found a movie in the list: \(title)")
}
```

> [!TIP]
> When extracting multiple values, you can use `case let .movie(title, director)` instead of `case .movie(let title, let director)` for cleaner code.
