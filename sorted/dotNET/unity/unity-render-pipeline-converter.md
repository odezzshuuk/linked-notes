# Unity - Render Pipeline Converter

## What's For

- convert assets built-in Render pipeline to URP or HDRP

> the conversion is irreversible 

## 5 types converters

1. Rendering Settings

- Create URP Asset and [Renderer](unity-renderer.md) assets
- Convert settings in built-in render pipeline to equivalent properties in URP

2. [Materials]() Upgrade

- convert [materials](unity-material.md)
- Works on **pre-built materials** supplied by Unity
- Not support materials with **custom shaders**

3. Animation Clip Converter

- convert the [animation]() clip

4. Read-Only Material Converter

- convert where materials upgrade converter cannot replace the [shader](unity-shader.md)
- read-only materials such as `Default-Diffuse`, `Default-Line`, `Default-Terrain-Diffuse`, ...

5. Post-Processing v2 Converter

- convert [PPv2 Volumes](), [Profiles](), and Layers to [URP Volumes](), Profiles, and Cameras

## Converion Using API

- Class `UnityEditor.Rendering.Universal.Converters`

```cs
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.Rendering.Universal;
using UnityEngine;

public class MyUpgradeScript : MonoBehaviour
{
    public static void ConvertBuiltinToURPMaterials()
    {
        Converters.RunInBatchMode(
            ConverterContainerId.BuiltInToURP
            , new List<ConverterId> {
                ConverterId.Material,
                ConverterId.ReadonlyMaterial
            }
            , ConverterFilter.Inclusive
        );
        EditorApplication.Exit(0);
    }
}
```

