---
id: 732
---
﻿# Accessing and Modifying Values (Subscript, Update Value)

## Overview

Dictionaries in Swift provide powerful and safe methods for accessing and modifying key-value pairs. This section covers subscript syntax, update operations, and best practices for dictionary manipulation with comprehensive examples and error handling patterns.

## Table of Contents

- [Dictionary Subscript Access](#dictionary-subscript-access)
- [Safe Dictionary Access](#safe-dictionary-access)
- [Updating Values](#updating-values)
- [Adding and Modifying Entries](#adding-and-modifying-entries)
- [Removing Entries](#removing-entries)
- [Bulk Operations](#bulk-operations)
- [Default Values](#default-values)
- [Advanced Patterns](#advanced-patterns)

## Dictionary Subscript Access

### Basic Subscript Operations

```swift
// Dictionary declaration and basic access
var userInfo: [String: String] = [
    "name": "John Doe",
    "email": "john@example.com",
    "city": "New York"
]

// Access values using subscript
let name = userInfo["name"]          // Optional("John Doe")
let email = userInfo["email"]        // Optional("john@example.com")
let phone = userInfo["phone"]        // nil (key doesn't exist)

print(name ?? "Name not found")      // "John Doe"
print(phone ?? "Phone not found")    // "Phone not found"
```

### Subscript Modification

```swift
// Modify values using subscript
var scores = ["Alice": 85, "Bob": 92, "Charlie": 78]

// Update existing value
scores["Alice"] = 90                 // ["Alice": 90, "Bob": 92, "Charlie": 78]

// Add new key-value pair
scores["David"] = 88                 // ["Alice": 90, "Bob": 92, "Charlie": 78, "David": 88]

// Attempt to access non-existent key (returns nil)
let missingScore = scores["Eve"]     // nil
print(missingScore ?? "Score not found") // "Score not found"

// Set value for non-existent key
scores["Eve"] = 95                   // ["Alice": 90, "Bob": 92, "Charlie": 78, "David": 88, "Eve": 95]
```

### Subscript with Complex Types

```swift
// Dictionary with complex value types
struct UserProfile {
    let id: UUID
    var name: String
    var age: Int
    var preferences: [String: Any]
}

var users: [String: UserProfile] = [:]

// Add user profile
let userID = "user123"
users[userID] = UserProfile(
    id: UUID(),
    name: "Alice Johnson",
    age: 28,
    preferences: ["theme": "dark", "notifications": true]
)

// Access nested properties
if let user = users[userID] {
    print("User: \(user.name), Age: \(user.age)")
    print("Theme: \(user.preferences["theme"] ?? "light")")
}

// Modify nested properties
users[userID]?.preferences["language"] = "en"
users[userID]?.age = 29

print(users[userID]?.preferences) // ["theme": "dark", "notifications": true, "language": "en"]
```

## Safe Dictionary Access

### Optional Binding

```swift
// Safe access with optional binding
let configuration = [
    "apiEndpoint": "https://api.example.com",
    "timeout": "30",
    "retries": "3"
]

// Safe access pattern
if let endpoint = configuration["apiEndpoint"] {
    print("API Endpoint: \(endpoint)")
} else {
    print("API Endpoint not configured")
}

if let timeoutString = configuration["timeout"],
   let timeout = Int(timeoutString) {
    print("Timeout: \(timeout) seconds")
} else {
    print("Invalid or missing timeout")
}

// Multiple keys with guard
func configureNetwork() -> Bool {
    guard let endpoint = configuration["apiEndpoint"],
          let timeoutString = configuration["timeout"],
          let timeout = Int(timeoutString),
          let retriesString = configuration["retries"],
          let retries = Int(retriesString) else {
        print("Invalid network configuration")
        return false
    }

    // Configure network with validated values
    print("Network configured: \(endpoint), timeout: \(timeout), retries: \(retries)")
    return true
}
```

### Custom Safe Access Extensions

```swift
// Custom safe access methods
extension Dictionary where Key == String {
    /// Safely get value and attempt type conversion
    func safeValue<T>(_ key: Key) -> T? {
        return self[key] as? T
    }

    /// Get value with type conversion and default
    func value<T>(_ key: Key, default defaultValue: T) -> T {
        return safeValue(key) ?? defaultValue
    }

    /// Get value with type conversion or throw
    func requiredValue<T>(_ key: Key) throws -> T {
        guard let value: T = safeValue(key) else {
            throw ConfigurationError.missingKey(key)
        }
        return value
    }
}

enum ConfigurationError: Error {
    case missingKey(String)
    case invalidType(expected: String, actual: String)
}

// Usage
let config = [
    "port": "8080",
    "debug": "true",
    "maxConnections": "100"
]

// Safe access with type conversion
let port: Int? = config.safeValue("port")          // 8080
let debug: Bool? = config.safeValue("debug")       // true
let maxConn: Int? = config.safeValue("maxConnections") // 100
let missing: String? = config.safeValue("host")    // nil

// With defaults
let timeout = config.value("timeout", default: 30) // 30
let enabled = config.value("enabled", default: false) // false

// Required values (throwing)
do {
    let requiredPort: Int = try config.requiredValue("port")
    print("Port: \(requiredPort)")
} catch {
    print("Configuration error: \(error)")
}
```

### Nested Dictionary Access

```swift
// Safe access for nested dictionaries
typealias JSON = [String: Any]

let response: JSON = [
    "user": [
        "profile": [
            "name": "John Doe",
            "preferences": [
                "theme": "dark",
                "language": "en"
            ]
        ],
        "stats": [
            "posts": 42,
            "followers": 1234
        ]
    ]
]

// Safe nested access
func getNestedValue<T>(_ dict: JSON, path: [String]) -> T? {
    var current: Any = dict

    for key in path {
        guard let nested = current as? JSON,
              let next = nested[key] else {
            return nil
        }
        current = next
    }

    return current as? T
}

// Usage
let userName: String? = getNestedValue(response, path: ["user", "profile", "name"])
let theme: String? = getNestedValue(response, path: ["user", "profile", "preferences", "theme"])
let posts: Int? = getNestedValue(response, path: ["user", "stats", "posts"])

print("User: \(userName ?? "Unknown")")     // "John Doe"
print("Theme: \(theme ?? "light")")         // "dark"
print("Posts: \(posts ?? 0)")               // 42
```

## Updating Values

### Direct Assignment

```swift
// Direct value updates
var inventory = [
    "apples": 50,
    "bananas": 25,
    "oranges": 30
]

// Update existing values
inventory["apples"] = 45    // Reduce apple count
inventory["bananas"] = 30   // Increase banana count

// Add new items
inventory["grapes"] = 20    // Add new item

print(inventory)
// ["oranges": 30, "grapes": 20, "bananas": 30, "apples": 45]
```

### Update with Current Value

```swift
// Update based on current value
var scores = ["Math": 85, "English": 92, "Science": 78]

// Add bonus points to all scores
for (subject, currentScore) in scores {
    scores[subject] = currentScore + 5
}
// ["Math": 90, "English": 97, "Science": 83]

// Double scores above 90
for subject in scores.keys where scores[subject]! > 90 {
    scores[subject]! *= 2
}
// ["Math": 90, "English": 194, "Science": 83]
```

### Functional Updates

```swift
// Functional approach to updates
let grades = ["A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0]

// Create new dictionary with updated values
let curvedGrades = grades.mapValues { grade in
    grade + 0.5  // Add curve
}
// ["A": 4.5, "B": 3.5, "C": 2.5, "D": 1.5]

// Update conditionally
var studentRecords = [
    "alice": ["grade": "A", "credits": 30],
    "bob": ["grade": "B", "credits": 25],
    "charlie": ["grade": "A", "credits": 28]
]

// Add extra credit for students with grade A
for (student, record) in studentRecords where record["grade"] == "A" {
    studentRecords[student]!["extraCredit"] = 5
}

print(studentRecords)
// ["bob": ["grade": "B", "credits": 25], "alice": ["grade": "A", "credits": 30, "extraCredit": 5], "charlie": ["grade": "A", "credits": 28, "extraCredit": 5]]
```

## Adding and Modifying Entries

### Conditional Addition

```swift
// Add entries only if they don't exist
var userSettings: [String: Any] = [
    "theme": "dark",
    "fontSize": 14
]

// Add default values for missing settings
let defaults = [
    "theme": "light",        // Won't override existing
    "fontSize": 12,          // Won't override existing
    "showToolbar": true,     // Will be added
    "autoSave": false        // Will be added
]

for (key, defaultValue) in defaults {
    if userSettings[key] == nil {
        userSettings[key] = defaultValue
    }
}

print(userSettings)
// ["theme": "dark", "fontSize": 14, "showToolbar": true, "autoSave": false]
```

### Merge Operations

```swift
// Merge dictionaries
var baseConfig = [
    "host": "localhost",
    "port": 8080,
    "debug": false
]

let overrideConfig = [
    "host": "production.example.com",  // Override
    "ssl": true                        // Add new
]

// Manual merge
var mergedConfig = baseConfig
for (key, value) in overrideConfig {
    mergedConfig[key] = value
}

// Result: ["host": "production.example.com", "port": 8080, "debug": false, "ssl": true]
```

### Bulk Modifications

```swift
// Bulk add/modify operations
var productInventory = [
    "widget": ["price": 10.99, "stock": 50],
    "gadget": ["price": 25.50, "stock": 30]
]

// Apply discount to all products
for (product, details) in productInventory {
    if var productDetails = details as? [String: Any] {
        if let currentPrice = productDetails["price"] as? Double {
            productDetails["price"] = currentPrice * 0.9  // 10% discount
            productInventory[product] = productDetails
        }
    }
}

// Add category to all products
let categories = ["widget": "electronics", "gadget": "tools"]
for (product, _) in productInventory {
    if let category = categories[product] {
        productInventory[product]!["category"] = category
    }
}

print(productInventory)
// ["widget": ["price": 9.891, "stock": 50, "category": "electronics"], "gadget": ["price": 22.95, "stock": 30, "category": "tools"]]
```

## Removing Entries

### Remove by Key

```swift
// Remove specific entries
var userProfiles = [
    "user1": ["name": "Alice", "age": 25],
    "user2": ["name": "Bob", "age": 30],
    "user3": ["name": "Charlie", "age": 35],
    "user4": ["name": "Diana", "age": 28]
]

// Remove single entry
let removedProfile = userProfiles.removeValue(forKey: "user2")
// removedProfile = Optional(["name": "Bob", "age": 30])
// userProfiles = ["user1": [...], "user3": [...], "user4": [...]]

// Remove and return value
if let removed = userProfiles.removeValue(forKey: "user4") {
    print("Removed user: \(removed["name"] ?? "Unknown")")
}

// Attempt to remove non-existent key
let nonExistent = userProfiles.removeValue(forKey: "user5")
// nonExistent = nil (no error thrown)
```

### Conditional Removal

```swift
// Remove entries based on conditions
var orders = [
    "order1": ["status": "completed", "amount": 99.99],
    "order2": ["status": "pending", "amount": 49.99],
    "order3": ["status": "cancelled", "amount": 29.99],
    "order4": ["status": "completed", "amount": 149.99]
]

// Remove cancelled orders
orders = orders.filter { (_, order) in
    (order as? [String: Any])?["status"] as? String != "cancelled"
}

// Remove orders under $50
orders = orders.filter { (_, order) in
    (order as? [String: Any])?["amount"] as? Double ?? 0 >= 50.0
}

print(orders)
// ["order1": ["status": "completed", "amount": 99.99], "order4": ["status": "completed", "amount": 149.99]]
```

### Bulk Removal

```swift
// Remove multiple keys at once
var data = [
    "name": "John",
    "age": 30,
    "email": "john@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St",
    "city": "Anytown",
    "zipCode": "12345"
]

// Remove sensitive information
let sensitiveKeys = ["phone", "address", "zipCode"]
for key in sensitiveKeys {
    data.removeValue(forKey: key)
}

print(data)
// ["name": "John", "age": 30, "email": "john@example.com", "city": "Anytown"]
```

## Bulk Operations

### Dictionary Merging

```swift
// Advanced merging operations
func mergeDictionaries(_ base: [String: Any], _ override: [String: Any]) -> [String: Any] {
    var result = base
    for (key, value) in override {
        if let existingDict = result[key] as? [String: Any],
           let overrideDict = value as? [String: Any] {
            // Deep merge for nested dictionaries
            result[key] = mergeDictionaries(existingDict, overrideDict)
        } else {
            // Direct replacement
            result[key] = value
        }
    }
    return result
}

// Usage
let baseSettings = [
    "ui": ["theme": "light", "fontSize": 14],
    "network": ["timeout": 30]
]

let userSettings = [
    "ui": ["theme": "dark"],
    "notifications": ["enabled": true]
]

let merged = mergeDictionaries(baseSettings, userSettings)
print(merged)
// ["ui": ["theme": "dark", "fontSize": 14], "network": ["timeout": 30], "notifications": ["enabled": true]]
```

### Transform Operations

```swift
// Transform dictionary values
let rawData = [
    "temperature": "23.5",
    "humidity": "65",
    "pressure": "1013.25"
]

// Convert string values to appropriate types
let processedData = rawData.compactMapValues { stringValue in
    Double(stringValue)
}
// ["temperature": 23.5, "humidity": 65.0, "pressure": 1013.25]

// Transform keys and values
let apiResponse = [
    "user_name": "john_doe",
    "user_age": "30",
    "user_email": "john@example.com"
]

let transformed = apiResponse.reduce(into: [String: Any]()) { result, pair in
    let (key, value) = pair

    // Transform snake_case to camelCase
    let camelCaseKey = key.replacingOccurrences(of: "_([a-z])", with: "$1".uppercased(), options: .regularExpression)

    // Attempt type conversion
    if let intValue = Int(value) {
        result[camelCaseKey] = intValue
    } else {
        result[camelCaseKey] = value
    }
}

print(transformed)
// ["userName": "john_doe", "userAge": 30, "userEmail": "john@example.com"]
```

## Default Values

### Subscript with Default

```swift
// Custom subscript with default values
extension Dictionary {
    subscript(key: Key, default defaultValue: Value) -> Value {
        get { self[key] ?? defaultValue }
        set { self[key] = newValue }
    }
}

// Usage
var settings: [String: Any] = ["theme": "dark"]

let fontSize = settings["fontSize", default: 12] as? Int  // 12
let showIcons = settings["showIcons", default: true] as? Bool  // true

// Setting values with subscript
settings["fontSize", default: 12] = 14
settings["showIcons", default: true] = false

print(settings)
// ["theme": "dark", "fontSize": 14, "showIcons": false]
```

### Default Value Patterns

```swift
// Common default value patterns
struct Configuration {
    private var values: [String: Any]

    init(values: [String: Any] = [:]) {
        self.values = values
    }

    // String defaults
    var appName: String { values["appName"] as? String ?? "MyApp" }
    var version: String { values["version"] as? String ?? "1.0.0" }

    // Numeric defaults
    var port: Int { values["port"] as? Int ?? 8080 }
    var timeout: TimeInterval { values["timeout"] as? TimeInterval ?? 30.0 }

    // Boolean defaults
    var debugMode: Bool { values["debugMode"] as? Bool ?? false }
    var enableLogging: Bool { values["enableLogging"] as? Bool ?? true }

    // Array defaults
    var supportedFormats: [String] {
        values["supportedFormats"] as? [String] ?? ["json", "xml"]
    }

    // Dictionary defaults
    var defaultHeaders: [String: String] {
        values["defaultHeaders"] as? [String: String] ?? ["Content-Type": "application/json"]
    }
}

// Usage
let config1 = Configuration()  // All defaults
let config2 = Configuration(values: ["appName": "CustomApp", "port": 9000])

print(config1.appName)  // "MyApp"
print(config2.appName)  // "CustomApp"
print(config2.port)     // 9000
print(config2.debugMode) // false (default)
```

## Advanced Patterns

### Computed Dictionary Properties

```swift
// Dictionary with computed properties
class UserPreferences {
    private var storage: [String: Any] = [:]

    // Computed properties with defaults
    var theme: String {
        get { storage["theme"] as? String ?? "system" }
        set { storage["theme"] = newValue }
    }

    var fontSize: Double {
        get { storage["fontSize"] as? Double ?? 14.0 }
        set { storage["fontSize"] = newValue }
    }

    var notificationsEnabled: Bool {
        get { storage["notificationsEnabled"] as? Bool ?? true }
        set { storage["notificationsEnabled"] = newValue }
    }

    // Computed array property
    var favoriteCategories: [String] {
        get { storage["favoriteCategories"] as? [String] ?? [] }
        set { storage["favoriteCategories"] = newValue }
    }

    // Subscript for direct access
    subscript(key: String) -> Any? {
        get { storage[key] }
        set { storage[key] = newValue }
    }
}

// Usage
let prefs = UserPreferences()
prefs.theme = "dark"
prefs["customSetting"] = "value"

print(prefs.theme)           // "dark"
print(prefs.fontSize)        // 14.0 (default)
print(prefs["customSetting"]) // "value"
```

### Dictionary Composition

```swift
// Compose dictionaries from multiple sources
protocol ConfigurationProvider {
    var configuration: [String: Any] { get }
}

class AppConfiguration {
    private var providers: [ConfigurationProvider]

    init(providers: [ConfigurationProvider]) {
        self.providers = providers
    }

    var configuration: [String: Any] {
        var result: [String: Any] = [:]

        // Later providers override earlier ones
        for provider in providers {
            for (key, value) in provider.configuration {
                result[key] = value
            }
        }

        return result
    }
}

// Configuration providers
class DefaultConfiguration: ConfigurationProvider {
    var configuration: [String: Any] = [
        "theme": "light",
        "fontSize": 14,
        "debugMode": false
    ]
}

class UserConfiguration: ConfigurationProvider {
    var configuration: [String: Any] = [
        "theme": "dark",
        "fontSize": 16
    ]
}

class EnvironmentConfiguration: ConfigurationProvider {
    var configuration: [String: Any] {
        var config: [String: Any] = [:]

        if let portString = ProcessInfo.processInfo.environment["PORT"],
           let port = Int(portString) {
            config["port"] = port
        }

        if let debugString = ProcessInfo.processInfo.environment["DEBUG"],
           let debug = Bool(debugString) {
            config["debugMode"] = debug
        }

        return config
    }
}

// Usage
let appConfig = AppConfiguration(providers: [
    DefaultConfiguration(),
    UserConfiguration(),
    EnvironmentConfiguration()
])

print(appConfig.configuration)
// Merged configuration with proper precedence
```

### Validation and Type Safety

```swift
// Dictionary with validation
struct ValidatedDictionary {
    private var storage: [String: Any] = [:]
    private let validators: [String: (Any) -> Bool]

    init(validators: [String: (Any) -> Bool] = [:]) {
        self.validators = validators
    }

    func setValue(_ value: Any, forKey key: String) throws {
        if let validator = validators[key], !validator(value) {
            throw ValidationError.invalidValue(key: key, value: value)
        }
        storage[key] = value
    }

    func value<T>(forKey key: String) -> T? {
        return storage[key] as? T
    }

    subscript<T>(key: String) -> T? {
        get { value(forKey: key) }
        set {
            if let newValue = newValue {
                try? setValue(newValue, forKey: key)
            } else {
                storage.removeValue(forKey: key)
            }
        }
    }
}

enum ValidationError: Error {
    case invalidValue(key: String, value: Any)
}

// Usage
var config = ValidatedDictionary(validators: [
    "port": { value in (value as? Int).map { $0 > 0 && $0 < 65536 } ?? false },
    "timeout": { value in (value as? TimeInterval).map { $0 > 0 } ?? false }
])

try config.setValue(8080, forKey: "port")       // Success
try config.setValue(-1, forKey: "port")         // Throws ValidationError

config["timeout"] = 30.0                        // Success
config["invalid"] = "value"                     // No validator, succeeds

print(config.value(forKey: "port") as Int?)     // 8080
print(config.value(forKey: "timeout") as TimeInterval?) // 30.0
```

### Summary

Swift dictionaries provide comprehensive methods for accessing and modifying key-value pairs:

**Safe Access Patterns:**
- Optional subscript returns `nil` for missing keys
- Optional binding for safe value extraction
- Custom extensions for type-safe access
- Nested dictionary traversal

**Modification Operations:**
- Direct subscript assignment for updates and additions
- `updateValue(_:forKey:)` returns old value
- Bulk operations with merging and transformation
- Conditional updates based on current values

**Advanced Patterns:**
- Default value subscripts
- Validation and type safety
- Dictionary composition from multiple sources
- Computed properties for complex access patterns

**Best Practices:**
- Use optional binding instead of force unwrapping
- Implement custom subscripts for safe access
- Validate dictionary contents when necessary
- Use functional operations for bulk transformations
- Consider performance implications of different access patterns

These patterns ensure safe, efficient, and maintainable dictionary operations throughout Swift applications.
