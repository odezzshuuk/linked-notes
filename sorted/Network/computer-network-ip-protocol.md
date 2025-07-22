# IP Protocol

- IP header information:
  - Appears in IP datagrams, used to specify the source IP address and destination IP address for IP communication, guide IP fragmentation and reassembly, and specify some communication behaviors.
- IP datagram routing and forwarding:
  - Occurs on all hosts and routers except the destination machine.
  - Determines whether and how datagrams should be forwarded.

## Characteristics of IP Service

- Provides **stateless, connectionless, unreliable** service.
- Stateless: IP communication parties do not synchronize the state information of data transmission.
- Connectionless: Does not permanently store any information about the other party.
- Unreliable: Does not guarantee accurate arrival at the receiver.
  - For example, if the transmission time is too long or the [IP datagram](ipv4数据报.md) is incorrect.
  - If transmission fails, it will notify the upper layer protocol and will not attempt retransmission.
