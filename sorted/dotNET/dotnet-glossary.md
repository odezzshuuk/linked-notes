# dotNet - Glossary

## .NET SDK

## .NET Core

## .NET Desktop

## ASP.NET Core Runtime

## .NET Runtime

## .NET Framework

- [CLR](#CLR): Common Language Runtime
- [BCL](#BCL): Base Class Library

## BCL

## CLR

- CLR: Common Language Runtime
- **Managed Code**: Code written using the .NET framework is called managed code.
- **Unmanaged Code**: Code that runs outside the control of the CLR (Common Language Runtime), such as Win32 C/C++, is called unmanaged code.
- Services provided by the CLR:
  - Garbage collection
  - Safety and security
  - Code execution, thread management, and exception handling
  - Access to a wide range of programming functionalities through the Base Class Library (BCL), including web services and data services.

## Program Assembly

Features

- Mostly single file, But can be multi-file
- Compiled into CIL, the source code generates an output file called an assembly
- Program Assembly is [executable file](executable-file.md) or DLL
- code in program assembly is not [native code], but a kind of intermediate language called [CIL](#CIL)

Information Contained In the **Program Assembly**

- Manifest
  - Assembly name information, including simple name, version number, public key, etc.
  - List of files composing the assembly
  - List of other assemblies referenced by this assembly
  - A map indicating which types are included in which assembly
- Metadata of the types used in the program
- CIL (Common Intermediate Language) Code
- Metadata referencing other assemblies

## JIT

- Code in the program assembly only compiled by JIT when needed, and the code is only compiled once when called

## CLI

- [CLI](dotnet-cli.md): Common Language Infrastructure

## CIL

- CIL: Common Intermediate Language

## CTS

> Abbreviation for Common Type System.

- Ensures interoperability between different languages that target the .NET platform by providing a common set of rules and guidelines for data types and oprations

Features

- Type Safety
- Metadata
- Unified Type Hierarchy
- Interoperability

## CLS

> Abbreviation for Common Language Specification

- subset of CTS

Features

- Data Types
- Naming Conventions
- Member Accessibility
- Exception Handling
