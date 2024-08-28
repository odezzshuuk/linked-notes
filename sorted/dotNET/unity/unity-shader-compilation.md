# Unity Shader - Compilation

## Shader Compilation When Working With Unity Editor

1. when a [shader asset]() imported, it performs some minimal processing
2. When it needs to show a shader variant, it checks `Library/ShaderCache` folder
3. if previously compiled found and identical, it uses the found one
4. if not found, it compiles the shader variant and saves it to `Library/ShaderCache` folder

> `Library/ShaderCache` folder can be quite large, if shaders change frequently. It is safe to delete

## Preprocessor

- Unity shader preprocessor is an optimized preprocessor
- Also called **Caching Shader Preprocessor**

