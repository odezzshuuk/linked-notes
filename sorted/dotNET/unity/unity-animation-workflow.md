# Unity - Animation Workflow

## Prerequisites

- A 3D model with a rig (skeleton/armature)
- Animation clips (either embedded in the model file or separate `.anim` files)
- Common formats: `.fbx`, `.glb`, `.gltf`

## Step-by-Step Workflow

**1. Import the Model**

- Drag your model file (e.g., `.fbx`) into the `Assets` folder
- Unity automatically creates a prefab-like asset

**2. Configure the Rig**

- Select the imported model in Project window
- In Inspector, go to **Rig** tab
- Set **Animation Type**:
  - `Humanoid` - for human-like characters (enables retargeting)
  - `Generic` - for non-human or custom rigs
  - `Legacy` - old system, avoid for new projects
- Click **Apply**

**3. Configure Animations**

- Go to **Animation** tab in Inspector
- Check animation clips are listed
- For each clip, configure:
  - **Loop Time** - enable for repeating animations (idle, walk)
  - **Root Motion** - enable if animation should move the character
- Click **Apply**

**4. Create an Animator Controller**

- Right-click in Project window → **Create** → **Animator Controller**
- Name it (e.g., `CharacterAnimator`)
- Double-click to open the **Animator** window

**5. Control via Script**

```csharp
using UnityEngine;

public class CharacterAnimationController : MonoBehaviour
{
    private Animator animator;

    void Start()
    {
        animator = GetComponent<Animator>();
    }

    void Update()
    {
        // Bool parameter
        bool isMoving = Input.GetAxis("Horizontal") != 0 || Input.GetAxis("Vertical") != 0;
        animator.SetBool("isWalking", isMoving);

        // Trigger parameter (one-shot)
        if (Input.GetKeyDown(KeyCode.Space))
        {
            animator.SetTrigger("Jump");
        }

        // Float parameter (for blend trees)
        float speed = new Vector2(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical")).magnitude;
        animator.SetFloat("Speed", speed);
    }
}
```

## Common State Machine Setup

```
[Entry] → [Idle] ←→ [Walk] ←→ [Run]
              ↓
          [Jump] → (returns to Idle/Walk based on grounded state)
```

Typical transitions:
- Idle → Walk: `isWalking == true`
- Walk → Idle: `isWalking == false`
- Any State → Jump: `Jump` trigger

## Tips & Tricks

- Use **Blend Trees** for smooth transitions between similar animations (walk/run speeds)
- Enable **Apply Root Motion** on Animator component if animation should drive movement
- Use **Animation Layers** for upper/lower body separation (shooting while running)
- **Avatar Masks** let you apply animations to specific body parts
- Check **Bake Into Pose** for root motion you want to ignore (Y for grounded anims)
- Use `animator.Play("StateName")` to force-play a state immediately
