# Computer Network - Router

- Operates at the [network layer](网络层.md).
- The first router on the path from a [computer-network-end-system](computer-network-end-system.md) to any other remote system is called the edge router.
- The router's input ports, output ports, and switching fabric are almost always implemented in hardware.

## Input Port

- Termination of physical layer functions.
- Also interacts with the data link layer at the remote end of the link to perform [data link layer](数据链路层.md) functions.
- Determines the router's output port by querying the [forwarding table](转发表.md).
- Performs functions belonging to the [data plane](数据平面.md).

## Switching Fabric

- Is a network structure within the router.
- Switches from input port to output port, i.e., forwards.
- Switching methods:
  - Switching via memory
  - Switching via bus
  - Switching via interconnection network

## Output Port

- Handles taking packets already stored in the output port's memory and sending them to the output link.
- Transmits these packets on the output link by performing necessary data link layer and physical layer functions.

```mermaid
flowchart LR
A["Queueing<br>(Buffer Management)"] --> B["Data Link Processing<br>(Protocol, Encapsulation)"]
B --> C[Line Termination]
```

## Routing Processor

- Executes the router's [control plane](控制平面.md) functions.
