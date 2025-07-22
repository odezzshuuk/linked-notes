# Computer Network - TCP segment structure

- [TCP segment structure](#tcp-segment-structure)
- [Sequence Number](#sequence-number)
- [Acknowledgement Number](#acknowledgement-number)
- [Data Offset](#data-offset)
- [Reserved](#reserved)
- [Flags](#flags)
- [Window Size](#window-size)
- [Checksum](#checksum)
- [Urgent Pointer](#urgent-pointer)
- [Options](#options)

## Take A Look

```sh
0x0000:  4500 0034 0014 0000 2e06 c005 4e8e d16e  E..4........N..n
0x0010:  ac1e 0090 6c86 01bb 8e0a b73e 1095 9779  ....l......>...y
0x0020:  8010 001c d202 0000 0101 080a 3803 7b55  ............8.{U
00030:  4801 8100
```

## TCP segment structure

```sh
| 0                            15                             31|
-----------------------------------------------------------------
|          source port          |       destination port        |
-----------------------------------------------------------------
|                        sequence number                        |
-----------------------------------------------------------------
|                     acknowledgment number                     |
-----------------------------------------------------------------
|  HL   | rsvd  |C|E|U|A|P|R|S|F|        window size            |
-----------------------------------------------------------------
|         TCP checksum          |       urgent pointer          |
-----------------------------------------------------------------
|                    options (if data offset > 5)               |
-----------------------------------------------------------------
```

- [options here](#options)

## Sequence Number

- 32-bit sequence number
- If [SYN flag](#flags) is set,

## Acknowledgement Number

- 32-bit acknowledgment number (ack = )

## Data Offset

- 4-bit data offset
- Specifies the size of the TCP header

## Reserved

## Flags

8 Flags

- CWR:
- ECE:
- URG: [Urgent pointer](#urgent-pointer) field is significant
- ACK: Acknowledgment field
  - All packets after the initial SYN packet sent by the client **should have** this flag set
- PSH:
- RST: Reset the connection
- SYN: Synchronize sequence numbers
  - Connection Initialization
  - Synchronization
- FIN: Last packet from sender


## Window Size

> 16 bits

- Specifies the number of window size units
- That the sender of this segment is currently willing to receive

## Checksum

> 16 bits

- Used for error-checking

## Urgent Pointer

> 16 bits

- Used to send urgent data byte

## Options

<table>
    <tr>
        <td>kind (1 byte)</td>
        <td>length (1 byte)</td>
        <td>info (remaining bytes)</td>
   </tr>
</table>

- Kind can be 0~8

