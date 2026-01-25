# Mermaid - ClassDiagram

## Define Class

```mermaid
classDiagram
class ClassName~GenericType~ {
    <<Interface>>
    +Type publicProp
    -Type privateProp
    #Type protectedProp
    Type staticProp$
    +method(param) returnType
    abstractMethod(param) returnType*
    staticMethod(param) returnType$

    List~GenericType~ propname
}
```

- `<<Interface>>` is annotation of class, other annotation is `<<Abstract>>`, `<<Service>>`, `<<Enumeration>>`

## Define Classes RelationShip

Relationship Arrow

- `--|>`: [Inheritance](uml.md#———▷-inheritance)
- `..|>`: [Realization](uml.md#---▷-implementation)
- `-->`:  [Association](uml.md#——󰁔-one-way-association)
- `*--`:  [Composition](uml.md#󰣏———-composition))
- `o--`:  [Aggregation](uml.md#󱀝———-aggregation)
- `--`:  [Association](uml.md#———-association)
- `..>`:  Dependency
- `..`:   Link (Dashed)

Label Relationship

- `[classA][arrow][classB]:labeltext`

```mermaid
classDiagram
classA <|-- classB : implements
classC *-- classD : composition
classE o-- classF : aggregation
```
