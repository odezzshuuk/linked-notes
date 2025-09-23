# JAVA - Reflect

## Introduction

Use of Reflection in Java

- analysis class at **runtime**
- access object at **runtime**
- Generic array operation code
- Locate resource position
- ~~Method object, very similar to [function pointers in C++](c++-function-pointer.md)~~

## Feature

- from Java 9, restrictions on the use of reflection have increased, which may cause `InaccessibleException`

## API

Class

[java.lang.Class](java-reflect-class.md)

AccessibleObject

[java.lang.reflect.Field](java-reflect-field.md)

[java.lang.reflect.Method](java-reflect-method.md)

[java.lang.reflect.Constructor](java-reflect-constructor.md)

Modifier

[java.lang.reflect.Modifier](java-reflect-modifier.md): public, private, and other modifiers

Annotation

[java.lang.Annotation](java-reflect-annotation.md)

[annotated element](java-annotated-element.md)

## Implementing a Generic toString() Using Reflection

