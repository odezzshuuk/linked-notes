# Maya - Auto Retopology

## Requirement for Auto retopology

- Ensure a base mesh and settings that are as clean as possible
- Retopologize works best on [high-poly](topology-glossary.md#high-poly), organic objects with roughly even face distribution

## Prepare The Mesh For Retopologize

if the mesh have dense input mesh

- `Mesh -> Retopologize`: enable *Preprocess Mesh* will speed up and increase the success of retopologize

if input mesh is not very dense or *Preprocess Mesh* is not viable

1. seprate the mesh into disconnected component(via `Mesh -> Separate`)
2. Soften as many edges as possible(`Mesh Display -> Soften Edge`). Limit [hard edges](topology-glossary.md#hard-edge) only to area where distinct features need to be maintained

> view hard edges by `Display -> Polygons -> Hard Edges(Color)`

3. Run `Mesh > Cleanup` with following options

- Faces with more than 4 sides
- Concave faces
- faces with holes
- Non-planar faces
- Lamina geometry
- Non-manifold geometry
- Edges with zero length
- Faces with zero geometry area
- Invalid Components

4. Split any faces with non-consecutive duplicate vertices into 2 faces.
5. Run Mesh > Merge: on all the vertices with a very small threshold to merge all very short edges.
6. Run Mesh > Remesh: on the mesh to evenly spread components out.
7. Delete history on the mesh (especially if your scene file includes a Retopo node prior to Maya 2020).
8. Set Retopologize settings appropriately based on whether your model is a hard surface or organic mesh. In particular,

- For [organic surfaces](topology-glossary.md#organic-surface): The default settings are ideally tuned for organic surfaces.
- For [hard surfaces](topology-glossary.md#hard-surface): Set high Topology Regularity and Face Uniformity values (i.e. 1) with a low Anisotropy value (i.e. 0).

9. Run Retopologize.

## Run Retopologize 

1. Select Mesh > Retopologize 󰖯 

- if you have a dense mesh to **speed up** Retopologize and increase the success of the operation, enable Preprocess Mesh 
- if you want to preserve the **original** mesh as a **backup**. The Retopologize operation will be performed on its duplicate, enable Keep **Original** 
- if you want to maintain hard edges and denote them as feature edges, enable Preserve **Hard Edges** 
- For organic surfaces: The default settings are ideally tuned for organic surfaces.
- For hard surfaces: Set high Topology Regularity and Face Uniformity values (i.e. 1) with a low Anisotropy value (i.e. 0).

> This will convert all the faces of the mesh into 4-sided faces (quads).
> Note: This operation may take a long time if you're working with a very dense mesh that hasn't been preprocessed. You can view Retopologize's progress in the Output window. To cancel the operation, hold the Esc key before Retopologize finishes.

2. (Optional) You can modify the settings in the polyRetopo node to adjust the result mesh. However, each change you make to an attribute will cause the algorithm to run again, unless you turn the node's Pause button on first. We highly recommend turning this on, making multiple changes, then turning it off to see all those changes reflected at once.
3. (Recommended) Once the topology looks good, we highly recommend immediately **deleting the object's history** (`Edit > Delete by Type > History`).

> Note: Ignoring this step will likely result in polyRetopo executing again upon further mesh operations or when opening the file again, which can take a long time for dense meshes.

4. (Optional) To **transfer UVs** from the original mesh **to the retopologized one**, select the original mesh and then the retopologized one and go to `Mesh > Transfer Attributes`.


