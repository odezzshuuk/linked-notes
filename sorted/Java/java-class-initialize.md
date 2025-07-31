# Initialization

## Constructor

[Constructor](java-class-constructor.md)

## Field

[Field Initialization](java-class-field-initialize.md)

## Steps when calling a constructor

1. All data is initialized to its default value (0, false, or null).
2. All [field initialization statements and initialization blocks](java-class-field-initialize.md) are executed in the order they appear in the class declaration.
3. The other constructor called in the first line is invoked.
4. The body of the constructor is executed.
