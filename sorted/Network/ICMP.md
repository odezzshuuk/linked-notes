# ICMP Internet Control Message Protocol

- Error reporting, for example, when a router cannot find a host path specified in an HTTP request, the router will generate an ICMP message and send it to the requesting [computer-network-end-system](computer-network-end-system.md).
- Usually considered part of IP.
- Contains a type field and a code field.
  - Includes the header and the first 8 bytes of the [IP datagram](ipv4数据报.md) that caused the ICMP message to be generated, so that the sender can determine which datagram caused the error.
