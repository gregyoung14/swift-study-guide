# Enums

## Overview
This section provides a detailed look into enumerations (enums) in Swift, a powerful way to define a common type for a group of related values. We will explore how to declare, use, and extend enums, including associated values, raw values, and recursive enumerations, which are crucial for creating expressive and type-safe code.

## Table of Contents

- [Introduction to Enumerations](#introduction-to-enumerations)
    - [Defining Enums (`enum CompassPoint { ... }`)](#defining-enums-enum-compasspoint)
    - [Enum Case Values (Distinct Cases)](#enum-case-values-distinct-cases)
    - [Enums as Value Types](#enums-as-value-types)
- [Matching Enum Values with `switch` Statements](#matching-enum-values-with-switch-statements)
    - [Exhaustive Cases (Covering All Possibilities)](#exhaustive-cases-covering-all-possibilities)
    - [Using `default` Case](#using-default-case)
    - [Combining Cases](#combining-cases)
    - [Pattern Matching with `if case let` and `guard case let`](#pattern-matching-with-if-case-let-and-guard-case-let)
- [Associated Values](#associated-values)
    - [Defining Enums with Associated Values (Storing Additional Information)](#defining-enums-with-associated-values-storing-additional-information)
    - [Extracting Associated Values](#extracting-associated-values)
    - [Pattern Matching with Associated Values](#pattern-matching-with-associated-values)
- [Raw Values](#raw-values)
    - [Defining Enums with Raw Values (Pre-Populated Values)](#defining-enums-with-raw-values-pre-populated-values)
    - [Implicitly Assigned Raw Values (Integers, Strings)](#implicitly-assigned-raw-values-integers-strings)
    - [Accessing Raw Values (`rawValue`)](#accessing-raw-values-rawvalue)
    - [Initializing from Raw Values (`init?(rawValue:)`)](#initializing-from-raw-values-initrawvalue)
- [Recursive Enumerations](#recursive-enumerations)
    - [Using `indirect` Keyword](#using-indirect-keyword)
    - [Practical Applications (e.g., Tree Structures, Expression Trees)](#practical-applications-eg-tree-structures-expression-trees)
- [Enum as a Data Type (Methods, Properties, Initializers)](#enum-as-a-data-type-methods-properties-initializers)
    - [Methods in Enums (Instance Methods)](#methods-in-enums-instance-methods)
    - [Computed Properties in Enums](#computed-properties-in-enums)
    - [Initializers in Enums](#initializers-in-enums)
    - [Conforming to Protocols](#conforming-to-protocols)
- [Optional Chaining with Enums](#optional-chaining-with-enums)
- [CaseIterable Protocol (Iterating Over All Cases)](#caseiterable-protocol-iterating-over-all-cases)
- [Equatable and Comparable Conformance](#equatable-and-comparable-conformance)
    - [Automatic Conformance](#automatic-conformance)
    - [Custom Conformance](#custom-conformance)
