# Blender - Life Saver

## Loop Cut

`ctrl + r`

- manually add vertices to a mesh

## Panel Show Up At Bottom-left When An Operation is Done

- This panel is used for showing the result of the operation
- And provide some options to adjust the operation
- This panel can be shown until the next operation is performed
- To show it again, press `F9`
- After next operation performed, it can't be taken back

## Transform Animation Workflow

> Animation transformation is based on bone's name

1. batch rename bones: `Batch Rename` 

- choose bones(armature), switch to edit mode or pose mode, select all
- change rename type to bones

2. `Object -> Apply -> Rotation/Scale/Location To Deltas`

- With `To Deltas`, other transform influenced will be included

3. `cmd + l` then select link animation data
4. (maximo only) Scale "hips x, y, z Location" to 0.01 on Y-axis, based on (0, 0) pivot 
5. Push down action in `Action Editor/NLA Editor`

## Delete Coincident Faces/Edges/Vertices

- Press `A` to select all
- Then `Merge By Distance`

## Delete Vertex Split Two Edges 


