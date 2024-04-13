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

## 5 Key Parts of Unity Animation System

1. [Animator](#animator)
2. [Controller](#controller)
3. [Animation Clips](#animation-clips)
4. [Avatar](#avatar)
5. [Script(Optional)]()

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

## Avatar

- bones

## Simple Animation Workflow

**Step 1:** Create A [GameObject](unity-gameobject.md)

**Step 2:** Create [Animator](#Animator), there are 2 ways to create an Animator:

- Directly [Create Animation On Object](), which will automatically create an Animator
- Add Animator [Component]() to GameObject. specify controller manually 

**Step 3:** Create Animation Clips, also 2 ways

- use unity: create by recording keyframe
- import from external source

**Step 4:** Edit Animation Controller. also 2 ways

- use unity controller editor, which edit a `.controller` file visually
- create your own [state machine](javascript-design-pattern-state.md) in code

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

Imported model file should be carefully prepared before importing to unity

- define the rig type and create the avatar
- verify the avatar's mapping

## Reuseable Humanoid Animation



