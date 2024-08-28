# Unity ShaderLab - Package Requirements


```sl
Shader "Foo/ShaderName"
{
    SubShader
    {
        PackageRequirements
        {
            "com.unity.render-pipelines.core" = "7.1.8"
        }
        Pass
        {
            PackageRequirements
            {
                "com.unity.render-pipelines.universal": "[10.2.1,11.0]"
                "com.unity.textmeshpro": "3.2"
            }
        }
        Pass
        {
            PackageRequirements
            {
                "com.unity.render-pipelines.high-definition": "10.2.1"
            }
        }
    }
}
```
