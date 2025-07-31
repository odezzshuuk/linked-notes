# Class Loader

- [Class Loader](#class-loader)
- [Class Loading Process](#class-loading-process)
- [Run-time Built-in Class Loaders](#run-time-built-in-class-loaders)
- [Class Loader Hierarchy](#class-loader-hierarchy)
- [Class Loader as a Namespace](#class-loader-as-a-namespace)
- [Custom Class Loader](#custom-class-loader)
- [ClassLoader Class](#classloader-class)
- [Module Class](#module-class)

> `ClassLoader` refers to the abstract class of class loaders, while `class loader` refers to the concept of class loaders in Java.

## Introduction

- Because resources are usually packaged with applications or libraries, class loaders are also responsible for locating resources in addition to loading classes.
- Loads classes by identifying their binary names.

> Binary names, for example: "java.lang.String", "javax.swing.JSpinner$DefaultEditor".

- A class loader needs to try to locate or generate the data that defines a class.

> A common practice is to use the class name as a path name and then read the class bytecode from the file system.
> Some classes may also be composed from the network or other applications.

- The class loader returned by `fooArray.getClassLoader()` for an array object is the same as the **Class Loader** of its elements.

## Class Loading Process

Assuming execution starts from the `MyProgram.class` file:

1. Load the [class file](java-class-file.md).
2. If `MyProgram` has a field of a certain type or extends a superclass, those class files will also be loaded.
3. The `main` method in `MyProgram` is executed in the virtual machine, and the classes in the `main` method will also be loaded.

## Run-time Built-in Class Loaders

1. Bootstrap ClassLoader

- Loads **core libraries** from **rt.jar**.
- Core libraries are located in the `$JAVA_HOME/jre/lib` directory.
- **System classes** are usually implemented in C, and there is no corresponding `ClassLoader` object.

2. Extension ClassLoader

- Loads standard extensions from the `$JAVA_HOME/jre/lib/ext` directory.
- By placing a JAR file in the `jre/lib/ext` directory, the extension loader can find the classes within it even without any classpath.

> Placing JAR files containing system classes or extensions in the `jre/lib/ext` directory can cause trouble, as the extension class loader does not use the classpath (CLASSPATH).

3. System ClassLoader

> ~~Mainly refers to **user-defined classes**.~~

- Finds these classes in the classpath set by the `CLASSPATH` environment variable or in the [command-line options](java-command-javac.md).

## Class Loader Hierarchy

- Except for the bootstrap class loader, every class loader has a parent class loader.
- A class loader will first let its parent class loader try to load a given class. Only when the parent class loader fails will the child class loader try to load it.

## Class Loader as a Namespace

## Custom Classloader

- Inherit the `ClassLoader` class and override the `findClass` method.
- Overriding `findClass` must do the following:
  - Load the bytecode for classes from the local file system or other sources.
  - Call the `defineClass()` method of the `ClassLoader` superclass to provide the bytecode to the virtual machine.

## ClassLoader Class

[ClassLoader Class](java-lang-classloader.md)

## Module Class

[Module Class](java-jvm-class-module.md)
