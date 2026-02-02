# Blender - Animation

* [Keyframes](#keyframes)
* [Bones](#bones)
* [Rigging](#rigging)
* [Normal Character Animation Workflow](#normal-character-animation-workflow)
* [Object Constraints](#object-constraints)
* [Bone Constraints](#bone-constraints)

## Actions

- Animation data container

## Action Slot

## Keyframes

- for interpolated animation
- overview keyframes via `dope sheet`
- when current frame is a keyframe, top-left corner object's name will be yellow
- timeline editor provides a simple way to manage keyframes

keyframe type color:

- Normal Keyframe: white(unselected), yellow(selected)
- ...

Interpolation

- Interpolation is controlled by curves edit via `graph editor`

Extrapolatoin

- Defines the behavior of a curve **before the first** and **after the last** keyframes


## Armature

When talk about armature, it means:

- A collection of bones
- Used to rig

## Bones

- base element of armature

## Rigging

What's For

- Adding control to object
- Effectively define a user interface for animator to use

## Workflow

1. Creating body, mostly a group of meshes(cube, cylinder, sphere, etc.)

Included Operations:

- `subdivision surface`
- ...

2. Creating [armature](#armature), mostly a group of bones

options in this steps:

- `infront`

3. [Parenting]() [**Armature(bones)**](#armature) to **Meshes(body)** with automatic weights

- this step will generate vertex groups based on bones

4. Adjusting weight paint

options in this steps:

- `auto normalize`

5. Adding [IK Constraint](blender-operation.md#set-ik-constraint) to bones

options in this steps

- `chain length`
- `inverse kinematics`, like lock rotation, etc.

## Object Constraints

- Constraint Object's location, rotation, scale, transform, transform path, etc.
- Constraint include: copy, limit, track, etc.

## Bone Constraints

## Animation Related Editors

- Timeline Editor
- Dope Sheet: Edit multiple [actions](#actions), those actions may coincide in time line
  - Action Editor: switch between actions
- Graph Editor: Edit Curves
- NLA Editor: non-linear animation editor, transition between actions
- Drivers

## Related Editors

Dope Sheet: 

- Overview of all animation in scene

Action Editor

- Focus on single action

