# Blender - Parenting

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
- Object C should not be selected

All Object Set As Child, will be flattened

- Parent is Parent, the object selected as parent will not be the grandparent of the child object
- If Object C is selected as child, Object A won't be the grandparent of Object C
- Object Tree will be like that

```
└── Object A
    ├── Object B
    └── Object C
```
