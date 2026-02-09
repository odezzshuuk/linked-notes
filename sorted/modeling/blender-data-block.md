# Blender - Data Block

## What It Is

- The named items that serve as the base unit of data in a blend **file**

## How Blender Organizes Data

Blender organizes data essentially by link data

- **When two objects linking to the same data-block, changing on one will appear in the other**
- To manually remove a data-block on an object, usually refers to unlink operation

Linked Data-block has some characteristics:

- Support being linked into other blend-files
- Every data-block has its usage counted, when there is more than one, you can see the number of current users of a data-block
- When a data-block has zero users, Blender will remove it when the file is saved or purge operation
- Data-blocks can be marked as protected(fake user)

## Data Type

> Pack Data: Support packed into the blend-file

| Type             | Link | Pack | Description                                                                                                                              |
| :--------------- | :--: | :--: | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Action           |  ✓   |  —   | Stores animation F-Curves. Used as data-block animation data, and the Nonlinear Animation editor.                                        |
| Armature         |  ✓   |  —   | Skeleton used to deform meshes. Used as data of armature objects, and by the Armature Modifier.                                          |
| Brush            |  ✓   |  —   | Used as brush assets in sculpt and paint modes.                                                                                          |
| Camera           |  ✓   |  —   | Used as data by camera objects.                                                                                                          |
| Cache File       |  ✓   |  —   | Used by Mesh Cache modifiers.                                                                                                            |
| Curve            |  ✓   |  —   | Used as data by curve, font & surface objects.                                                                                           |
| Font             |  ✓   |  ✓   | References font files. Used by curve object-data of text objects.                                                                        |
| Grease Pencil    |  ✓   |  —   | 2D/3D sketch data used by Grease Pencil objects. Used as overlay helper info, by the 3D Viewport, Image, Sequencer & Movie Clip editors. |
| Collection       |  ✓   |  —   | Group and organize objects in scenes. Used to instance objects, and in library linking.                                                  |
| Image            |  ✓   |  ✓   | Image files. Used by shader nodes and textures.                                                                                          |
| Keys(Shape Keys) |  ✗   |  —   | Geometry shape storage, which can be animated. Used by mesh, curve, and lattice objects.                                                 |
| Light            |  ✓   |  —   | Used as object data by light objects.                                                                                                    |
| Library          |  ✗   |  ✓   | References to an external blend-file. Access from the Outliner’s Blender File view.                                                      |
| Line Style       |  ✓   |  —   | Used by the Freestyle renderer.                                                                                                          |
| Lattice          |  ✓   |  —   | Grid based lattice deformation. Used as data of lattice objects, and by the Lattice Modifier.                                            |
| Mask             |  ✓   |  —   | 2D animated mask curves. Used by compositing nodes & sequencer strip.                                                                    |
| Material         |  ✓   |  —   | Set shading and texturing render properties. Used by objects, meshes & curves.                                                           |
| Metaball         |  ✓   |  —   | An isosurface in 3D space. Used as data of metaball objects.                                                                             |
| Mesh             |  ✓   |  —   | Geometry made of vertices/edges/faces. Used as data of mesh objects.                                                                     |
| Movie Clip       |  ✓   |  ✗   | Reference to an image sequence or video file. Used in the Movie Clip editor.                                                             |
| Node Tree        |  ✓   |  —   | Groups of re-usable nodes. Used in the node editors.                                                                                     |
| Object           |  ✓   |  —   | An entity in the scene with location, scale, rotation. Used by scenes & collections.                                                     |
| Paint Curve      |  ✓   |  —   | Stores a paint or sculpt stroke. Access from the paint tools.                                                                            |
| Palette          |  ✓   |  —   | Store color presets. Access from the paint tools.                                                                                        |
| Particle         |  ✓   |  —   | Particle settings. Used by particle systems.                                                                                             |
| Light Probe      |  ✓   |  —   | Help achieve complex real-time lighting in EEVEE.                                                                                        |
| Scene            |  ✓   |  —   | Primary store of all data displayed and animated. Used as top-level storage for objects & animation.                                     |
| Sounds           |  ✓   |  ✓   | Reference to sound files. Used as data of speaker objects.                                                                               |
| Speaker          |  ✓   |  —   | Sound sources for a 3D scene. Used as data of speaker object.                                                                            |
| Text             |  ✓   |  ✗   | Text data. Used by Python scripts and OSL shaders.                                                                                       |
| Texture          |  ✓   |  —   | 2D/3D textures. Used by brushes and modifiers.                                                                                           |
| Window Manager   |  ✗   |  —   | The overarching manager for all of Blender’s user interface. Includes Workspaces, notification system, operators, and keymaps.           |
| World            |  ✓   |  —   | Define global render environment settings.                                                                                               |
| Workspace        |  ✗   |  —   | UI layout. Used by each window, which has its own workspace.                                                                             |

