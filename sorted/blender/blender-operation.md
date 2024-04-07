# Blender - Operation

## General

- switch between object mode and edit mode: `tab`
- toggle top-right axis thing: `show gizmo`
- switch editor type: top-left corner dropdown menu

| Key | Description                                                   |
| :-: | ------------------------------------------------------------- |
|  n  | toggle context(usually about transformation, rotation, scale) |

## Viewport

|              Key               | Description   |
| :----------------------------: | ------------- |
|     `mouse wheel pressing`     | rotate view   |
| `mouse wheel pressing + shift` | pan veiw move |
|     `mouse wheel rolling`      | zoom in/out   |

## Object Mode

|        Key         | Description                   |
| :----------------: | ----------------------------- |
|         g          | grab                          |
|         gx         | grab and move on x axis       |
|         r          | rotate                        |
|         rx         | rotate on x axis              |
|         s          | scale                         |
|         sx         | scale on x axis               |
|        `/`         | local view or focus on select |
|         n          | 3D view properties            |
| shift + left click | select multiple objects       |
|      alt + p       | clear parent                  |
|      ctrl + j      | join objects                  |

## Edit Mode

|       Key        | Description                            |
| :--------------: | -------------------------------------- |
|        g         | grab                                   |
|     alt + s      | flat translate select                  |
|      ctrl-l      | select linked part                     |
|        e         | extrude                                |
|        p         | separate vertices to new object        |
|        p         | separate                               |
|     crtl - +     | select next vertices on the chain      |
|        h         | hide                                   |
|     alt - h      | unhide                                 |
| alt + left click | select edge loop                       |
|    shift + s     | snap cursor or selected or interaction |

## Moving

|     Key     | Description          |
| :---------: | -------------------- |
| shift + tab | toggle snapping mode |

## Set Parent

1. select multiple objects
2. key `ctrl-p`
3. select `object` in popup menu

- the last selected object will be the parent of the others
- In step 3, when change the parent, the scale of the child object will be changed
- select `object(keep transform)` to keep the child object's transform

## Set IK Constraint

1. create a bone, clear its parent, used as the bone handler
2. select handlers and target bone
3. In pose mode: `shift-i` to set IK constraint

## Glossary

- subvision

## extrude

## vertical split
