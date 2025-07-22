# Computer Network - Reliable Transmission

## Three-way Handshake

- `TCP SYN` from Client to Server
- `TCP SYN/ACK` From Server to Client
- `TCP ACK` from server to Server

## Four-way Handshake

Start With A send disconnect request

```mermaid
sequenceDiagram
A ->> B: FIN:1
B ->> A: ACK
Note right of B: send receiving confirm packet
B ->> A: FIN:1
A ->> B: ACK
```

## Normal Case

- After sending each [network-group](network-group.md), stop sending and wait for acknowledgment from the other party. Only after receiving the acknowledgment, send the next one.
  - After A sends a packet, it temporarily keeps a copy of the sent packet.
  - Both packets and acknowledgment packets must be numbered.
  - The retransmission time set by the timeout timer should be longer than the average round-trip time of data transmission in the packet.

```mermaid
sequenceDiagram
A ->> B: Send packet M1
Note left of A: RTT
B ->> A: Acknowledge M1
A -) B: Continue sending packet M2
Note left of A: RTT
B ->> A: Acknowledge M2
```

## Abnormal Cases

### 1. No response

```mermaid
sequenceDiagram
participant A
participant B
A -x B: Send erroneous packet M1
B --> A: Discard erroneous M1, do not send any information
Note left of A: Timeout retransmission
A ->> B: Send packet M1
B -->> A: Acknowledge M1
```

### 2. Acknowledgment from B is lost

1. A retransmits.
2. B discards the duplicate M1.
3. Sends acknowledgment to A.

```mermaid
sequenceDiagram
participant A
participant B
A ->> B: Send erroneous packet M1
B --x A: Acknowledgment sent is lost
Note left of A: Timeout retransmission
A ->> B: Send packet M1
B -->> A: Acknowledge M1
A ->> B: Continue sending packet M2
```

### 3. Acknowledgment from B is delayed

1. A retransmits.
2. B discards the duplicate M1.

## Go-Back-N ARQ Protocol (Continuous ARQ Protocol)

- The sender maintains a sending window, and all packets in the window can be sent continuously without waiting for acknowledgment from the other party, improving [channel utilization](信道利用率.md).
- Each time the sender receives an acknowledgment, it slides the sending window forward by one packet position.
- The receiver does not need to send acknowledgments one by one; it only sends an acknowledgment for the last received packet, indicating that the current packet and all preceding packets have been correctly received.

[Timeout Retransmission](超时重传.md)
