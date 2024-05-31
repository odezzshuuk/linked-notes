# Unity - Assembly Definition

* [What's For](#what's-for)
* [Defining Assembly](#defining-assembly)
* [Assembly Definition File](#assembly-definition-file)
* [Assembly Reference](#assembly-reference)

## What's For

- increase build speed

## Defining Assembly

Directory Structure

```
Assets
└── Scripts 
    ├── Editor
    │   ├── Synaptafin.Editor.asmdef
    │   ├── SubEditor
    │   │   ├── A1.cs
    │   │   └── B1.cs
    │   ├── A.cs
    │   ├── B.cs
    │   ├── C.cs
    │   └── D.cs
    ├── Runtime
    │   ├── Synaptafin.Runtime.asmdef
    │   ├── E.cs
    │   ├── F.cs
    │   ├── G.cs
    │   └── H.cs
    └── RuntimeExtra
        ├── Synaptafin.RuntimeExtra.asmref
        ├── I.cs
        ├── J.cs
        ├── K.cs
        └── L.cs
```

- takes all of the scripts in a folder that contains an [assembly definition file](#assembly-definition-file) and compiles them into a separate assembly
- Also include child folders unless child folder has its own [assembly definition] or [assembly reference](#assembly-reference-file)

> File Synaptafin.Editor.asmdef include all scripts in the Editor folder and its child folders

- To include scripts from a **non-child folder** in an existing assembly, create [assembly reference] asset

> Open file Synaptafin.RuntimeExtra.asmref [inspector]() then link Synaptafin.Runtime.asmdef to reference the assembly
> then all scripts in the RuntimeExtra folder will be included in the assembly defined by `Synaptafin.Runtime.asmdef`

## Assembly Definition File

- `.asmdef` file

## Assembly Reference File

- `.asmref` file


