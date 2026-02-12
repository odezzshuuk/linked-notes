# Blender - Parenting

## Parenting Options

- Object
- Object(Keep Transform): when object already has parent and being transformed, transform will be kept when parent to new parent
- Object(Without Inverse): child transform will immediately relative to the parent origin

## When Parenting, Which Object Should be selected as DIRECT child

Conclusions

- direct child, constraints, ...

For Object Tree, like that

```
├── Object A
└── Object B
    └── Object C
```

- When Set Object A as Parent of Object B
  - Only select Object A and B
  - Object C should **Not** be selected

All Object Set As Child, will be flattened

- Parent is Parent, the object selected as parent will not be the grandparent of the child object
- If Object C is selected as child, Object A won't be the grandparent of Object C
- Object Tree will be like that

```
└── Object A
    ├── Object B
    └── Object C
```
