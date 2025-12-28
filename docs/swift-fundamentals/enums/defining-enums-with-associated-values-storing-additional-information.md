---
id: 894
---
# Defining Enums with Associated Values

**Associated Values** allow you to store additional information of any type along with an enum case. This makes enums incredibly powerful for representing state and data simultaneously.

## 1. Syntax and Usage
You define associated values by placing a tuple of type names after the case name.

```swift
enum Barcode {
    case upc(Int, Int, Int, Int)
    case qrCode(String)
}
```

In this example, a `Barcode` can be *either* a UPC with four integer segments *or* a QR code with a string.

## 2. Creating Instances
When you create a case, you provide the specific values:

```swift
var productBarcode = Barcode.upc(8, 85909, 51226, 3)
productBarcode = .qrCode("ABCDEFGHIJKLMNOP")
```

## 3. Extracting Associated Values
You use a `switch` statement or `if case let` to "extract" the stored values.

### Using Switch
```swift
switch productBarcode {
case .upc(let numberSystem, let manufacturer, let product, let check):
    print("UPC: \(numberSystem), \(manufacturer), \(product), \(check).")
case .qrCode(let productCode):
    print("QR Code: \(productCode).")
}
```

### Using Shorthand (if case let)
```swift
if case let .qrCode(code) = productBarcode {
    print("Scanned QR: \(code)")
}
```

## 4. Real-World Example: Network Response
Associated values are perfect for representing the result of an operation that can succeed with data or fail with an error.

```swift
enum NetworkResult {
    case success(data: Data, code: Int)
    case failure(Error)
}

let result: NetworkResult = .success(data: Data(), code: 200)

switch result {
case .success(let data, let code):
    print("Received data of size \(data.count) with status \(code)")
case .failure(let error):
    print("Error: \(error.localizedDescription)")
}
```

> [!IMPORTANT]
> A case can have **multiple** associated values with labels, making the code more readable:
> `case user(id: UUID, name: String, email: String)`
