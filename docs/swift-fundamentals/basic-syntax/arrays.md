---
id: 734
---
﻿# Arrays

## Overview

Arrays in Swift are ordered collections that store multiple values of the same type. They provide efficient access to elements by index and support a wide range of operations for data manipulation. This section covers array fundamentals, creation, manipulation, and best practices.

## Table of Contents

- [Array Fundamentals](#array-fundamentals)
- [Creating Arrays](#creating-arrays)
- [Array Types and Generics](#array-types-and-generics)
- [Array Operations](#array-operations)
- [Multi-dimensional Arrays](#multi-dimensional-arrays)
- [Array Performance](#array-performance)
- [Common Patterns](#common-patterns)
- [Best Practices](#best-practices)

## Array Fundamentals

### What is an Array?

```swift
// Arrays are ordered collections of values of the same type
let numbers: [Int] = [1, 2, 3, 4, 5]        // Array of integers
let fruits: [String] = ["Apple", "Banana"]   // Array of strings
let coordinates: [(Double, Double)] = [(0, 0), (1, 1), (2, 2)] // Array of tuples

// Arrays maintain order and allow duplicate values
let duplicates = [1, 2, 2, 3, 3, 3]         // [1, 2, 2, 3, 3, 3]
let ordered = [3, 1, 4, 1, 5]               // Order is preserved: [3, 1, 4, 1, 5]

// Empty arrays
let emptyInts: [Int] = []
let emptyStrings: [String] = []
let emptyArray = [String]()                  // Type inferred as [String]
```

### Array Characteristics

```swift
// Arrays are value types (copied when assigned or passed)
var original = [1, 2, 3]
var copy = original        // Creates a copy
copy[0] = 99              // Modifies copy only
print(original)            // [1, 2, 3] (unchanged)
print(copy)                // [99, 2, 3]

// Arrays are mutable by default when declared with var
var mutableArray = [1, 2, 3]
mutableArray.append(4)     // OK
mutableArray[0] = 0        // OK

// Arrays are immutable when declared with let
let immutableArray = [1, 2, 3]
// immutableArray.append(4)  // Error: Cannot modify immutable array
// immutableArray[0] = 0     // Error: Cannot modify immutable array

// Arrays can contain any type that conforms to the element type
protocol Shape {
    var area: Double { get }
}

struct Circle: Shape {
    let radius: Double
    var area: Double { .pi * radius * radius }
}

struct Square: Shape {
    let side: Double
    var area: Double { side * side }
}

let shapes: [Shape] = [Circle(radius: 5), Square(side: 4)]
let areas = shapes.map { $0.area }  // [78.53981633974483, 16.0]
```

## Creating Arrays

### Array Literals

```swift
// Creating arrays with literals
let emptyArray: [Int] = []                    // Empty array
let numbers = [1, 2, 3, 4, 5]                // Array literal
let strings = ["Hello", "World"]              // String array
let mixed = [1, 2, 3] as [Double]             // Type casting

// Arrays can be created from ranges
let rangeArray = Array(1...5)                 // [1, 2, 3, 4, 5]
let strideArray = Array(stride(from: 0, to: 10, by: 2)) // [0, 2, 4, 6, 8]

// Creating arrays with repeated values
let zeros = Array(repeating: 0, count: 5)     // [0, 0, 0, 0, 0]
let greeting = Array(repeating: "Hello", count: 3) // ["Hello", "Hello", "Hello"]

// Creating arrays from other sequences
let stringArray = Array("Hello")              // ["H", "e", "l", "l", "o"]
let setToArray = Array(Set([1, 2, 3, 4]))    // Order not guaranteed
let dictionaryKeys = Array(["a": 1, "b": 2].keys) // ["a", "b"] (order not guaranteed)
```

### Initializers and Constructors

```swift
// Using Array initializers
let empty1 = [Int]()                          // Empty array of Int
let empty2 = Array<Int>()                     // Same as above
let empty3 = Array(repeating: 0, count: 0)    // Empty array

// Creating arrays from sequences
let fromRange = Array(1..<6)                  // [1, 2, 3, 4, 5]
let fromStride = Array(stride(from: 10, through: 50, by: 10)) // [10, 20, 30, 40, 50]

// Creating arrays from collections
let slice = [1, 2, 3, 4, 5][1...3]           // ArraySlice [2, 3, 4]
let arrayFromSlice = Array(slice)             // [2, 3, 4]

// Creating arrays with computed values
let squares = Array((1...5).map { $0 * $0 })  // [1, 4, 9, 16, 25]
let evenNumbers = Array((1...10).filter { $0 % 2 == 0 }) // [2, 4, 6, 8, 10]

// Unsafe buffer pointer (advanced, use with caution)
let bytes: [UInt8] = [0x48, 0x65, 0x6C, 0x6C, 0x6F] // "Hello" in ASCII
let buffer = UnsafeBufferPointer(start: bytes, count: bytes.count)
let arrayFromBuffer = Array(buffer)           // [72, 101, 108, 108, 111]
```

### Type Inference

```swift
// Swift infers array types from context
let inferredEmpty = []                        // Error: Cannot infer type
let inferredNumbers = [1, 2, 3]              // [Int]
let inferredStrings = ["a", "b", "c"]         // [String]
let inferredMixed = [1, 2.0, "three"]        // Error: Mixed types not allowed

// Explicit type annotation when needed
let explicitInts: [Int] = []                  // Empty array with explicit type
let explicitDoubles: [Double] = [1, 2, 3]     // Explicit type overrides inference

// Type inference with complex types
let tuples = [(1, "one"), (2, "two")]         // [(Int, String)]
let optionals = [Optional(1), nil, Optional(3)] // [Int?]
let functions = [{ $0 * 2 }, { $0 + 1 }]      // [(Int) -> Int]

// Context matters for inference
func processNumbers(_ numbers: [Int]) { }
processNumbers([1, 2, 3])                     // Infers [Int] from parameter type

let ambiguous = [1, 2, 3]
// ambiguous.map { $0.description }             // Infers String return type
// ambiguous.reduce(0, +)                       // Infers Int return type
```

## Array Types and Generics

### Generic Array Type

```swift
// Array<Element> is the full generic type
let numbers: Array<Int> = [1, 2, 3]           // Full form
let strings: [String] = ["a", "b", "c"]       // Shorthand form (preferred)

// Both are equivalent
func processArray(_ array: Array<Int>) { }     // Full form
func processArray(_ array: [Int]) { }          // Shorthand form

// Arrays can contain any type
struct Person {
    let name: String
    let age: Int
}

let people: [Person] = [
    Person(name: "Alice", age: 25),
    Person(name: "Bob", age: 30)
]

// Arrays of protocols
protocol Drawable {
    func draw()
}

let drawables: [Drawable] = [Circle(), Square()]

// Arrays of optionals
let optionalInts: [Int?] = [1, nil, 3, nil, 5]

// Arrays of functions
let operations: [(Int, Int) -> Int] = [{ $0 + $1 }, { $0 - $1 }, { $0 * $1 }]
let results = operations.map { $0(10, 5) }    // [15, 5, 50]
```

### Array Type Constraints

```swift
// Arrays work with any element type
let anyArray: [Any] = [1, "hello", true, [1, 2, 3]]

// But lose type safety
if let number = anyArray[0] as? Int {
    print("Number: \(number)")                 // 1
}

// Generic constraints
func findFirst<T: Equatable>(_ array: [T], matching element: T) -> Int? {
    return array.firstIndex(of: element)
}

let strings = ["a", "b", "c"]
let index = findFirst(strings, matching: "b")  // Optional(1)

// Arrays of hashable elements can be converted to sets
let numbers = [1, 2, 3, 2, 1]
let uniqueNumbers = Array(Set(numbers))        // [1, 2, 3] (order not preserved)

// Arrays of comparable elements can be sorted
let unsorted = [3, 1, 4, 1, 5]
let sorted = unsorted.sorted()                 // [1, 1, 3, 4, 5]
```

### Nested Arrays

```swift
// Arrays can contain other arrays
let matrix: [[Int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

// Accessing nested elements
let firstRow = matrix[0]                       // [1, 2, 3]
let firstElement = matrix[0][0]                // 1

// Creating jagged arrays (arrays of different lengths)
let jagged: [[Int]] = [
    [1, 2],
    [3, 4, 5, 6],
    [7]
]

// Flattening nested arrays
let flattened = matrix.flatMap { $0 }          // [1, 2, 3, 4, 5, 6, 7, 8, 9]
let reallyFlattened = matrix.flatMap { $0 }.flatMap { [$0] } // Same result

// Creating arrays of arrays programmatically
let grid = (0..<3).map { row in
    (0..<4).map { col in
        row * 4 + col
    }
}
// [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

## Array Operations

### Mutation Operations

```swift
// Modifying arrays (requires var declaration)
var mutableArray = [1, 2, 3]

// Adding elements
mutableArray.append(4)                         // [1, 2, 3, 4]
mutableArray.insert(0, at: 0)                  // [0, 1, 2, 3, 4]
mutableArray.insert(contentsOf: [10, 11], at: 2) // [0, 1, 10, 11, 2, 3, 4]

// Removing elements
let removed = mutableArray.remove(at: 2)       // removed = 10, array = [0, 1, 11, 2, 3, 4]
let last = mutableArray.removeLast()           // last = 4, array = [0, 1, 11, 2, 3]
let first = mutableArray.removeFirst()         // first = 0, array = [1, 11, 2, 3]

mutableArray.removeFirst(2)                    // Remove first 2: [2, 3]
mutableArray.removeLast(1)                     // Remove last 1: [2]

// Replacing elements
mutableArray[0] = 100                          // [100, 3]
mutableArray.replaceSubrange(0...1, with: [200, 300, 400]) // [200, 300, 400]

// Bulk operations
mutableArray.removeAll()                       // []
mutableArray = [1, 2, 3, 4, 5]
mutableArray.removeAll { $0 % 2 == 0 }         // Remove evens: [1, 3, 5]
```

### Non-Mutating Operations

```swift
// Operations that return new arrays (work with let arrays)
let original = [1, 2, 3, 4, 5]

// Filtering
let evens = original.filter { $0 % 2 == 0 }    // [2, 4]
let greaterThan3 = original.filter { $0 > 3 }  // [4, 5]

// Mapping (transforming)
let doubled = original.map { $0 * 2 }          // [2, 4, 6, 8, 10]
let strings = original.map { String($0) }      // ["1", "2", "3", "4", "5"]
let descriptions = original.map { "Number: \($0)" } // ["Number: 1", ...]

// Reducing (combining)
let sum = original.reduce(0, +)                // 15
let product = original.reduce(1, *)            // 120
let concatenated = original.reduce("") { $0 + String($1) } // "12345"

// Sorting
let ascending = original.sorted()               // [1, 2, 3, 4, 5]
let descending = original.sorted(by: >)        // [5, 4, 3, 2, 1]

// Reversing
let reversed = original.reversed()              // ReversedCollection [5, 4, 3, 2, 1]
let reversedArray = Array(reversed)             // [5, 4, 3, 2, 1]

// Shuffling
let shuffled = original.shuffled()              // Random order each time

// Prefix and suffix
let firstThree = original.prefix(3)             // [1, 2, 3]
let lastTwo = original.suffix(2)                // [4, 5]
let upTo4 = original.prefix(while: { $0 < 4 }) // [1, 2, 3]
let from3 = original.drop(while: { $0 < 3 })   // [3, 4, 5]
```

### Combining Arrays

```swift
// Joining arrays
let array1 = [1, 2, 3]
let array2 = [4, 5, 6]
let array3 = [7, 8, 9]

// Concatenation
let combined = array1 + array2 + array3        // [1, 2, 3, 4, 5, 6, 7, 8, 9]

// Appending arrays
var mutable = [1, 2, 3]
mutable.append(contentsOf: [4, 5, 6])         // [1, 2, 3, 4, 5, 6]

// Joining with separators
let words = ["Hello", "world", "from", "Swift"]
let sentence = words.joined(separator: " ")    // "Hello world from Swift"
let path = ["Users", "john", "Documents"].joined(separator: "/") // "Users/john/Documents"

// Zipping arrays
let names = ["Alice", "Bob", "Charlie"]
let ages = [25, 30, 35]
let zipped = zip(names, ages)                 // Zip2Sequence
let paired = Array(zipped)                     // [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

// Uneven arrays are truncated to shortest
let longNames = ["Alice", "Bob", "Charlie", "Diana"]
let shortAges = [25, 30]
let shortZipped = Array(zip(longNames, shortAges)) // [("Alice", 25), ("Bob", 30)]
```

## Multi-dimensional Arrays

### 2D Arrays (Matrices)

```swift
// Creating 2D arrays
let matrix3x3: [[Int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

// Accessing elements
let topLeft = matrix3x3[0][0]                  // 1
let middle = matrix3x3[1][1]                   // 5
let bottomRight = matrix3x3[2][2]              // 9

// Iterating over 2D arrays
for (rowIndex, row) in matrix3x3.enumerated() {
    for (colIndex, value) in row.enumerated() {
        print("[\(rowIndex)][\(colIndex)] = \(value)")
    }
}

// Creating matrices programmatically
func createIdentityMatrix(size: Int) -> [[Int]] {
    return (0..<size).map { row in
        (0..<size).map { col in
            row == col ? 1 : 0
        }
    }
}

let identity3x3 = createIdentityMatrix(size: 3)
// [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

// Matrix operations
func addMatrices(_ a: [[Int]], _ b: [[Int]]) -> [[Int]] {
    return zip(a, b).map { zip($0, $1).map(+) }
}

let matrixA = [[1, 2], [3, 4]]
let matrixB = [[5, 6], [7, 8]]
let sum = addMatrices(matrixA, matrixB)       // [[6, 8], [10, 12]]
```

### 3D Arrays and Higher Dimensions

```swift
// 3D arrays (cubes)
let cube: [[[Int]]] = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

// Accessing 3D elements
let element = cube[0][1][0]                    // 3

// Creating 3D arrays
func create3DArray(depth: Int, rows: Int, cols: Int) -> [[[Int]]] {
    return (0..<depth).map { _ in
        (0..<rows).map { _ in
            Array(0..<cols)
        }
    }
}

let array3D = create3DArray(depth: 2, rows: 3, cols: 4)
// [[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]]

// Iterating over 3D arrays
for (depthIndex, layer) in array3D.enumerated() {
    for (rowIndex, row) in layer.enumerated() {
        for (colIndex, value) in row.enumerated() {
            print("[\(depthIndex)][\(rowIndex)][\(colIndex)] = \(value)")
        }
    }
}
```

### Jagged Arrays

```swift
// Arrays of arrays with different lengths
let jaggedArray: [[Int]] = [
    [1, 2, 3, 4, 5],         // 5 elements
    [10, 20],                 // 2 elements
    [100, 200, 300, 400]     // 4 elements
]

// Safe access with bounds checking
func safeAccess(_ array: [[Int]], row: Int, col: Int) -> Int? {
    guard array.indices.contains(row) else { return nil }
    let rowArray = array[row]
    guard rowArray.indices.contains(col) else { return nil }
    return rowArray[col]
}

let value1 = safeAccess(jaggedArray, row: 0, col: 2)  // Optional(3)
let value2 = safeAccess(jaggedArray, row: 1, col: 3)  // nil (out of bounds)
let value3 = safeAccess(jaggedArray, row: 3, col: 0)  // nil (row out of bounds)

// Finding dimensions
let rowCount = jaggedArray.count
let columnCounts = jaggedArray.map { $0.count }     // [5, 2, 4]
let maxColumns = columnCounts.max() ?? 0            // 5
let totalElements = jaggedArray.flatMap { $0 }.count // 11
```

## Array Performance

### Time Complexity

```swift
// Array operation performance characteristics
/*
Operation       | Time Complexity | Notes
----------------|-----------------|--------
Access [index]  | O(1)           | Direct memory access
Append          | O(1) amortized | May trigger reallocation
Insert(at:)     | O(n)           | Elements shifted right
Remove(at:)     | O(n)           | Elements shifted left
first/last      | O(1)           | Direct access
count           | O(1)           | Stored property
isEmpty         | O(1)           | Derived from count
contains        | O(n)           | Linear search
firstIndex      | O(n)           | Linear search
filter          | O(n)           | Process each element
map             | O(n)           | Process each element
sort            | O(n log n)     | Efficient sorting
reverse         | O(n)           | Create reversed copy
*/

// Performance optimization example
var array = [Int]()

// Pre-allocating capacity improves performance
array.reserveCapacity(10000)

for i in 0..<10000 {
    array.append(i)  // No reallocations needed
}

// Compare with no capacity reservation
var slowArray = [Int]()
for i in 0..<10000 {
    slowArray.append(i)  // May trigger multiple reallocations
}
```

### Memory Layout

```swift
// Arrays store elements contiguously in memory
let numbers = [1, 2, 3, 4, 5]
// Memory: [1][2][3][4][5] (contiguous block)

// Copy-on-write optimization
var original = Array(1...1000)
var copy = original        // No actual copying yet

// Only when modified does the copy occur
copy[0] = 999             // Now copy is created
print(original[0])        // Still 1 (original unchanged)

// Memory efficiency with large arrays
let largeArray = Array(0..<1000000)
// Efficient storage of 1M elements

// Value types vs Reference types in arrays
struct Point {
    var x, y: Double
}

class Person {
    var name: String
    init(name: String) { self.name = String }
}

let points = [Point(x: 0, y: 0), Point(x: 1, y: 1)]    // Value types copied
let people = [Person(name: "Alice"), Person(name: "Bob")] // References stored

// Memory implications:
// - points: Stores actual Point structs (efficient)
// - people: Stores references to Person objects (reference counting overhead)
```

### Optimization Techniques

```swift
// Array optimization patterns
extension Array {
    // Efficient bulk operations
    mutating func removeElements(in indices: Set<Index>) {
        // Sort descending to avoid index shifting
        let sortedIndices = indices.sorted(by: >)
        for index in sortedIndices {
            remove(at: index)
        }
    }

    // In-place transformation (avoids creating new array)
    mutating func transformInPlace(_ transform: (Element) -> Element) {
        for index in indices {
            self[index] = transform(self[index])
        }
    }

    // Lazy operations for memory efficiency
    func lazyFilter(_ predicate: @escaping (Element) -> Bool) -> LazyFilterSequence<Self> {
        return lazy.filter(predicate)
    }

    func lazyMap<T>(_ transform: @escaping (Element) -> T) -> LazyMapSequence<Self, T> {
        return lazy.map(transform)
    }
}

// Usage examples
var data = Array(1...100)

// Efficient bulk removal
let indicesToRemove: Set<Int> = [10, 20, 30, 40]
data.removeElements(in: indicesToRemove)

// In-place transformation
data.transformInPlace { $0 * 2 }

// Lazy operations
let result = data.lazyFilter { $0 > 50 }.lazyMap { $0.description }.prefix(5)
let finalResult = Array(result)  // Only computed when needed
```

## Common Patterns

### Stack Implementation

```swift
// Array-based stack (LIFO)
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

    func isEmpty() -> Bool {
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
print(stack.count)  // 2
```

### Queue Implementation

```swift
// Array-based queue (FIFO)
struct Queue<Element> {
    private var elements: [Element] = []

    mutating func enqueue(_ element: Element) {
        elements.append(element)
    }

    mutating func dequeue() -> Element? {
        elements.isEmpty ? nil : elements.removeFirst()
    }

    func peek() -> Element? {
        elements.first
    }

    func isEmpty() -> Bool {
        elements.isEmpty
    }

    var count: Int {
        elements.count
    }
}

// Usage
var queue = Queue<String>()
queue.enqueue("First")
queue.enqueue("Second")
queue.enqueue("Third")

print(queue.dequeue())  // "First"
print(queue.peek())     // "Second"
print(queue.count)      // 2
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

### Array Builders

```swift
// Functional array construction
@resultBuilder
struct ArrayBuilder<Element> {
    static func buildBlock(_ components: Element...) -> [Element] {
        Array(components)
    }

    static func buildOptional(_ component: Element?) -> [Element] {
        component.map { [$0] } ?? []
    }

    static func buildEither(first component: Element) -> [Element] {
        [component]
    }

    static func buildEither(second component: Element) -> [Element] {
        [component]
    }

    static func buildArray(_ components: [Element]) -> [Element] {
        components
    }
}

@ArrayBuilder<String>
func buildMenu(allowAdvanced: Bool) -> [String] {
    "File"
    "Edit"
    "View"

    if allowAdvanced {
        "Tools"
        "Advanced"
    }
}

let basicMenu = buildMenu(allowAdvanced: false)     // ["File", "Edit", "View"]
let advancedMenu = buildMenu(allowAdvanced: true)  // ["File", "Edit", "View", "Tools", "Advanced"]
```

## Best Practices

### Choosing the Right Array Type

```swift
// Different array types for different needs

// Regular Array for general use
let generalArray = [1, 2, 3, 4, 5]

// ContiguousArray for performance-critical code (guaranteed contiguous storage)
let contiguousArray = ContiguousArray([1, 2, 3, 4, 5])

// ArraySlice for temporary views (zero-cost substrings)
let fullArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let slice = fullArray[2...6]  // ArraySlice [3, 4, 5, 6, 7]

// Lazy sequences for memory efficiency
let lazyFiltered = fullArray.lazy.filter { $0 % 2 == 0 }.map { $0 * 2 }
// No computation until accessed
let result = Array(lazyFiltered.prefix(3))  // Only computes first 3 results
```

### Memory Management

```swift
// Proper memory management with arrays
class DataProcessor {
    private var largeDataset: [DataPoint] = []

    func loadLargeDataset() {
        // Reserve capacity to avoid reallocations
        largeDataset.reserveCapacity(100000)

        for i in 0..<100000 {
            largeDataset.append(DataPoint(value: Double(i)))
        }
    }

    func processInBatches(batchSize: Int) -> [[DataPoint]] {
        // Process in chunks to manage memory
        return stride(from: 0, to: largeDataset.count, by: batchSize).map { startIndex in
            let endIndex = min(startIndex + batchSize, largeDataset.count)
            return Array(largeDataset[startIndex..<endIndex])
        }
    }

    func clearData() {
        // Explicitly clear large arrays
        largeDataset.removeAll(keepingCapacity: false)
    }
}

// Avoiding retain cycles with arrays
class NetworkManager {
    private var completionHandlers: [() -> Void] = []

    func addCompletionHandler(_ handler: @escaping () -> Void) {
        completionHandlers.append(handler)
    }

    func executeHandlers() {
        let handlers = completionHandlers
        completionHandlers.removeAll()  // Clear before executing to prevent re-entrance

        for handler in handlers {
            handler()
        }
    }
}
```

### Error Handling

```swift
// Safe array operations with error handling
extension Array {
    /// Safely access element at index
    func safeGet(at index: Index) -> Element? {
        guard indices.contains(index) else {
            print("Index \(index) out of bounds for array of count \(count)")
            return nil
        }
        return self[index]
    }

    /// Safely insert element with bounds checking
    mutating func safeInsert(_ element: Element, at index: Index) -> Bool {
        guard index >= 0 && index <= count else {
            print("Cannot insert at index \(index) in array of count \(count)")
            return false
        }
        insert(element, at: index)
        return true
    }

    /// Safely remove element with bounds checking
    mutating func safeRemove(at index: Index) -> Element? {
        guard indices.contains(index) else {
            print("Cannot remove at index \(index) in array of count \(count)")
            return nil
        }
        return remove(at: index)
    }
}

// Usage with error handling
var safeArray = [1, 2, 3, 4, 5]

// Safe access
if let value = safeArray.safeGet(at: 10) {
    print("Value: \(value)")
} else {
    print("Index out of bounds")
}

// Safe insertion
let inserted = safeArray.safeInsert(99, at: 2)  // true
let failedInsert = safeArray.safeInsert(100, at: 10)  // false

// Safe removal
if let removed = safeArray.safeRemove(at: 3) {
    print("Removed: \(removed)")
}
```

### Performance Monitoring

```swift
// Array performance monitoring
class ArrayPerformanceMonitor {
    private var operationCount = 0
    private var totalTime: TimeInterval = 0

    func measure<T>(_ operation: () -> T) -> T {
        let startTime = CFAbsoluteTimeGetCurrent()
        let result = operation()
        let endTime = CFAbsoluteTimeGetCurrent()

        operationCount += 1
        totalTime += (endTime - startTime)

        return result
    }

    func report() {
        let averageTime = operationCount > 0 ? totalTime / Double(operationCount) : 0
        print("Array operations: \(operationCount)")
        print("Total time: \(String(format: "%.6f", totalTime)) seconds")
        print("Average time: \(String(format: "%.6f", averageTime)) seconds")
    }
}

// Usage
let monitor = ArrayPerformanceMonitor()

var testArray = Array(0..<10000)

// Monitor operations
_ = monitor.measure { testArray.filter { $0 % 2 == 0 } }
_ = monitor.measure { testArray.map { $0 * 2 } }
_ = monitor.measure { testArray.sorted() }

monitor.report()
```

### Summary

Arrays are fundamental to Swift programming, providing ordered, type-safe collections with rich functionality:

**Core Characteristics:**
- Ordered collections of elements of the same type
- Zero-based indexing with bounds checking
- Value types (copied when assigned)
- Support for any element type

**Creation Methods:**
- Array literals `[1, 2, 3]`
- Initializers `Array(repeating:count:)`
- From sequences `Array(1...5)`
- Type inference and explicit typing

**Key Operations:**
- **Access:** Subscript `array[index]`, safe access patterns
- **Mutation:** `append()`, `insert()`, `remove()`, `replaceSubrange()`
- **Query:** `count`, `isEmpty`, `first`, `last`, `contains()`
- **Transformation:** `map()`, `filter()`, `reduce()`, `sorted()`
- **Combination:** Concatenation `+`, `append(contentsOf:)`, `zip()`

**Performance Considerations:**
- `append()` is amortized O(1)
- Insert/remove operations are O(n)
- Reserve capacity for bulk operations
- Use lazy operations for memory efficiency
- Copy-on-write optimization

**Advanced Patterns:**
- Generic array extensions
- Custom array types (Stack, Queue, CircularBuffer)
- Multi-dimensional arrays
- Functional programming with arrays
- Performance monitoring and optimization

**Best Practices:**
- Choose appropriate array types for specific needs
- Use safe access patterns to prevent crashes
- Reserve capacity for large arrays
- Leverage functional operations for clarity
- Monitor performance in critical code paths

Arrays form the backbone of data manipulation in Swift, offering both simplicity for basic use cases and sophisticated capabilities for complex applications.
