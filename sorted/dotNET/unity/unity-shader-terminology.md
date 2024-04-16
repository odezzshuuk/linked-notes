# Unity - Shader Terminology

* [Shader Program](#shader-program)
* [Shader Class](#shader-class)
* [Shader Object](#shader-object)
* [Shader Lab](#shader-lab)
* [Shader Graph](#shader-graph)
* [Shader Asset](#shader-asset)
* [Shader Graph Asset](#shader-graph-asset)

## Shader Program

- A program that runs on a GPU

## Shader Class

A class used to write scripts for shader

- Mostly used **just** to check whether a shader is supported on hardware
- Which means shader class can't control the details of the shader

## Shader Object

what's this

- An instance of [`Shader`]() class

what's inside

- Information about the shader
- An optional fallback Shader object
- One or more SubShaders

2 ways for create Shader Object

> it's NOT created by [unity script](unity-script.md)

- write shader code with .shader extension
- use [Shader Graph](#shader-graph)

## Shader Lab

## Shader Graph

A tool for creating shaders without writing code

## Shader Asset

A file with the .shader extension

## Shader Graph Asset

A file define a shader object



