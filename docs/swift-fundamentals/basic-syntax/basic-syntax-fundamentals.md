---
id: 735
---
# Basic Syntax Fundamentals

## Overview

Swift's syntax is designed to be clean, expressive, and safe. Understanding the basic syntax elements is fundamental to writing readable and maintainable Swift code. This section covers the core building blocks of Swift syntax including statements, expressions, comments, and code structure.

## Table of Contents

- [Statements and Expressions](#statements-and-expressions)
- [Comments](#comments)
- [Semicolons](#semicolons)
- [Whitespace and Line Breaks](#whitespace-and-line-breaks)
- [Code Blocks](#code-blocks)
- [Keywords and Identifiers](#keywords-and-identifiers)
- [Operators](#operators)
- [Literals](#literals)
- [Scope and Visibility](#scope-and-visibility)

## Statements and Expressions

### Expressions

```swift
// Expressions evaluate to a value
let number = 42                    // Literal expression
let sum = 2 + 3                    // Arithmetic expression
let greeting = "Hello" + " World"  // String concatenation expression
let isEven = number % 2 == 0       // Comparison expression
let result = max(10, 20)           // Function call expression

// Complex expressions
let complex = (number * 2) + (sum / 3) - 1  // Nested arithmetic
let conditional = isEven ? "even" : "odd"    // Ternary conditional expression

// Expressions can be used anywhere a value is expected
print("The number \(number) is \(conditional)")  // Uses string interpolation
let array = [number, sum, complex]  // Array literal with expressions
let dict = ["value": number, "sum": sum]  // Dictionary literal with expressions
```

### Statements

```swift
// Declaration statements
let constant = "immutable"
var variable = "mutable"
func greet(name: String) { }

// Assignment statements
variable = "changed"
let computed = constant + " value"

// Control flow statements
if variable.count > 5 {
    print("Long string")
} else {
    print("Short string")
}

for i in 1...5 {
    print("Count: \(i)")
}

while variable != "stop" {
    variable += "."
}

switch number {
case 0:
    print("Zero")
case 1...10:
    print("Small number")
default:
    print("Large number")
}

// Loop control statements
for i in 1...10 {
    if i == 5 {
        break  // Exit loop
    }
    if i % 2 == 0 {
        continue  // Skip to next iteration
    }
    print(i)  // Prints: 1, 3
}

// Return statements (in functions)
func double(_ x: Int) -> Int {
    return x * 2
}

// Throw statements (error handling)
enum MathError: Error {
    case divisionByZero
}

func divide(_ a: Int, _ b: Int) throws -> Int {
    guard b != 0 else {
        throw MathError.divisionByZero
    }
    return a / b
}
```

### Expression Statements

```swift
// Some expressions can be used as statements
var counter = 0

// Function call expressions as statements
print("Hello")                      // Side effect only
counter += 1                        // Assignment expression as statement

// Method calls on objects
var array = [1, 2, 3]
array.append(4)                     // Mutating method call
array.sort()                        // Another mutating method call

// Closure execution
let operation = { (x: Int) -> Int in x * 2 }
let doubled = operation(5)          // Expression
operation(5)                        // Same expression used as statement

// Optional operations
var optionalValue: Int? = 42
optionalValue = nil                 // Assignment
optionalValue?.description         // Optional chaining (expression)
```

## Comments

### Single-Line Comments

```swift
// This is a single-line comment
let value = 42  // Comments can follow code on the same line

// Comments are ignored by the compiler
// They exist solely for human readers
// Use them to explain complex logic

func complexCalculation(x: Int, y: Int) -> Int {
    // Step 1: Validate inputs
    guard x > 0 && y > 0 else { return 0 }

    // Step 2: Perform calculation
    let result = (x * y) + (x / y)

    // Step 3: Return result
    return result
}
```

### Multi-Line Comments

```swift
/*
 This is a multi-line comment.
 It can span multiple lines.
 All text between /* and */ is ignored by the compiler.
 */

/*
 Multi-line comments are useful for:
 - Detailed explanations of complex algorithms
 - API documentation
 - Temporarily disabling large blocks of code
 - Legal notices and copyrights
 */

/*
 You can nest multi-line comments, but this is rarely needed:

 /*
  This nested comment
  is valid but not recommended
  */
 */

func documentedFunction() {
    /*
     This function performs a complex operation.
     It takes no parameters and returns void.
     Side effects: modifies global state
     */
    print("Function executed")
}
```

### Documentation Comments

```swift
/// A simple greeting function
/// - Parameter name: The name of the person to greet
/// - Returns: A greeting string
/// - Note: This function capitalizes the first letter of the name
func createGreeting(for name: String) -> String {
    let capitalizedName = name.prefix(1).uppercased() + name.dropFirst()
    return "Hello, \(capitalizedName)!"
}

/**
 A more complex function with detailed documentation.

 This function calculates the factorial of a given number using
 recursion. Factorial of n (n!) is the product of all positive
 integers less than or equal to n.

 ## Example Usage:
 ```
 let fact5 = factorial(5)  // Returns 120
 let fact0 = factorial(0)  // Returns 1
 ```

 ## Important Notes:
 - Returns 1 for input 0 (by mathematical definition)
 - May cause stack overflow for large inputs due to recursion
 - Only works with non-negative integers

 - Parameter n: A non-negative integer
 - Returns: The factorial of n
 - Precondition: n >= 0
 - Complexity: O(n) time, O(n) space due to recursion
 */
func factorial(_ n: Int) -> Int {
    precondition(n >= 0, "Factorial is only defined for non-negative integers")
    return n == 0 ? 1 : n * factorial(n - 1)
}

/**
 A class representing a geometric point.

 Points can be created with x and y coordinates and support
 various geometric operations.

 ## Topics
 - ``init(x:y:)``
 - ``distance(to:)``
 - ``angle(to:)``

 ### Coordinate System
 This class uses the standard Cartesian coordinate system
 where (0,0) is the origin.
 */
class Point {
    /// The x-coordinate
    let x: Double
    /// The y-coordinate
    let y: Double

    /// Creates a new point with the specified coordinates
    /// - Parameters:
    ///   - x: The x-coordinate
    ///   - y: The y-coordinate
    init(x: Double, y: Double) {
        self.x = x
        self.y = y
    }

    /// Calculates the distance to another point
    /// - Parameter other: The other point
    /// - Returns: The Euclidean distance between the points
    func distance(to other: Point) -> Double {
        let dx = x - other.x
        let dy = y - other.y
        return sqrt(dx * dx + dy * dy)
    }
}
```

### Comment Best Practices

```swift
// ✅ Good: Clear, concise comments that add value

// Calculates compound interest
func calculateCompoundInterest(principal: Double, rate: Double, years: Int) -> Double {
    return principal * pow(1 + rate, Double(years))
}

// ❌ Bad: Comments that state the obvious

// This function adds two numbers
func add(_ a: Int, _ b: Int) -> Int {
    // Add a and b
    return a + b
}

// ✅ Good: Comments explaining why, not what

// Using binary search for O(log n) performance on sorted arrays
func findElement(in array: [Int], target: Int) -> Int? {
    var low = 0
    var high = array.count - 1

    while low <= high {
        let mid = (low + high) / 2
        if array[mid] == target {
            return mid
        } else if array[mid] < target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return nil
}

// ✅ Good: TODO and FIXME comments

// TODO: Implement caching to improve performance
func expensiveOperation() -> Data {
    // FIXME: This operation blocks the main thread
    return performNetworkRequest()
}

// ✅ Good: Warning comments for dangerous code

func dangerousOperation() {
    // WARNING: This function is not thread-safe
    // Only call from the main thread
    modifySharedState()
}
```

## Semicolons

### Optional Semicolons

```swift
// Semicolons are optional in Swift
let a = 1
let b = 2
let c = 3

// Same code with semicolons (valid but not preferred)
let x = 1;
let y = 2;
let z = 3;

// Multiple statements on one line require semicolons
let p = 1; let q = 2; let r = 3

// Control flow statements
if true { print("yes") }; if false { print("no") }

// Closures and complex expressions
let result = [1, 2, 3].map { $0 * 2 }; print(result)
```

### When Semicolons Are Required

```swift
// Required: Multiple statements in control flow
if condition { statement1(); statement2() }

// Required: Multiple statements in closures
let doubled = numbers.map { value in statement1(); return value * 2 }

// Required: After return statements in single-line closures
let sorted = array.sorted { $0 > $1; return $0 }

// Required: In complex expressions
func complex() -> Int { let x = 1; let y = 2; return x + y }

// Required: In enum cases with raw values
enum Status: String {
    case active = "ACTIVE";
    case inactive = "INACTIVE";
}

// Required: In protocol compositions
protocol A {}; protocol B {}
typealias AB = A & B; let instance: AB = object
```

### Style Guidelines

```swift
// Preferred: No semicolons except where required
func preferredStyle() {
    let a = 1
    let b = 2
    let c = a + b
    print(c)
}

// Acceptable: Semicolons for compact code (rare)
func compactStyle() { let a = 1; let b = 2; print(a + b) }

// Avoid: Excessive semicolons
func avoidThis() {
    let a = 1;  // Unnecessary semicolon
    let b = 2;  // Unnecessary semicolon
    print(a + b); // Unnecessary semicolon
}
```

## Whitespace and Line Breaks

### Line Breaks and Indentation

```swift
// Good: Proper indentation and line breaks
func calculateArea(width: Double, height: Double) -> Double {
    let area = width * height
    return area
}

// Bad: Poor formatting
func calculateArea(width:Double,height:Double)->Double{let area=width*height;return area;}

// Good: Logical line breaks
func longFunctionName(
    with parameter1: String,
    and parameter2: Int,
    anotherParameter: Bool
) -> String {
    // Implementation
    return "result"
}

// Good: Breaking long expressions
let result = someVeryLongVariableName
    .someMethod()
    .anotherMethod(with: parameter)
    .finalMethod()

// Good: Aligning similar elements
let names = [
    "Alice",
    "Bob",
    "Charlie"
]

let coordinates = [
    (x: 1, y: 2),
    (x: 3, y: 4),
    (x: 5, y: 6)
]
```

### Spacing Conventions

```swift
// Good: Consistent spacing
let sum = a + b
let array = [1, 2, 3]
let dict = ["key": "value"]
func call(param: Int) { }

// Bad: Inconsistent spacing
let sum=a+b
let array=[1,2,3]
let dict=["key":"value"]
func call(param:Int){ }

// Good: Spaces around operators
if x > 5 && y < 10 || z == 0 {
    // condition
}

// Good: No spaces in ranges
let range = 1...10
let halfOpen = 0..<count

// Good: Spaces after commas
let tuple = (1, 2, 3)
func multiParam(a: Int, b: String, c: Bool) { }

// Good: Spaces in closures
let doubled = numbers.map { $0 * 2 }
let filtered = numbers.filter { $0 > 5 }
```

### Vertical Spacing

```swift
// Good: Logical grouping with blank lines
import Foundation

class Calculator {

    // MARK: - Public Methods

    func add(_ a: Double, _ b: Double) -> Double {
        return a + b
    }

    func subtract(_ a: Double, _ b: Double) -> Double {
        return a - b
    }

    // MARK: - Private Methods

    private func validateInput(_ input: Double) -> Bool {
        return input.isFinite && !input.isNaN
    }
}

// Good: Separating logical sections
func complexFunction() {
    // Input validation
    guard validateInput() else { return }

    // Processing
    let result = performCalculation()

    // Output
    displayResult(result)
}
```

## Code Blocks

### Block Structure

```swift
// Function blocks
func exampleFunction() {
    // Code block starts
    let localVariable = "value"

    if localVariable.count > 0 {
        // Nested block
        print(localVariable)
    }
    // Code block ends
}

// Control flow blocks
if condition {
    // if block
    action1()
} else {
    // else block
    action2()
}

// Loop blocks
for item in collection {
    // loop block
    process(item)
}

// Switch cases (implicit blocks)
switch value {
case .option1:
    // case block
    handleOption1()
case .option2:
    // case block
    handleOption2()
default:
    // default block
    handleDefault()
}
```

### Scope and Lifetime

```swift
// Variables scoped to their containing block
func demonstrateScope() {
    let outerVariable = "outer"

    if true {
        let innerVariable = "inner"
        print(outerVariable)  // ✅ Accessible
        print(innerVariable)  // ✅ Accessible
    }

    print(outerVariable)      // ✅ Accessible
    // print(innerVariable)   // ❌ Not accessible (out of scope)
}

// Block scope in control flow
for i in 0..<3 {
    let loopVariable = "iteration \(i)"
    print(loopVariable)
}
// loopVariable not accessible here

// Closures capture their defining scope
func createCounter() -> () -> Int {
    var count = 0

    return {
        count += 1
        return count
    }
}

let counter = createCounter()
print(counter())  // 1
print(counter())  // 2
// count variable persists due to closure capture
```

### Early Returns and Guard Clauses

```swift
// Early returns for cleaner code
func processUserInput(_ input: String?) -> String {
    guard let input = input else {
        return "No input provided"
    }

    guard !input.isEmpty else {
        return "Input cannot be empty"
    }

    guard input.count >= 3 else {
        return "Input must be at least 3 characters"
    }

    // Process valid input
    return "Processed: \(input.uppercased())"
}

// Multiple return points in switch
func describeNumber(_ number: Int) -> String {
    switch number {
    case 0:
        return "zero"
    case let x where x < 0:
        return "negative"
    case 1...9:
        return "single digit positive"
    case 10...99:
        return "double digit positive"
    default:
        return "large number"
    }
}
```

## Keywords and Identifiers

### Reserved Keywords

```swift
// Swift reserved keywords (cannot be used as identifiers)
// Keywords are context-sensitive - some can be used in certain contexts

// Declaration keywords
class, struct, enum, protocol, extension, func, let, var
init, deinit, subscript, typealias, associatedtype

// Control flow keywords
if, else, switch, case, default, for, while, repeat, break, continue
return, throw, defer, do, catch, guard, fallthrough

// Access control keywords
public, internal, private, fileprivate, open

// Other keywords
import, as, is, self, super, inout, mutating, nonmutating
convenience, required, static, final, lazy, weak, unowned
optional, required, override, indirect, isolated, nonisolated
```

### Identifier Rules

```swift
// Valid identifiers
let variableName = "valid"
let _privateVar = "starts with underscore"
let camelCase = "convention"
let PascalCase = "for types"
let withNumbers123 = "can contain numbers"
let unicode = "café"  // Unicode characters allowed

// Invalid identifiers (would cause compile errors)
// let 123invalid = "cannot start with number"
// let var = "reserved keyword"
// let let = "duplicate keyword"
// let invalid-char = "hyphens not allowed"

// Backtick escaping for reserved words (rarely recommended)
let `class` = "escaped keyword"  // Valid but not recommended
let `func` = "another escaped keyword"  // Avoid when possible

// Conventions
struct User {
    let firstName: String    // camelCase for properties
    let lastName: String

    func getFullName() -> String {  // camelCase for methods
        return "\(firstName) \(lastName)"
    }
}

class APIManager {  // PascalCase for types
    static let shared = APIManager()  // camelCase for static properties

    func fetchData() {  // camelCase for methods
        // implementation
    }
}
```

### Naming Conventions

```swift
// Swift naming conventions (from Swift API Design Guidelines)

// 1. Clarity at the point of use
let names = ["Alice", "Bob", "Charlie"]
// Clear that this contains names

let stringValues: [String] = []
// Redundant type annotation - compiler can infer

// 2. Use US English spelling
let color = "red"          // Not "colour"
let center = CGPoint()     // Not "centre"

// 3. Type names: PascalCase
class UserManager { }
struct HTTPResponse { }
enum Result<T> { }

// 4. Function and variable names: camelCase
func sendMessage() { }
let maximumValue = 100
var currentUser: User?

// 5. Constants: camelCase (same as variables)
let maximumLoginAttempts = 3
let apiBaseURL = "https://api.example.com"

// 6. Acronyms treated as words
let htmlString = "<p>Hello</p>"      // Not HTMLString
let urlPath = "/users"               // Not URLPath
let jsonData = Data()                // Not JSONData

// 7. Delegate protocols end with "Delegate"
protocol UITableViewDelegate { }
protocol URLSessionDelegate { }

// 8. Type-erasing wrappers end with "Any"
struct AnyPublisher<Output, Failure> { }
struct AnyView { }

// 9. Generic parameters: single uppercase letter or descriptive
func swap<T>(_ a: inout T, _ b: inout T) { }
func transform<Input, Output>(_ input: Input) -> Output { }
```

## Operators

### Arithmetic Operators

```swift
// Basic arithmetic
let sum = 5 + 3          // 8
let difference = 5 - 3   // 2
let product = 5 * 3      // 15
let quotient = 5 / 3     // 1 (integer division)
let remainder = 5 % 3    // 2

// Floating point arithmetic
let floatSum = 5.0 + 3.0        // 8.0
let floatQuotient = 5.0 / 3.0   // 1.666...

// Compound assignment
var value = 10
value += 5    // value = 15
value -= 3    // value = 12
value *= 2    // value = 24
value /= 4    // value = 6
value %= 5    // value = 1

// Unary operators
let positive = +5       // 5
let negative = -5       // -5
var count = 0
count += 1             // Increment
count -= 1             // Decrement
```

### Comparison Operators

```swift
// Equality and inequality
let equal = (5 == 5)              // true
let notEqual = (5 != 3)           // true

// Ordering comparisons
let greater = (5 > 3)             // true
let less = (5 < 3)                // false
let greaterEqual = (5 >= 5)       // true
let lessEqual = (3 <= 5)          // true

// String comparisons (lexicographic)
let strCompare = ("apple" < "banana")  // true ("a" comes before "b")

// Optional comparisons
let optional1: Int? = 5
let optional2: Int? = nil
let optCompare = (optional1 == optional2)  // false

// Identity operators (for reference types)
class Person {
    let name: String
    init(name: String) { self.name = name }
}

let person1 = Person(name: "Alice")
let person2 = Person(name: "Alice")
let person3 = person1

let identical = (person1 === person3)     // true (same instance)
let notIdentical = (person1 === person2)  // false (different instances)
let equalValues = (person1 == person2)    // error: == not defined for Person
```

### Logical Operators

```swift
// Logical AND
let bothTrue = (true && true)      // true
let oneFalse = (true && false)     // false
let bothFalse = (false && false)   // false

// Logical OR
let eitherTrue = (true || false)   // true
let oneTrue = (false || true)      // true
let bothFalseOr = (false || false) // false

// Logical NOT
let notTrue = !true                // false
let notFalse = !false              // true

// Short-circuit evaluation
func expensiveOperation() -> Bool {
    print("Expensive operation called")
    return true
}

let result1 = false && expensiveOperation()  // Short-circuits, expensiveOperation not called
let result2 = true || expensiveOperation()   // Short-circuits, expensiveOperation not called
```

### Range Operators

```swift
// Closed range operator
let closedRange = 1...5            // 1, 2, 3, 4, 5
for i in closedRange {
    print(i)  // Prints 1, 2, 3, 4, 5
}

// Half-open range operator
let halfOpenRange = 1..<5          // 1, 2, 3, 4
for i in halfOpenRange {
    print(i)  // Prints 1, 2, 3, 4
}

// One-sided ranges
let fromStart = ...5               // -infinity...5
let toEnd = 3...                   // 3...infinity
let fromArrayStart = ..<array.count

// Range with arrays
let numbers = [10, 20, 30, 40, 50]
let slice = numbers[1...3]         // [20, 30, 40]

// Pattern matching with ranges
let score = 85
switch score {
case 0..<60:
    print("Failing")
case 60..<70:
    print("D")
case 70..<80:
    print("C")
case 80..<90:
    print("B")
case 90...100:
    print("A")
default:
    print("Invalid score")
}
```

### Custom Operators

```swift
// Defining custom operators
infix operator ** : MultiplicationPrecedence

func ** (lhs: Double, rhs: Double) -> Double {
    return pow(lhs, rhs)
}

let power = 2.0 ** 3.0  // 8.0

// Custom operator for string repetition
infix operator * : MultiplicationPrecedence

func * (lhs: String, rhs: Int) -> String {
    return String(repeating: lhs, count: rhs)
}

let repeated = "Ha" * 3  // "HaHaHa"

// Prefix and postfix operators
prefix operator √

prefix func √ (value: Double) -> Double {
    return sqrt(value)
}

let squareRoot = √16.0  // 4.0

// Operator precedence and associativity
precedencegroup ExponentiationPrecedence {
    higherThan: MultiplicationPrecedence
    associativity: right
}

infix operator ** : ExponentiationPrecedence
```

## Literals

### Numeric Literals

```swift
// Integer literals
let decimal = 42          // Decimal
let binary = 0b101010     // Binary: 42
let octal = 0o52          // Octal: 42
let hexadecimal = 0x2A    // Hexadecimal: 42

// Floating-point literals
let float1 = 3.14159      // Decimal
let float2 = 0.5          // Leading zero
let float3 = 1e10         // Scientific notation: 10000000000.0
let float4 = 1.5e-2       // Scientific notation: 0.015

// Underscore separators for readability
let largeNumber = 1_000_000     // 1000000
let binaryByte = 0b1000_0000    // 128
let ipAddress = 192_168_1_1     // More readable

// Type inference and explicit types
let inferredInt = 42            // Int
let inferredDouble = 42.0       // Double
let explicitFloat: Float = 42   // Float
let explicitInt64: Int64 = 42   // Int64
```

### String Literals

```swift
// String literals
let simple = "Hello, World!"
let multiLine = """
    This is a multi-line
    string literal.
    It preserves whitespace.
    """

// Escaped characters
let escaped = "Line 1\nLine 2\tTabbed"
let quotes = "He said \"Hello\" to me"
let path = "C:\\Users\\John\\Documents"

// Raw strings (Swift 5.0+)
let rawString = #"Line 1\nLine 2"#     // No escaping: "Line 1\nLine 2"
let rawWithQuotes = #"He said "Hello""# // No escaping needed

// String interpolation
let name = "Alice"
let age = 25
let greeting = "Hello, \(name)! You are \(age) years old."

// Extended string delimiters
let json = #"""
{
    "name": "\#(name)",
    "age": \#(age)
}
"""#
```

### Boolean and Nil Literals

```swift
// Boolean literals
let `true` = true         // true
let `false` = false       // false

// Nil literal
let optionalInt: Int? = nil
let optionalString: String? = nil

// Checking for nil
if optionalInt == nil {
    print("Value is nil")
}

// Optional binding
if let value = optionalInt {
    print("Value is \(value)")
} else {
    print("Value is nil")
}
```

### Array and Dictionary Literals

```swift
// Array literals
let emptyArray: [Int] = []
let numbers = [1, 2, 3, 4, 5]
let strings = ["a", "b", "c"]
let inferred = [1, 2, 3]  // [Int]

// Dictionary literals
let emptyDict: [String: Int] = [:]
let ages = ["Alice": 25, "Bob": 30, "Charlie": 35]
let inferredDict = ["a": 1, "b": 2]  // [String: Int]

// Complex literals
let complexArray = [
    ["name": "Alice", "age": 25],
    ["name": "Bob", "age": 30]
]

let mixedDict = [
    "users": [["name": "Alice"], ["name": "Bob"]],
    "count": 2
] as [String: Any]
```

## Scope and Visibility

### Global Scope

```swift
// Global variables and functions (accessible everywhere)
let globalConstant = "I'm global"
var globalVariable = 42

func globalFunction() {
    print("I'm a global function")
}

// Global scope is the file level
class GlobalClass {
    // Class members have their own scope
}

// Nested scopes
func outerFunction() {
    let outerVariable = "outer"

    func innerFunction() {
        let innerVariable = "inner"
        print(outerVariable)  // ✅ Can access outer scope
        print(innerVariable)  // ✅ Can access own scope
    }

    innerFunction()
    print(outerVariable)     // ✅ Can access own scope
    // print(innerVariable)  // ❌ Cannot access inner scope
}
```

### Local Scope

```swift
func demonstrateLocalScope() {
    let localVar = "I'm local to this function"

    if true {
        let blockVar = "I'm local to this block"
        print(localVar)    // ✅ Accessible
        print(blockVar)    // ✅ Accessible
    }

    print(localVar)        // ✅ Accessible
    // print(blockVar)     // ❌ Not accessible (out of scope)
}

// Loop scopes
for i in 0..<3 {
    let loopVar = "Iteration \(i)"
    print(loopVar)         // ✅ Accessible in loop
}
// print(loopVar)          // ❌ Not accessible (loop scope ended)

// Switch case scopes
let value = 1
switch value {
case 1:
    let caseVar = "Case 1"
    print(caseVar)         // ✅ Accessible in case
case 2:
    let anotherCaseVar = "Case 2"
    print(anotherCaseVar)  // ✅ Accessible in case
default:
    break
}
// Variables from cases are not accessible here
```

### Member Scope

```swift
class Person {
    // Instance properties (accessible within instance methods)
    let name: String
    private var age: Int

    // Type properties (accessible on the type)
    static let species = "Human"

    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    // Instance method
    func getDisplayName() -> String {
        return name  // ✅ Can access instance property
    }

    // Type method
    static func getSpecies() -> String {
        return species  // ✅ Can access type property
        // return name   // ❌ Cannot access instance property
    }

    // Private method
    private func calculateAgeInDays() -> Int {
        return age * 365
    }
}

// Accessing members
let person = Person(name: "Alice", age: 25)
print(person.name)                    // ✅ Public instance property
// print(person.age)                  // ❌ Private instance property

print(Person.species)                 // ✅ Type property
print(Person.getSpecies())            // ✅ Type method

// Extensions can access private members of the same file
extension Person {
    func getAgeInDays() -> Int {
        return calculateAgeInDays()   // ✅ Can access private method
    }
}
```

### Access Control

```swift
// Access control modifiers
public class PublicClass {
    public var publicProperty = "anyone can access"
    internal var internalProperty = "module can access"
    private var privateProperty = "file can access"
}

internal class InternalClass {  // Default access level
    var defaultProperty = "module can access"
}

private class PrivateClass {
    var property = "file can access"
}

// Extensions and subclasses respect access control
extension PublicClass {
    func accessPrivate() {
        print(privateProperty)  // ✅ Same file can access private
    }
}

class Subclass: PublicClass {
    func accessFromSubclass() {
        print(publicProperty)    // ✅ Public accessible
        print(internalProperty)  // ✅ Internal accessible (same module)
        // print(privateProperty) // ❌ Private not accessible
    }
}
```

## Summary

Swift's basic syntax fundamentals provide a clean, expressive, and safe foundation for programming:

**Core Elements:**
- **Expressions and Statements**: Expressions evaluate to values, statements perform actions
- **Comments**: Single-line (`//`), multi-line (`/* */`), and documentation (`///`)
- **Semicolons**: Optional except in specific cases
- **Whitespace**: Proper indentation and spacing for readability

**Code Structure:**
- **Blocks**: Define scope and control flow
- **Identifiers**: Naming conventions and rules
- **Operators**: Arithmetic, comparison, logical, and custom operators
- **Literals**: Representations of values in source code

**Scope and Visibility:**
- **Global Scope**: Accessible throughout the program
- **Local Scope**: Limited to containing blocks
- **Member Scope**: Within classes, structs, and enums
- **Access Control**: `public`, `internal`, `private` modifiers

**Key Principles:**
- **Clarity**: Code should be readable and self-documenting
- **Safety**: Compile-time checks prevent common errors
- **Consistency**: Follow Swift naming and style conventions
- **Expressiveness**: Powerful features with clean syntax

Mastering these fundamentals enables writing clean, maintainable, and efficient Swift code that leverages the language's full potential.
