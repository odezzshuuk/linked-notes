# Java - Module

- A directory containing module-info.class (compiled from module-info.java)
- The module-info.java file should contain
  - Declaration of the module name
  - List of packages exported by the module (to allow reuse by other modules);
  - List of other modules required by this module (to reuse their exported packages).
- Organize packages into a module, which is represented by one or more package directories
  - One of the directories contains the module-info.java file
  - Convenient but not required
- The development environment may name directories after the module name
- Project-level directory
- The module can be packaged as a `.jar` archive
- A module is a set of packages designed for reuse

> For Example:
> module a.b.c represents the `a.b.c` directory of the entire system
> The declaration of the module is represented by the module-info.java file under the a.b.c directory.
> For a package `p.q.r` in the module, module `a.b.c` contains the directory tree p/q/r

## Create A Module

Create a module named moduleA

1. Create a moduleA folder
2. Create `module-info.java` with the following content:

```java
module moduleA {}
```
3. Add sample code to the module, placed in moduleA/com/company/demomodule directory

```java
package com.company.demomodule;

public class DemoClass{
    public static void main(String[] args) {
        System.out.println("A module demo");
    }
}
```

4. Compile the module, specify the output directory for class files, and specify the source files

5. Run the module, execute the main class in the module

## keyword: module

- For declare a module

```java
module com.company.mymodule {
}
```

## keyword: requires

```java
module java.desktop{ 
    requires java.xml;
}
```

## keyword: transitive

- Force reading dependencies

```java
module java.desktop{
    requires transitive module_name;
}
```

- Any module that reads the java.desktop module will also be forced to read the java.xml module

## keyword: Exports

## keyword: Uses

## Related Command

### javac Command

- `--add-modules module, module`

Specify the path

- `--module-path path` or `-p path`: Specify where to find the application's module-path
- `--module-source-path`: Specify the module source file path

### java Command

- `-m` or `--module module[/mainclass]`: Execute the main class in the module
- `--module-path path` or `-p path`: Specify the module-path
  - Use `;` to separate multiple directories
