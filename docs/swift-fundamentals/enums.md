# Enums

## Overview
This section provides a detailed look into enumerations (enums) in Swift, a powerful way to define a common type for a group of related values. We will explore how to declare, use, and extend enums, including associated values, raw values, and recursive enumerations, which are crucial for creating expressive and type-safe code.

## Table of Contents

- [Introduction to Enumerations](enums/introduction-to-enumerations.md)
    - [Defining Enums (`enum CompassPoint { ... }`)](enums/defining-enums-enum-compasspoint.md)
    - [Enum Case Values (Distinct Cases)](enums/enum-case-values-distinct-cases.md)
    - [Enums as Value Types](enums/enums-as-value-types.md)
- [Matching Enum Values with `switch` Statements](enums/matching-enum-values-with-switch-statements.md)
    - [Exhaustive Cases (Covering All Possibilities)](enums/exhaustive-cases-covering-all-possibilities.md)
    - [Using `default` Case](enums/using-default-case.md)
    - [Combining Cases](enums/combining-cases.md)
    - [Pattern Matching with `if case let` and `guard case let`](enums/pattern-matching-with-if-case-let-and-guard-case-let.md)
- [Associated Values](enums/associated-values.md)
    - [Defining Enums with Associated Values (Storing Additional Information)](enums/defining-enums-with-associated-values-storing-additional-information.md)
    - [Extracting Associated Values](enums/extracting-associated-values.md)
    - [Pattern Matching with Associated Values](enums/pattern-matching-with-associated-values.md)
- [Raw Values](enums/raw-values.md)
    - [Defining Enums with Raw Values (Pre-Populated Values)](enums/defining-enums-with-raw-values-pre-populated-values.md)
    - [Implicitly Assigned Raw Values (Integers, Strings)](enums/implicitly-assigned-raw-values-integers-strings.md)
    - [Accessing Raw Values (`rawValue`)](enums/accessing-raw-values-rawvalue.md)
    - [Initializing from Raw Values (`init?(rawValue:)`)](enums/initializing-from-raw-values-initrawvalue.md)
- [Recursive Enumerations](enums/recursive-enumerations.md)
    - [Using `indirect` Keyword](enums/using-indirect-keyword.md)
    - [Practical Applications (e.g., Tree Structures, Expression Trees)](enums/practical-applications-eg-tree-structures-expression-trees.md)
- [Enum as a Data Type (Methods, Properties, Initializers)](enums/enum-as-a-data-type-methods-properties-initializers.md)
    - [Methods in Enums (Instance Methods)](enums/methods-in-enums-instance-methods.md)
    - [Computed Properties in Enums](enums/computed-properties-in-enums.md)
    - [Initializers in Enums](enums/initializers-in-enums.md)
    - [Conforming to Protocols](enums/conforming-to-protocols.md)
- [Optional Chaining with Enums](enums/optional-chaining-with-enums.md)
- [CaseIterable Protocol (Iterating Over All Cases)](enums/caseiterable-protocol-iterating-over-all-cases.md)
- [Equatable and Comparable Conformance](enums/equatable-and-comparable-conformance.md)
    - [Automatic Conformance](enums/automatic-conformance.md)
    - [Custom Conformance](enums/custom-conformance.md)
