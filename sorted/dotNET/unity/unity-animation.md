# Unity - Animation

* [Features](#features)
* [5 Key Parts of Unity Animation System](#5-key-parts-of-unity-animation-system)
* [Animator](#animator)
* [Controller](#controller)
* [Animation Clips](#animation-clips)
* [Avatar](#avatar)
* [Simple Animation Workflow](#simple-animation-workflow)
* [Importing Model File](#importing-model-file)
* [Reuseable Humanoid Animation](#reuseable-humanoid-animation)

## Features

Provide numerous features for handling **humanoid characters**

- Which giving the ability to retarget animation to character model
- This Feature Provides by [Avatar](#avatar) System

## 6 Key Parts of Unity Animation System

1. [Rig](#rig)
2. [Avatar](#avatar)
3. [Animator](#animator)
4. [Controller](unity-animation-controller.md)
5. [Animation Clips](#animation-clips)
6. [Script(Optional)]()

Relationship between these 5 parts

- Animator: Main [component](unity-component.md) of the system, which contains the Controller, Avatar
- Controller
  - A State machine
  - Contains many animation clips
  - Controls the flow of animation clips
- **When Controller And Animation Clips are created, they are independent of the GameObject**, which means:
  - You can use the same Controller and Animation Clips on different GameObjects
  - For example, A Cube animation clips can be used on a Sphere 


## Animator

- A Unity Class to control the animation system

## Animation Controller

[Animation Controller](unity-animation-controller.md)

## Animation Clips

- Essentially series properties of GameObject transformed on timeline

2 ways to create animation clips:

- Import from external source
- Create in scratch

## Rig Tab

What's Avatar

- **Data Structure** that map bone to 3D model's transform hierarchy
- Suppose it is corresponding to the [vertex groups](blender-glossary#vertex-groups) in Blender

Skin Weights

- Define how much influence each bone has on the vertices in the mesh
- Default limit to 4 bones
- The other bones influence will be ignored

Export Mesh And Animation Separately

- Because several animation usually perform on the same model and bone structure

## Simple Animation Workflow

**Step 1:** Create A [GameObject](unity-gameobject.md)

**Step 2:** Create [Animator](#Animator), there are 2 ways to create an Animator:

- Directly [Create Animation On Object](), which will automatically attach an animator to the GameObject
- Add Animator [Component]() to GameObject. specify controller manually 

**Step 3:** Create Animation Clips, also 2 ways

- use unity: create by recording keyframe
- import from external source

**Step 4:** Edit Animation Controller. also 2 ways

- Using unity controller editor, which edit a `.controller` file visually
- Create your own [state machine](javascript-design-pattern-state.md) in code

**Step 5:** Create script to interact with the controller, simple example:

```c
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cube : MonoBehaviour
{
    // Start is called before the first frame update
    private Animator cubeAnimator;

    void Start()
    {
        cubeAnimator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.W))
        {
            cubeAnimator.SetBool("isWalking", true);
            cubeAnimator.SetBool("isIdle", false);
        }
        else if (Input.GetKeyDown(KeyCode.S))
        {
            cubeAnimator.SetBool("isWalking", false);
            cubeAnimator.SetBool("isIdle", true);
        }
    }
}
```

## Importing Model File

[importing model](unity-importing-model.md)

Imported model file should be carefully prepared before importing to unity

- define the rig type and create the avatar
- verify the avatar's mapping

## Reuseable Humanoid Animation

