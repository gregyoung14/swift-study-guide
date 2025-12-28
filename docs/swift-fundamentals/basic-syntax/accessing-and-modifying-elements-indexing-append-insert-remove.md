---
id: 731
---
﻿# Accessing and Modifying Elements (Indexing, Append, Insert, Remove)

## Overview

Arrays in Swift provide powerful and safe methods for accessing and modifying elements. This section covers indexing, appending, inserting, and removing elements with comprehensive examples and best practices for safe array manipulation.

## Table of Contents

- [Safe Indexing](#safe-indexing)
- [Appending Elements](#appending-elements)
- [Inserting Elements](#inserting-elements)
- [Removing Elements](#removing-elements)
- [Batch Operations](#batch-operations)
- [Performance Considerations](#performance-considerations)
- [Common Patterns](#common-patterns)

## Safe Indexing

### Basic Subscript Access

```swift
// Array declaration and basic access
var fruits = ["Apple", "Banana", "Orange", "Mango"]

// Access by index (0-based)
let firstFruit = fruits[0]      // "Apple"
let secondFruit = fruits[1]     // "Banana"
let lastFruit = fruits[3]       // "Mango"

// Modify by index
fruits[1] = "Pineapple"         // ["Apple", "Pineapple", "Orange", "Mango"]
fruits[2] = "Grape"             // ["Apple", "Pineapple", "Grape", "Mango"]

print(fruits) // ["Apple", "Pineapple", "Grape", "Mango"]
```

### Safe Array Access

```swift
// Avoid index out of bounds errors
extension Array {
    /// Safely access array elements
    subscript(safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}

// Usage
let safeFruits = ["Apple", "Banana", "Orange"]
let first = safeFruits[safe: 0]      // Optional("Apple")
let tenth = safeFruits[safe: 9]      // nil (safe!)
let negative = safeFruits[safe: -1]  // nil (safe!)

// Safe modification
if let index = safeFruits.firstIndex(of: "Banana") {
    safeFruits[index] = "Pineapple"  // Safe modification
}
```

### Negative Indexing

```swift
// Access from the end using negative indices
extension Array {
    /// Access elements from the end using negative indices
    subscript(backward index: Int) -> Element? {
        guard index < 0 else { return nil }
        let actualIndex = count + index
        return indices.contains(actualIndex) ? self[actualIndex] : nil
    }
}

let numbers = [10, 20, 30, 40, 50]
let last = numbers[backward: -1]      // Optional(50)
let secondLast = numbers[backward: -2] // Optional(40)
let tenthLast = numbers[backward: -10] // nil (out of bounds)

// Alternative: use endIndex
let lastElement = numbers[numbers.endIndex - 1]  // 50 (but unsafe if empty!)
```

### Range Access

```swift
// Access multiple elements using ranges
let colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]

// Closed range (inclusive)
let firstThree = colors[0...2]        // ["Red", "Green", "Blue"]
let middleThree = colors[1...3]       // ["Green", "Blue", "Yellow"]

// Half-open range (exclusive of end)
let firstTwo = colors[..<2]           // ["Red", "Green"]
let lastThree = colors[3..<6]         // ["Yellow", "Purple", "Orange"]

// One-sided ranges (Swift 4+)
let fromThird = colors[2...]          // ["Blue", "Yellow", "Purple", "Orange"]
let upToThird = colors[...2]          // ["Red", "Green", "Blue"]
let allButFirst = colors[1...]        // ["Green", "Blue", "Yellow", "Purple", "Orange"]
let allButLast = colors[..<5]         // ["Red", "Green", "Blue", "Yellow", "Purple"]

// Modify ranges
var mutableColors = colors
mutableColors[1...3] = ["Cyan", "Magenta"]  // ["Red", "Cyan", "Magenta", "Purple", "Orange"]
mutableColors[2...] = ["Black", "White"]    // ["Red", "Cyan", "Black", "White"]
```

## Appending Elements

### Single Element Append

```swift
// Append single elements
var shoppingList = ["Milk", "Bread"]

// Method 1: append(_:)
shoppingList.append("Butter")        // ["Milk", "Bread", "Butter"]

// Method 2: += operator
shoppingList += ["Eggs"]             // ["Milk", "Bread", "Butter", "Eggs"]

// Method 3: append(contentsOf:)
shoppingList.append(contentsOf: ["Cheese", "Yogurt"])  // ["Milk", "Bread", "Butter", "Eggs", "Cheese", "Yogurt"]

print(shoppingList)
```

### Multiple Elements Append

```swift
// Append multiple elements at once
var numbers = [1, 2, 3]

// Append array of elements
numbers.append(contentsOf: [4, 5, 6])  // [1, 2, 3, 4, 5, 6]

// Using += with array
numbers += [7, 8, 9]                  // [1, 2, 3, 4, 5, 6, 7, 8, 9]

// Functional approach
let moreNumbers = numbers + [10, 11, 12]  // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
// Note: + creates new array, doesn't modify original
```

### Conditional Append

```swift
// Append with conditions
var uniqueItems = ["Apple", "Banana"]
let newItem = "Orange"

// Only append if not already present
if !uniqueItems.contains(newItem) {
    uniqueItems.append(newItem)       // ["Apple", "Banana", "Orange"]
}

// Append with transformation
let scores = [85, 92, 78]
var gradeLetters: [String] = []

for score in scores {
    switch score {
    case 90...100: gradeLetters.append("A")
    case 80...89: gradeLetters.append("B")
    case 70...79: gradeLetters.append("C")
    default: gradeLetters.append("F")
    }
}
print(gradeLetters) // ["B", "A", "C"]
```

## Inserting Elements

### Insert at Specific Index

```swift
// Insert single element at index
var letters = ["A", "B", "D", "E"]

// Insert "C" at index 2
letters.insert("C", at: 2)            // ["A", "B", "C", "D", "E"]

// Insert at beginning
letters.insert("Z", at: 0)            // ["Z", "A", "B", "C", "D", "E"]

// Insert at end (same as append)
letters.insert("F", at: letters.endIndex)  // ["Z", "A", "B", "C", "D", "E", "F"]

print(letters)
```

### Insert Multiple Elements

```swift
// Insert multiple elements
var numbers = [1, 2, 5, 6]

// Insert [3, 4] starting at index 2
numbers.insert(contentsOf: [3, 4], at: 2)  // [1, 2, 3, 4, 5, 6]

// Insert at beginning
numbers.insert(contentsOf: [0], at: 0)     // [0, 1, 2, 3, 4, 5, 6]

// Insert at end
numbers.insert(contentsOf: [7, 8], at: numbers.endIndex)  // [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

### Safe Insertion

```swift
// Safe insertion with bounds checking
extension Array {
    /// Safely insert element at index
    mutating func safeInsert(_ element: Element, at index: Index) {
        guard index >= 0 && index <= count else {
            print("Index \(index) out of bounds for array of count \(count)")
            return
        }
        insert(element, at: index)
    }

    /// Safely insert multiple elements at index
    mutating func safeInsert(contentsOf elements: [Element], at index: Index) {
        guard index >= 0 && index <= count else {
            print("Index \(index) out of bounds for array of count \(count)")
            return
        }
        insert(contentsOf: elements, at: index)
    }
}

// Usage
var safeArray = [1, 2, 3]
safeArray.safeInsert(99, at: 1)           // [1, 99, 2, 3]
safeArray.safeInsert(100, at: 10)         // Prints warning, no insertion
safeArray.safeInsert(contentsOf: [4, 5], at: 4)  // [1, 99, 2, 3, 4, 5]
```

## Removing Elements

### Remove by Index

```swift
// Remove element at specific index
var names = ["Alice", "Bob", "Charlie", "David", "Eve"]

// Remove and return element at index
let removedName = names.remove(at: 2)     // removedName = "Charlie"
// names = ["Alice", "Bob", "David", "Eve"]

// Remove first element
let firstName = names.removeFirst()       // firstName = "Alice"
// names = ["Bob", "David", "Eve"]

// Remove last element
let lastName = names.removeLast()         // lastName = "Eve"
// names = ["Bob", "David"]

// Remove first N elements
names = ["Alice", "Bob", "Charlie", "David"]
let firstTwo = names.removeFirst(2)       // firstTwo = ["Alice", "Bob"]
// names = ["Charlie", "David"]

// Remove last N elements
let lastOne = names.removeLast(1)         // lastOne = ["David"]
// names = ["Charlie"]
```

### Remove by Value

```swift
// Remove specific values
var fruits = ["Apple", "Banana", "Orange", "Apple", "Grape"]

// Remove first occurrence of value
if let index = fruits.firstIndex(of: "Apple") {
    fruits.remove(at: index)              // ["Banana", "Orange", "Apple", "Grape"]
}

// Remove all occurrences
fruits.removeAll { $0 == "Apple" }        // ["Banana", "Orange", "Grape"]

// Remove all elements
fruits.removeAll()                        // []

// Alternative: filter out elements
let numbers = [1, 2, 3, 4, 5, 6]
let evenNumbers = numbers.filter { $0 % 2 == 0 }  // [2, 4, 6]
// Original array unchanged
```

### Conditional Removal

```swift
// Remove elements based on conditions
var scores = [85, 92, 78, 95, 88, 76]

// Remove failing scores (< 80)
scores.removeAll { $0 < 80 }              // [85, 92, 95, 88]

// Remove elements at specific indices
var items = ["A", "B", "C", "D", "E"]
let indicesToRemove = [1, 3]  // Remove "B" and "D"

// Sort indices in descending order to avoid index shifting
for index in indicesToRemove.sorted(by: >) {
    items.remove(at: index)
}
// items = ["A", "C", "E"]

// Remove duplicates while preserving order
var duplicates = [1, 2, 2, 3, 4, 3, 5]
var seen = Set<Element>()
duplicates.removeAll { !seen.insert($0).inserted }
// duplicates = [1, 2, 3, 4, 5]
```

## Batch Operations

### Bulk Modifications

```swift
// Multiple operations in sequence
var data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Chain operations
data.removeFirst(2)        // Remove first 2: [3, 4, 5, 6, 7, 8, 9, 10]
data.removeLast(2)         // Remove last 2: [3, 4, 5, 6, 7, 8]
data.insert(2.5, at: 1)    // Insert at position 1: [3, 2.5, 4, 5, 6, 7, 8]
data.append(9)             // Append: [3, 2.5, 4, 5, 6, 7, 8, 9]

print(data) // [3, 2.5, 4, 5, 6, 7, 8, 9]
```

### Replace Subranges

```swift
// Replace multiple elements at once
var colors = ["Red", "Green", "Blue", "Yellow"]

// Replace range with new elements
colors.replaceSubrange(1...2, with: ["Cyan", "Magenta", "Black"])
// colors = ["Red", "Cyan", "Magenta", "Black", "Yellow"]

// Replace with different number of elements
colors.replaceSubrange(0...1, with: ["White"])  // ["White", "Magenta", "Black", "Yellow"]

// Replace entire array
colors.replaceSubrange(colors.startIndex..<colors.endIndex, with: ["Rainbow"])
// colors = ["Rainbow"]
```

### Functional Transformations

```swift
// Transform arrays functionally
let original = [1, 2, 3, 4, 5]

// Create new arrays (non-destructive)
let doubled = original.map { $0 * 2 }           // [2, 4, 6, 8, 10]
let evens = original.filter { $0 % 2 == 0 }     // [2, 4]
let sum = original.reduce(0, +)                 // 15
let strings = original.map { String($0) }       // ["1", "2", "3", "4", "5"]

// Chain operations
let result = original
    .filter { $0 > 2 }                          // [3, 4, 5]
    .map { $0 * 10 }                            // [30, 40, 50]
    .sorted(by: >)                              // [50, 40, 30]

// Original array unchanged
print(original) // [1, 2, 3, 4, 5]
print(result)   // [50, 40, 30]
```

## Performance Considerations

### Time Complexity

```swift
// Array operation time complexities
/*
Operation       | Time Complexity | Notes
----------------|-----------------|--------
Access [index]  | O(1)           | Direct memory access
Append          | O(1) amortized | May require array reallocation
Insert(at:)     | O(n)           | Shifts elements after insertion point
Remove(at:)     | O(n)           | Shifts elements after removal point
RemoveFirst()   | O(n)           | Shifts all elements
RemoveLast()    | O(1)           | No element shifting needed
Contains        | O(n)           | Linear search
firstIndex(of:) | O(n)           | Linear search
sort()          | O(n log n)     | Efficient sorting algorithm
filter()        | O(n)           | Processes each element once
map()           | O(n)           | Processes each element once
*/
```

### Memory Management

```swift
// Array capacity and memory efficiency
var efficientArray: [Int] = []

// Reserve capacity to avoid reallocations
efficientArray.reserveCapacity(1000)

for i in 0..<1000 {
    efficientArray.append(i)
}
// Only one memory allocation needed

// Check capacity vs count
print("Count: \(efficientArray.count)")      // 1000
print("Capacity: \(efficientArray.capacity)") // >= 1000

// Shrink capacity if needed
efficientArray = Array(efficientArray)  // Creates new array with optimal capacity
```

### Optimization Patterns

```swift
// Optimize for performance
extension Array where Element: Equatable {

    // Fast removal of all occurrences
    mutating func removeAllFast(_ element: Element) {
        var writeIndex = 0
        for readIndex in 0..<count {
            if self[readIndex] != element {
                self[writeIndex] = self[readIndex]
                writeIndex += 1
            }
        }
        removeLast(count - writeIndex)
    }

    // Batch operations are more efficient
    mutating func removeElements(in indices: Set<Index>) {
        // Sort indices descending to avoid index shifting issues
        let sortedIndices = indices.sorted(by: >)
        for index in sortedIndices {
            remove(at: index)
        }
    }
}

// Usage
var largeArray = Array(0..<10000)
largeArray.removeAllFast(5000)  // Efficient removal

var indicesToRemove: Set<Int> = [100, 200, 300]
largeArray.removeElements(in: indicesToRemove)
```

## Common Patterns

### Stack Operations

```swift
// Array as stack (LIFO)
struct Stack<Element> {
    private var elements: [Element] = []

    mutating func push(_ element: Element) {
        elements.append(element)
    }

    mutating func pop() -> Element? {
        elements.popLast()
    }

    func peek() -> Element? {
        elements.last
    }

    var isEmpty: Bool {
        elements.isEmpty
    }

    var count: Int {
        elements.count
    }
}

// Usage
var stack = Stack<String>()
stack.push("First")
stack.push("Second")
stack.push("Third")

print(stack.pop())  // "Third"
print(stack.peek()) // "Second"
```

### Queue Operations

```swift
// Array as queue (FIFO) - less efficient but simple
struct SimpleQueue<Element> {
    private var elements: [Element] = []

    mutating func enqueue(_ element: Element) {
        elements.append(element)
    }

    mutating func dequeue() -> Element? {
        guard !elements.isEmpty else { return nil }
        return elements.removeFirst()  // O(n) operation
    }

    func peek() -> Element? {
        elements.first
    }

    var isEmpty: Bool {
        elements.isEmpty
    }
}

// More efficient queue using two arrays
struct EfficientQueue<Element> {
    private var enqueueStack: [Element] = []
    private var dequeueStack: [Element] = []

    mutating func enqueue(_ element: Element) {
        enqueueStack.append(element)
    }

    mutating func dequeue() -> Element? {
        if dequeueStack.isEmpty {
            dequeueStack = enqueueStack.reversed()
            enqueueStack.removeAll()
        }
        return dequeueStack.popLast()
    }

    func peek() -> Element? {
        dequeueStack.last ?? enqueueStack.first
    }

    var isEmpty: Bool {
        enqueueStack.isEmpty && dequeueStack.isEmpty
    }
}
```

### Circular Buffer

```swift
// Fixed-size circular buffer
struct CircularBuffer<Element> {
    private var buffer: [Element?]
    private var readIndex = 0
    private var writeIndex = 0
    private var count = 0
    private let capacity: Int

    init(capacity: Int) {
        self.capacity = capacity
        buffer = Array(repeating: nil, count: capacity)
    }

    mutating func write(_ element: Element) {
        buffer[writeIndex] = element
        writeIndex = (writeIndex + 1) % capacity

        if count < capacity {
            count += 1
        } else {
            readIndex = (readIndex + 1) % capacity  // Overwrite oldest
        }
    }

    mutating func read() -> Element? {
        guard count > 0 else { return nil }

        let element = buffer[readIndex]
        buffer[readIndex] = nil
        readIndex = (readIndex + 1) % capacity
        count -= 1

        return element
    }

    func peek() -> Element? {
        count > 0 ? buffer[readIndex] : nil
    }

    var isEmpty: Bool { count == 0 }
    var isFull: Bool { count == capacity }
    var availableSpace: Int { capacity - count }
}
```

### Summary

Swift arrays provide comprehensive methods for accessing and modifying elements:

**Safe Access:**
- Use `safe` subscripts to prevent crashes
- Check bounds with `indices.contains(index)`
- Use negative indexing for end-relative access

**Efficient Operations:**
- `append()` and `+=` for adding elements
- `insert(at:)` and `insert(contentsOf:at:)` for insertions
- `remove(at:)`, `removeFirst()`, `removeLast()` for removals
- Range operations for bulk modifications

**Performance Awareness:**
- `append()` is amortized O(1)
- Insert/remove operations are O(n)
- Reserve capacity for bulk insertions
- Use functional operations for transformations

**Common Patterns:**
- Stack operations using `append()` and `popLast()`
- Queue implementations with varying efficiency
- Circular buffers for fixed-size collections
- Safe access patterns to prevent runtime errors

These methods form the foundation for working with collections in Swift, enabling both safe and efficient array manipulations across a wide range of use cases.
