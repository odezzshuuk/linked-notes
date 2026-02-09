# Blender - Animation

* [Actions](#actions)
* [Action Slot](#action-slot)
* [Keyframes](#keyframes)
* [Armature](#armature)
* [Bones](#bones)
* [Vertex Group](#vertex-group)
* [Rigging](#rigging)
* [Workflow](#workflow)
* [Object Constraints](#object-constraints)
* [Bone Constraints](#bone-constraints)
* [Animation Related Editors](#animation-related-editors)
* [Animation Editors](#related-editors)

## Actions

- Animation data container
- An action can has multiple [action slots](#action-slot)
- A [data-blocks](blender-concepts#data-block)

## Action Slot

- Where the animation data actually stored
- A group of evoluted properties
- For example, An action has two action slots: One for transformation, one for material

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

## Vertex Group

- muscle of the body

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

optional in this steps:

- In armature properties: Viewport -> check `infront` for better visibility

3. [Parenting](blender-operation#parenting) [**Armature(bones)**](#armature) to **Meshes(body)** with automatic weights

> Set Armature as Object Parent

- this step will generate [vertex groups](blender-concepts#vertex-groups) based on bones

4. Weight Paint

[Weight Paint](blender-weight-paint)

options in this steps:

- `auto normalize`

5. (Optional)Adding [IK Constraint](blender-operation.md#set-ik-constraint) to bones

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

## Animation Editors

Dope Sheet: 

- Overview of all animation in scene

Action Editor

- Focus on single action

## F-Curve

- Blender animation almost any property
- The evolution of a property's value over time is represented by F-Curve(Function Curve)

