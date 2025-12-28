---
id: 733
---
﻿# Array Methods (count, isEmpty, first, last, contains, sorted, filter, map)

## Overview

Swift arrays provide a rich set of methods for querying, transforming, and manipulating collections. This section covers the essential array methods including counting, searching, sorting, filtering, and mapping operations with comprehensive examples and performance considerations.

## Table of Contents

- [Basic Properties and Access](#basic-properties-and-access)
- [Searching and Finding](#searching-and-finding)
- [Sorting Operations](#sorting-operations)
- [Filtering Methods](#filtering-methods)
- [Mapping Transformations](#mapping-transformations)
- [Combining Operations](#combining-operations)
- [Performance Considerations](#performance-considerations)
- [Advanced Patterns](#advanced-patterns)

## Basic Properties and Access

### Count and Empty Checks

```swift
// Array count and empty state
let numbers = [1, 2, 3, 4, 5]
let emptyArray: [Int] = []
let singleElement = [42]

// Count property - O(1) operation
print("Numbers count: \(numbers.count)")          // 5
print("Empty array count: \(emptyArray.count)")   // 0
print("Single element count: \(singleElement.count)") // 1

// isEmpty property - more efficient than count == 0
print("Numbers is empty: \(numbers.isEmpty)")     // false
print("Empty array is empty: \(emptyArray.isEmpty)") // true

// Preferred empty check pattern
if numbers.isEmpty {
    print("Array is empty")
} else {
    print("Array has \(numbers.count) elements")
}

// Avoid this pattern (less efficient):
if numbers.count == 0 {  // Still works but less clear
    print("Array is empty")
}
```

### First and Last Access

```swift
// Safe first and last element access
let fruits = ["Apple", "Banana", "Orange", "Mango"]
let noFruits: [String] = []

// first property - returns Optional
if let firstFruit = fruits.first {
    print("First fruit: \(firstFruit)")           // "Apple"
} else {
    print("No fruits in array")
}

if let firstEmpty = noFruits.first {
    print("First: \(firstEmpty)")
} else {
    print("Empty array has no first element")     // This prints
}

// last property - returns Optional
if let lastFruit = fruits.last {
    print("Last fruit: \(lastFruit)")             // "Mango"
}

// Safe indexing vs first/last
let safeFirst = fruits[safe: 0] ?? "No first element"
let safeLast = fruits[safe: fruits.count - 1] ?? "No last element"

print("Safe first: \(safeFirst)")                 // "Apple"
print("Safe last: \(safeLast)")                   // "Mango"

// Custom safe subscript extension
extension Array {
    subscript(safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}
```

### Min, Max, and Sum

```swift
// Finding minimum, maximum, and sum values
let scores = [85, 92, 78, 96, 88]
let temperatures = [-5.2, 15.7, 22.1, 8.9, -12.3]

// Min and max - work with Comparable elements
if let minScore = scores.min() {
    print("Minimum score: \(minScore)")           // 78
}

if let maxScore = scores.max() {
    print("Maximum score: \(maxScore)")           // 96
}

if let lowestTemp = temperatures.min() {
    print("Lowest temperature: \(lowestTemp)°C")  // -12.3
}

if let highestTemp = temperatures.max() {
    print("Highest temperature: \(highestTemp)°C") // 22.1
}

// Sum - works with numeric types
let totalScore = scores.reduce(0, +)              // 439
let averageScore = Double(totalScore) / Double(scores.count) // 87.8

// Custom sum for non-numeric types
extension Array where Element: Numeric {
    func sum() -> Element {
        return reduce(0, +)
    }

    func average() -> Element? {
        guard !isEmpty else { return nil }
        return sum() / Element(exactly: count)!
    }
}

print("Total score: \(scores.sum())")             // 439
print("Average score: \(scores.average() ?? 0)") // 87

// Finding min/max with custom criteria
struct Person {
    let name: String
    let age: Int
    let salary: Double
}

let people = [
    Person(name: "Alice", age: 25, salary: 50000),
    Person(name: "Bob", age: 30, salary: 60000),
    Person(name: "Charlie", age: 35, salary: 55000)
]

// Find youngest person
if let youngest = people.min(by: { $0.age < $1.age }) {
    print("Youngest: \(youngest.name), age \(youngest.age)")
}

// Find highest paid person
if let highestPaid = people.max(by: { $0.salary < $1.salary }) {
    print("Highest paid: \(highestPaid.name), $\(highestPaid.salary)")
}
```

## Searching and Finding

### Contains Method

```swift
// Check if array contains specific elements
let colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Basic contains - O(n) complexity
let hasRed = colors.contains("Red")              // true
let hasBlack = colors.contains("Black")          // false

let hasEven = numbers.contains { $0 % 2 == 0 }   // true
let hasNegative = numbers.contains { $0 < 0 }    // false

// Contains with custom conditions
let hasVowelStarting = colors.contains { color in
    let firstChar = color.lowercased().first
    return ["a", "e", "i", "o", "u"].contains(firstChar)
}                                                // true ("Orange" not present, but logic shows pattern)

// Check for multiple conditions
let hasMultipleConditions = colors.contains(where: { color in
    color.count > 4 && color.lowercased().contains("e")
})                                                // true ("Green", "Yellow", "Purple")
```

### Index Finding Methods

```swift
// Find indices of elements
let letters = ["A", "B", "C", "D", "E", "A", "B"]

// firstIndex(of:) - find first occurrence
if let firstA = letters.firstIndex(of: "A") {
    print("First 'A' at index: \(firstA)")       // 0
}

if let firstZ = letters.firstIndex(of: "Z") {
    print("First 'Z' at index: \(firstZ)")
} else {
    print("'Z' not found")                        // This prints
}

// firstIndex(where:) - find with predicate
if let firstVowel = letters.firstIndex(where: { letter in
    ["A", "E", "I", "O", "U"].contains(letter)
}) {
    print("First vowel at index: \(firstVowel)") // 0
}

// lastIndex(of:) - find last occurrence
if let lastA = letters.lastIndex(of: "A") {
    print("Last 'A' at index: \(lastA)")          // 5
}

// lastIndex(where:) - find last with predicate
if let lastConsonant = letters.lastIndex(where: { letter in
    !["A", "E", "I", "O", "U"].contains(letter)
}) {
    print("Last consonant at index: \(lastConsonant)") // 6 ("B")
}
```

### Finding Multiple Elements

```swift
// Find all indices of elements
extension Array where Element: Equatable {
    func indices(of element: Element) -> [Index] {
        return enumerated()
            .filter { $0.element == element }
            .map { $0.offset }
    }

    func indices(where predicate: (Element) -> Bool) -> [Index] {
        return enumerated()
            .filter { predicate($0.element) }
            .map { $0.offset }
    }
}

let values = [10, 20, 30, 20, 40, 20, 50]

// Find all indices of specific value
let allTwenties = values.indices(of: 20)         // [1, 3, 5]

// Find all indices matching condition
let evenIndices = values.indices(where: { $0 % 2 == 0 }) // [0, 1, 2, 3, 4, 5, 6] (all even numbers)
let largeValues = values.indices(where: { $0 > 25 })     // [2, 4, 6] (30, 40, 50)

// Find elements with their indices
let indexedElements = values.enumerated()
    .filter { $0.element > 25 }
    .map { (index: $0.offset, value: $0.element) }

print("Large values with indices: \(indexedElements)")
// [(index: 2, value: 30), (index: 4, value: 40), (index: 6, value: 50)]
```

## Sorting Operations

### Basic Sorting

```swift
// Sort arrays in place and create sorted copies
var unsortedNumbers = [64, 34, 25, 12, 22, 11, 90]
let originalNumbers = [64, 34, 25, 12, 22, 11, 90]

// sort() - modifies the array in place
unsortedNumbers.sort()
print("Sorted in place: \(unsortedNumbers)")     // [11, 12, 22, 25, 34, 64, 90]

// sorted() - returns a new sorted array
let sortedNumbers = originalNumbers.sorted()
print("Original: \(originalNumbers)")             // [64, 34, 25, 12, 22, 11, 90]
print("Sorted copy: \(sortedNumbers)")            // [11, 12, 22, 25, 34, 64, 90]

// Sort in descending order
let descending = originalNumbers.sorted(by: >)
print("Descending: \(descending)")                // [90, 64, 34, 25, 22, 12, 11]
```

### Custom Sort Criteria

```swift
// Sort with custom criteria
struct Product {
    let name: String
    let price: Double
    let rating: Double
    let inStock: Bool
}

let products = [
    Product(name: "Laptop", price: 999.99, rating: 4.5, inStock: true),
    Product(name: "Mouse", price: 29.99, rating: 4.2, inStock: false),
    Product(name: "Keyboard", price: 79.99, rating: 4.8, inStock: true),
    Product(name: "Monitor", price: 299.99, rating: 4.3, inStock: true)
]

// Sort by price (ascending)
let byPrice = products.sorted { $0.price < $1.price }
print("By price: \(byPrice.map { $0.name })")
// ["Mouse", "Keyboard", "Monitor", "Laptop"]

// Sort by rating (descending)
let byRating = products.sorted { $0.rating > $1.rating }
print("By rating: \(byRating.map { $0.name })")
// ["Keyboard", "Laptop", "Monitor", "Mouse"]

// Complex multi-criteria sort
let complexSort = products.sorted { lhs, rhs in
    // First by availability (in stock first)
    if lhs.inStock != rhs.inStock {
        return lhs.inStock && !rhs.inStock
    }
    // Then by rating (higher first)
    if lhs.rating != rhs.rating {
        return lhs.rating > rhs.rating
    }
    // Finally by price (lower first)
    return lhs.price < rhs.price
}

print("Complex sort: \(complexSort.map { "\($0.name)($\($0.price))" })")
// ["Keyboard($79.99)", "Laptop($999.99)", "Monitor($299.99)", "Mouse($29.99)"]
```

### Stable Sorting

```swift
// Stable sort maintains relative order of equal elements
let cards = [
    (suit: "Hearts", value: 10),
    (suit: "Spades", value: 5),
    (suit: "Hearts", value: 5),
    (suit: "Diamonds", value: 10)
]

// Sort by value, then by suit (stable)
let sortedByValue = cards.sorted { $0.value <= $1.value }
print("By value: \(sortedByValue)")
// Original order of equal values is preserved

// Unstable sort might change order of equal elements
// Swift's sort is stable, so equal elements maintain relative order
```

## Filtering Methods

### Basic Filter

```swift
// Filter elements based on conditions
let numbers = Array(1...20)

// Filter even numbers
let evens = numbers.filter { $0 % 2 == 0 }
print("Even numbers: \(evens)")                   // [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

// Filter numbers greater than 10
let greaterThanTen = numbers.filter { $0 > 10 }
print("Greater than 10: \(greaterThanTen)")       // [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

// Filter with complex conditions
let primes = numbers.filter { number in
    if number <= 1 { return false }
    if number <= 3 { return true }
    if number % 2 == 0 || number % 3 == 0 { return false }

    var i = 5
    while i * i <= number {
        if number % i == 0 || number % (i + 2) == 0 {
            return false
        }
        i += 6
    }
    return true
}
print("Prime numbers: \(primes)")                  // [2, 3, 5, 7, 11, 13, 17, 19]
```

### Advanced Filtering

```swift
// Filter with indices and multiple conditions
let words = ["apple", "Banana", "cherry", "Date", "elderberry"]

// Filter by length and case
let longWords = words.filter { $0.count > 5 }
print("Long words: \(longWords)")                  // ["Banana", "elderberry"]

let uppercaseWords = words.filter { $0.first?.isUppercase == true }
print("Uppercase words: \(uppercaseWords)")        // ["Banana", "Date"]

// Filter with index information
let indexedFilter = words.enumerated()
    .filter { index, word in
        index % 2 == 0 && word.count >= 5
    }
    .map { $0.element }

print("Even indices, length >= 5: \(indexedFilter)") // ["apple", "elderberry"]

// Remove elements matching condition (filter + invert)
let noFruits = ["apple", "car", "banana", "truck", "cherry"]
let nonFruits = noFruits.filter { word in
    !["apple", "banana", "cherry"].contains(word.lowercased())
}
print("Non-fruits: \(nonFruits)")                  // ["car", "truck"]
```

### Compact Map for Filtering and Transforming

```swift
// compactMap combines filter and map, removing nil values
let stringNumbers = ["1", "2", "three", "4", "five", "6"]

// Convert to integers, filtering out invalid strings
let validNumbers = stringNumbers.compactMap { Int($0) }
print("Valid numbers: \(validNumbers)")            // [1, 2, 4, 6]

// Process optional values
let optionalStrings: [String?] = ["hello", nil, "world", nil, "swift"]
let nonNilStrings = optionalStrings.compactMap { $0 }
print("Non-nil strings: \(nonNilStrings)")         // ["hello", "world", "swift"]

// Transform and filter in one operation
struct Person {
    let name: String?
    let age: Int?
}

let peopleData = [
    Person(name: "Alice", age: 25),
    Person(name: nil, age: 30),
    Person(name: "Bob", age: nil),
    Person(name: "Charlie", age: 35)
]

// Extract valid names of adults
let adultNames = peopleData.compactMap { person -> String? in
    guard let name = person.name, let age = person.age, age >= 18 else {
        return nil
    }
    return name
}
print("Adult names: \(adultNames)")                 // ["Alice", "Charlie"]
```

## Mapping Transformations

### Basic Map

```swift
// Transform each element using map
let numbers = [1, 2, 3, 4, 5]

// Double each number
let doubled = numbers.map { $0 * 2 }
print("Doubled: \(doubled)")                        // [2, 4, 6, 8, 10]

// Convert to strings
let numberStrings = numbers.map { String($0) }
print("As strings: \(numberStrings)")               // ["1", "2", "3", "4", "5"]

// Transform to different types
let temperatures = [23.5, 18.7, 25.1, 30.2]
let temperatureStrings = temperatures.map { String(format: "%.1f°C", $0) }
print("Temperatures: \(temperatureStrings)")        // ["23.5°C", "18.7°C", "25.1°C", "30.2°C"]
```

### Complex Transformations

```swift
// Complex transformations with map
struct Student {
    let name: String
    let scores: [Int]
}

let students = [
    Student(name: "Alice", scores: [85, 92, 88]),
    Student(name: "Bob", scores: [78, 85, 82]),
    Student(name: "Charlie", scores: [95, 88, 91])
]

// Transform to grade reports
let gradeReports = students.map { student -> [String: Any] in
    let average = Double(student.scores.reduce(0, +)) / Double(student.scores.count)
    let grade = average >= 90 ? "A" : average >= 80 ? "B" : "C"

    return [
        "name": student.name,
        "average": average,
        "grade": grade,
        "scores": student.scores
    ]
}

print("Grade reports:")
gradeReports.forEach { report in
    print("\(report["name"]!): \(report["grade"]!) (\(String(format: "%.1f", report["average"] as! Double)))")
}
```

### Map with Indices

```swift
// Transform with index information
let names = ["Alice", "Bob", "Charlie", "Diana"]

// Add index to each name
let indexedNames = names.enumerated().map { index, name in
    "\(index + 1). \(name)"
}
print("Indexed names: \(indexedNames)")
// ["1. Alice", "2. Bob", "3. Charlie", "4. Diana"]

// Create ranking system
let scores = [95, 87, 92, 78]
let rankings = scores.enumerated()
    .sorted { $0.element > $1.element }  // Sort by score descending
    .enumerated()
    .map { rank, indexedScore in
        "Rank \(rank + 1): Student \(indexedScore.offset + 1) with \(indexedScore.element) points"
    }

print("Rankings:")
rankings.forEach { print($0) }
```

## Combining Operations

### Method Chaining

```swift
// Chain multiple array operations
let data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

// Complex data processing pipeline
let result = data
    .filter { $0 % 2 == 0 }                    // Keep even numbers: [2, 4, 6, 8, 10, 12]
    .map { $0 * $0 }                          // Square them: [4, 16, 36, 64, 100, 144]
    .filter { $0 < 100 }                      // Keep under 100: [4, 16, 36, 64]
    .sorted(by: >)                            // Sort descending: [64, 36, 16, 4]
    .map { "Value: \($0)" }                   // Format as strings

print("Processed result: \(result)")
// ["Value: 64", "Value: 36", "Value: 16", "Value: 4"]
```

### Advanced Chaining with Custom Types

```swift
// Complex chaining with custom types
struct Transaction {
    let id: String
    let amount: Double
    let date: Date
    let category: String
    let isCompleted: Bool
}

let transactions = [
    Transaction(id: "1", amount: 50.0, date: Date(), category: "Food", isCompleted: true),
    Transaction(id: "2", amount: 25.0, date: Date(), category: "Transport", isCompleted: false),
    Transaction(id: "3", amount: 100.0, date: Date(), category: "Food", isCompleted: true),
    Transaction(id: "4", amount: 75.0, date: Date(), category: "Entertainment", isCompleted: true),
    Transaction(id: "5", amount: 30.0, date: Date(), category: "Transport", isCompleted: true)
]

// Process transactions: filter, group, and summarize
let categorySummaries = transactions
    .filter { $0.isCompleted }                  // Only completed transactions
    .reduce(into: [String: [Transaction]]()) {  // Group by category
        result[$1.category, default: []].append($1)
    }
    .mapValues { transactions -> [String: Any] in   // Summarize each category
        let total = transactions.reduce(0) { $0 + $1.amount }
        let count = transactions.count
        let average = total / Double(count)

        return [
            "total": total,
            "count": count,
            "average": average,
            "transactions": transactions.map { $0.id }
        ]
    }

print("Category summaries:")
for (category, summary) in categorySummaries {
    print("\(category): $\(summary["total"]!) from \(summary["count"]!) transactions")
}
```

## Performance Considerations

### Operation Complexity

```swift
// Time complexity of array operations
/*
Operation       | Time Complexity | Notes
----------------|-----------------|--------
count           | O(1)           | Direct property access
isEmpty         | O(1)           | Direct property access
first/last      | O(1)           | Direct property access
contains        | O(n)           | Linear search
firstIndex      | O(n)           | Linear search
filter          | O(n)           | Processes each element
map             | O(n)           | Processes each element
sort            | O(n log n)     | Efficient sorting
reduce          | O(n)           | Accumulates over all elements
min/max         | O(n)           | Scans all elements
*/

// Optimize for performance
extension Array where Element: Hashable {
    // Fast contains for hashable elements
    func fastContains(_ element: Element) -> Bool {
        return Set(self).contains(element)  // O(1) average case
    }
}

let largeArray = Array(1...100000)
let searchValue = 50000

// Compare performance
let start1 = CFAbsoluteTimeGetCurrent()
let result1 = largeArray.contains(searchValue)
let time1 = CFAbsoluteTimeGetCurrent() - start1

let start2 = CFAbsoluteTimeGetCurrent()
let result2 = largeArray.fastContains(searchValue)
let time2 = CFAbsoluteTimeGetCurrent() - start2

print("Linear search: \(time1) seconds")
print("Set lookup: \(time2) seconds")
print("Set is \(time1/time2) times faster")
```

### Memory Efficiency

```swift
// Memory-efficient operations
let numbers = Array(1...1000000)

// Lazy operations don't create intermediate arrays
let result = numbers
    .lazy                    // Make operations lazy
    .filter { $0 % 2 == 0 }  // No intermediate array created
    .map { $0 * 2 }          // No intermediate array created
    .prefix(10)              // Only takes first 10 results
    .reduce(0, +)            // Final computation

print("Result: \(result)")   // Only creates final result, not intermediate arrays

// Eager vs Lazy comparison
let eagerResult = numbers.filter { $0 % 2 == 0 }.map { $0 * 2 }.prefix(10)
// Creates two intermediate arrays

let lazyResult = numbers.lazy.filter { $0 % 2 == 0 }.map { $0 * 2 }.prefix(10)
// No intermediate arrays created
```

## Advanced Patterns

### Custom Array Extensions

```swift
// Useful array extensions
extension Array {
    // Safe subscript
    subscript(safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }

    // Chunk array into smaller arrays
    func chunked(into size: Int) -> [[Element]] {
        stride(from: 0, to: count, by: size).map {
            Array(self[$0..<Swift.min($0 + size, count)])
        }
    }

    // Find duplicates
    func duplicates() -> [Element] where Element: Hashable {
        let seen = Set(self)
        return filter { element in
            let count = self.filter { $0 == element }.count
            return count > 1 && seen.contains(element)
        }.removingDuplicates()
    }

    // Remove duplicates while preserving order
    func removingDuplicates() -> [Element] where Element: Hashable {
        var seen = Set<Element>()
        return filter { seen.insert($0).inserted }
    }

    // Group by key
    func groupedBy<T: Hashable>(_ keyForValue: (Element) -> T) -> [T: [Element]] {
        return Dictionary(grouping: self, by: keyForValue)
    }

    // Partition array
    func partition(by predicate: (Element) -> Bool) -> ([Element], [Element]) {
        var matching = [Element]()
        var nonMatching = [Element]()

        for element in self {
            if predicate(element) {
                matching.append(element)
            } else {
                nonMatching.append(element)
            }
        }

        return (matching, nonMatching)
    }
}

// Usage examples
let data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

// Safe access
print("Safe access [5]: \(data[safe: 5] ?? "nil")")  // 6
print("Safe access [20]: \(data[safe: 20] ?? "nil")") // nil

// Chunking
let chunks = data.chunked(into: 3)
print("Chunks: \(chunks)")
// [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2], [3]]

// Duplicates
let duplicates = data.duplicates()
print("Duplicates: \(duplicates)")  // [1, 2, 3]

// Grouping
let groupedByParity = data.groupedBy { $0 % 2 == 0 ? "even" : "odd" }
print("Grouped: \(groupedByParity)")
// ["odd": [1, 3, 5, 7, 9, 1, 3], "even": [2, 4, 6, 8, 10, 2]]

// Partitioning
let (evens, odds) = data.partition { $0 % 2 == 0 }
print("Evens: \(evens), Odds: \(odds)")
// Evens: [2, 4, 6, 8, 10, 2], Odds: [1, 3, 5, 7, 9, 1, 3]
```

### Functional Programming Patterns

```swift
// Advanced functional patterns
extension Array {
    // Flat map with index
    func flatMapWithIndex<T>(_ transform: (Index, Element) -> [T]) -> [T] {
        var result = [T]()
        for (index, element) in enumerated() {
            result.append(contentsOf: transform(index, element))
        }
        return result
    }

    // Running total
    func runningTotal() -> [Element] where Element: Numeric {
        var total: Element = 0
        return map { element in
            total += element
            return total
        }
    }

    // Sliding window
    func slidingWindow(size: Int) -> [[Element]] {
        guard size > 0 && size <= count else { return [] }
        return (0...(count - size)).map { Array(self[$0..<$0 + size]) }
    }

    // Frequency count
    func frequency() -> [Element: Int] where Element: Hashable {
        return reduce(into: [:]) { counts, element in
            counts[element, default: 0] += 1
        }
    }
}

// Usage examples
let values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Running total
let totals = values.runningTotal()
print("Running totals: \(totals)")  // [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

// Sliding window
let windows = values.slidingWindow(size: 3)
print("Sliding windows: \(windows)")
// [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]]

// Frequency count
let repeated = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
let frequencies = repeated.frequency()
print("Frequencies: \(frequencies)")  // [1: 1, 2: 2, 3: 3, 4: 4]

// Flat map with index
let indexedPairs = values.flatMapWithIndex { index, value in
    [(index, value), (index, value * 2)]
}
print("Indexed pairs: \(indexedPairs.prefix(6))")
// [(0, 1), (0, 2), (1, 2), (1, 4), (2, 3), (2, 6)]
```

### Summary

Swift's array methods provide powerful tools for data manipulation:

**Basic Properties:**
- `count` and `isEmpty` for size information
- `first` and `last` for safe element access
- `min()`, `max()`, and custom reductions

**Searching Methods:**
- `contains()` for presence checking
- `firstIndex()` and `lastIndex()` for position finding
- Custom search predicates with `firstIndex(where:)`

**Transformation Methods:**
- `sorted()` and `sort()` for ordering
- `filter()` for conditional selection
- `map()` for element transformation
- `compactMap()` for filtering and transforming

**Performance Awareness:**
- Understanding time complexity (O(1) vs O(n) vs O(n log n))
- Lazy operations for memory efficiency
- Custom extensions for specialized needs

**Advanced Patterns:**
- Method chaining for complex pipelines
- Custom array extensions for reusable functionality
- Functional programming approaches
- Memory-efficient operations

These methods form the foundation for working with collections in Swift, enabling both simple operations and complex data processing pipelines while maintaining safety and performance.
