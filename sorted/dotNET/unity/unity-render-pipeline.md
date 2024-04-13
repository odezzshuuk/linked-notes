# Unity - Render Pipeline

## What It Is

- Takes the objects in a scene and displays them on-screen

## Render Pipeline Steps

1. Culling

- Pipeline decides which objects from the scene to display
- This is means it **removes object that are outside** the camera's view
- Or **hidden behind other** objects

2. Rendering

- Draw the objects with their corrent lighting into [pixel buffer](webgl-shader.md)

3. Post-processing

- Modifies the pixel buffers to generate the final output frame for the display

## Predefined Render Pipeline In Unity

Built-in Render Pipeline

- Default render pipeline in Unity

[Universal Render Pipeline(URP)](unity-universal-render-pipeline.md)

- Prebuilt **Scriptable** Render Pipeline

[High Definition Render Pipeline(HDRP)](unity-high-definition-render-pipeline.md)

- Also Scriptable Render Pipeline
- for high-fidelity graphics on high-end platforms

## How to Choose Pipeline

**Built-in Render Pipeline** 

- is the default choice

**Universal Render Pipeline** 

- Covers most built-in pipeline features
- Especially for tile-based deferred rendering(TBDR) platform
- Need customize the rendering pipeline

**High Definition Render Pipeline**

- need photorealism and high-fidelity rendering on high-end platforms

## Render Pipeline Converter

[Render Pipeline Converter](unity-render-pipeline-converter.md)


