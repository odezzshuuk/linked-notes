# Modeling - Glossary

- [Model](#model)
- [Mesh](#mesh)
- [Material](#material)
- [Texture](#texture)
- [UV Mapping](#uv-mapping)
- [Normal Map](#normal-map)
- [Bump Map](#bump-map)
- [Metallic Map](#metallic-map)

## Model

## Mesh

- structure of interconnected vertices, edges, faces

## Material

- Define how the surface handles the textures and interacts with light
- Languages for createing materials:
  - GLSL
  - HLSL(unity)
  - Shader Graph(unity)

## Texture

- mostly is an image

## UV Mapping

- Mapping a 2D image to a 3D model
- Holds no color information
- Only the relationship between the 2D image and the 3D model

## Normal Map

- A technique used for **faking** the lighting of bumps and dents
- Used to add details **without using more polygons**

![normap](/image/normal-map-example.jpg)

- normal map color explanation
- A normal pointing directly **towards the viewer** (0, 0, -1) is mapped to (128, 128, 255)

> Hence the most common color of a normal map is blue

- A normal pointing to **top right** corner of the texture `(1,1,0)` is mapped to `(255,255,128)`, yellow
- A normal pointing to **right** of the texture (1,0,0) is mapped to (255,128,128)(red)
- A normal pointing to **top** of the texture (0,1,0) is mapped to (128,255,128)(green)
- A normal pointing to **left** of the texture (-1,0,0) is mapped to (0,128,128)(cyan)
- A normal pointing to **bottom** of the texture (0,-1,0) is mapped to (128,0,128)(magenta)
- A normal pointing to **bottom left** corner of the texture (-1,-1,0) is mapped to (0,0,128)(blue)

| Pointing Direction | Normal Vector | Mapped Color    |
| ------------------ | ------------- | --------------- |
| Towards Viewer     | (0, 0, -1)    | (128, 128, 255) |
| Top Right          | (1, 1, 0)     | (255, 255, 128) |
| Right              | (1, 0, 0)     | (255, 128, 128) |
| Top                | (0, 1, 0)     | (128, 255, 128) |
| Left               | (-1, 0, 0)    | (0, 128, 128)   |
| Bottom             | (0, -1, 0)    | (128, 0, 128)   |
| Bottom Left        | (-1, -1, 0)   | (0, 0, 128)     |

## Bump Map

## Metallic Map
