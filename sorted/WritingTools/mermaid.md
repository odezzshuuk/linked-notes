# Mermaid

* [Flowchart](#flowchart)
* [stateDiagram](#statediagram)
* [sequence](#sequence)
* [classdiagram](#classdiagram)

## Flowchart

```mermaid
flowchart TB
A --o B --x C & D
E & F --> G & H
I <--> J
```

flowchart TB represents flow direction other available options:

- flowchart TD
- flowchart TB
- flowchart LR

> T:Top, B and D: Bottom, L and R: Left and Right

Node Shape

```mermaid
flowchart LR
id1[rectangle]
id1 --> id2(round edge)
id2 ==>id3([stadium-shaped])
id3 -.-id4((circle))
id5>asymmetric shape]
id6{rhombus}
id7{{hexagon node}}
id8[/parallelogram/]
id9[/trapezoid\]
id10[(cylindrical)]
```

Link Style

```mermaid
flowchart LR
    A-->B  
    A---B
    A---|text|B
    A-.->B
```

## stateDiagram

## sequence

```sequence
left -> right : left ot right
Note right of right:right context
Note left of left:left content
```

## classdiagram

[classDiagram](mermaid-classdiagram.md)

