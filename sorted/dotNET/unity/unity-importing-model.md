# Unity - Importing Model

## File Format

1. `.fbx`
2. `.dae`
3. `.dxf`
4. `.obj`

## Caveats Exporting from Blender

Tricks for exporting multiple [animations](blender-animation.md) from blender

- In Action editor, press `push down` for each action you want to export respectively

![push down](/image/blender-tricks-push-down.png)

## Caveats Exporting from Maya

Before Exporting From Maya

- Preferences -> Settings
  - `Up Axis` to `Y`
  - Linear: `millimetter`
- `Soften Edge` apply on mesh
- `Bake Simulation`: Bake the rig animation to the skin 
  - Select all related Joints, then the mesh

Exporting Options

- `embed media` to include textures files

After Importing

- Rig Tab
  - Animation Type: `legacy`, `generic`, `humanoid`
- Animation Tab
  - Loop Time 
  - Bake Into Pose 


