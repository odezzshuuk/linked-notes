# Annotated Element

## Containing Annotation Interface

The containing annotation interface of an annotation interface A must meet the following conditions:

1. Declare a `value()` method that returns a type of `A[]`.
2. Other methods besides `value()` have default values.
3. The retention period is at least as long as A's.
4. ~~Elements in A are applicable to the corresponding elements within it.~~
5. Corresponds to `java.lang.annotation.Documented` of A.
6. Corresponds to `java.lang.annotation.Inherited` of A.

## Retention Policy

> Specifies the retention period of the annotation.

- CLASS: In class but need not be retained in VM.
- RUNTIME: In class by compiler and at run time in VM.
- SOURCE: Discarded by compiler.

## AnnotatedElement Interface

- An annotated structure of a program running in the current VM.
- Classes that implement the `AnnotatedElement` interface:
  - [x] [AccessibleObject](java-reflect-accessibleobject.md)
  - [x] [Class](java-reflect-class.md)
  - [ ] Constructor
  - [ ] Executable
  - [x] Field
  - [x] Method
  - [ ] Module
  - [ ] Package
  - [ ] Parameter
  - [ ] RecordComponent
- An `AnnotatedElement` on an element is called a declaration annotation.
- An `AnnotatedElement` on a type (class, interface, enum) is called a type annotation.
