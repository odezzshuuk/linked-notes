# Rust - AsRef vs Deref

## Differences

For `*` operator

- If a type implements `AsRef<T>` but not `Deref<Target=T>`, `*` operator cannot be used to dereference it to `T`

State

- `AsRef<T>` is used **explicitly** by calling `as_ref()` method.
- `Deref` is used **implicitly**.

Number Of Convert Target

- `AsRef<T>` can be implemented for any type to convert it to a reference of type `&T`
- `Deref`: there is always one unambiguous type to convert
 
Where they are used

- `AsRef` mainly for API design
- `Deref` mainly for smart pointer types 

## When And When Not For AsRef

[As Trait bound or parameter annotation](rust-asref#as-trait-bound-or-parameter)

[Not just for dereferencing](rust-asref#what-asref-should-not-used-to)

## When And When Not For Deref

[When Deref Is Appropriate](rust-deref-trait.md#when-deref-is-appropriate)

[When Deref Is Anti-pattern](rust-deref-trait.md#when-deref-is-anti-pattern)

## How to Decide

- Do you want ALL methods of the inner type to be callable?
  - Yes: Does the type enforce invariants or restrict the API
    - Yes: Don't impl Deref. For example `String` but `Email` type
    - No: Impl Deref. For example `String` but `Hostname` type or smart pointer
  - No: Don't impl Deref, use AsRef

