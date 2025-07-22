# Transport Layer

## About Transport Layer

- Function:
  - Extends the delivery service between two [computer-network-end-system](computer-network-end-system.md) in the network layer to a delivery service between two different application layer **processes** in two different end systems.
- Between [Network_Application_Layer](network-application-layer.md) and [network layer](computer-network-network-layer.md).
- Mainly has 2 protocols: [TCP](computer-network-tcp.md), [UDP](udp.md).
- Translates messages received from application layer processes to groups in the transport layer; the group is called a transport layer segment.
- Provides logical communication between **processes** in different hosts.
- [Multiplexing] and [Demultiplexing].

![Multiplexing_diagram.svg](/image/Multiplexing_diagram.svg.png)

- Structure of a transport layer segment:
  - Source port number and destination port number.
  - Other header fields.
  - Application data (message).

## Glossary of Transport Layer

[TCP](computer-network-tcp.md)

[UDP](udp.md)

