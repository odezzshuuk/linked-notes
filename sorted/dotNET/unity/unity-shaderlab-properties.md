# Unity ShaderLab - Properties

## What's For

- Properties that can be adjusted in the inspector
- Can be get or set in c# script with `material.GetColor("_Color")` or `material.SetColor("_Color", color)`

## Property Declaration

`[optional: attribute] name("display name in inspector", type name) = default value`

```sl
Properties
{
    _Color ("Main Color", Color) = (1,1,1,1)
}
```

- `_Color`: the name used in c# script, for example `material.GetColor("_Color")` or `material.SetColor("_Color", color)`
- `Main Color`: Text displayed in inspector
- `Color`: Type of the property
- `"(1, 1, 1 ,1)"`: Default value

## Usage

- In ShaderLab [Command](unity-shaderlab-commands.md)
- In Shader Code

```c
Properties
{
    _Color ("Main Color", Color) = (1,1,1,1)
    _OffsetUnitScale ("Offset Unit Scale", Float) = 1
}
SubShader
{
    Pass
    {
        // Use property in command
        Offset 0, [_OffsetUnitScale]

        CGPROGRAM
        #pragma vertex vert
        #pragma fragment frag
        // ...
        fixed4 _Color;

        fixed4 frag (v2f i) : SV_Target
        {
            return _Color;
        }
        ENDCG
    }
}
```

## Attribute For Property

- `[Gamma]`
- `[HDR]`
- `[HideInInspector]`
- `[MainTexture]`: Property with `[MainTexture]` attribute can be access using `Material.mainTexture` in c# script
- `[MainColor]`: Property with `[MainColor]` attribute can be access using `Material.color` in c# script
- `[NoScaleOffset]`:
- `[Normal]`: A texture property that is used as a normal map
- `[PerRendererData]`
