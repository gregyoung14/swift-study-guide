---
id: 42
---
# Testing with DI

Dependency Injection (DI) is the foundation of high-quality **Unit Testing** in iOS. By externalizing dependencies, you gain the ability to completely control the environment in which your tests run.

## 1. The Setup
To test a class using DI, you follow three steps: **Arrange**, **Act**, and **Assert**.

### The SUT (System Under Test)
This is the class you are currently testing.

### The Collaborators (The Mocks)
These are the protocols you inject into the SUT to simulate different behaviors.

```swift
class ProfileTests: XCTestCase {
    var sut: ProfileViewModel!
    var mockAPI: MockAPI!
    
    override func setUp() {
        super.setUp()
        // Arrange
        mockAPI = MockAPI()
        sut = ProfileViewModel(api: mockAPI)
    }
}
```

## 2. Simulating Success vs. Failure
With DI, you can test how your app handles errors without needing to actually disconnect your Wi-Fi or break your server.

```swift
func test_fetch_withError_showsAlert() {
    // 1. Force the dependency to fail
    mockAPI.shouldFail = true
    
    // 2. Act
    sut.loadData()
    
    // 3. Assert
    XCTAssertTrue(sut.isShowingErrorAlert)
}
```

## 3. Testing Side Effects (Spies)
Use a "Spy" to verify that a class is talking to its dependencies correctly.

```swift
func test_logout_clearsKeychain() {
    // Act
    sut.logout()
    
    // Assert: Verify that the dependency was called
    XCTAssertTrue(mockKeychain.clearWasCalled)
}
```

## Testability Benefits Summary

| Feature | Impact on Testing |
| :--- | :--- |
| **Isolation** | Test one class at a time, not the whole graph. |
| **Speed** | Tests run in RAM, no disk or network I/O. |
| **Determinism** | No "flaky" tests due to environment state. |
| **Confidence** | You can test 100% of the code branches easily. |

## Visualization: The Test Sandbox
```mermaid
graph LR
    subgraph "Test Suite"
        SUT[ViewModel]
        M1[Mock API]
        M2[Mock DB]
    end
    
    SUT --> M1
    SUT --> M2
    Note right of M1: Controlled Output
```

## Summary
Unit testing is a competitive advantage for any mobile engineering team. It allows for faster releases and fewer regressions. By embracing Dependency Injection, you transform your codebase into a "modular laboratory" where every scenario can be tested with precision.
