# Computer Network - Frame

- Different transmission media have different frame types.
  - [Ethernet](以太网.md) frame
  - [Token Ring](令牌环.md) frame

## Ethernet Frame

<table>
    <tr align="center">
        <td>Destination Physical Address</td>
        <td>Source Physical Address</td>
        <td>Type</td>
        <td>Data</td>
        <td>CRC</td>
    </tr>
    <tr align="center">
        <td>6 bytes</td>
        <td>6 bytes</td>
        <td>2 bytes</td>
        <td>46~1500 bytes</td>
        <td>4 bytes</td>
    </tr>
</table>
- Maximum Transmission Unit (MTU) refers to how much upper-layer data a protocol can carry. In the table above, the MTU is 1500 bytes.
- ARP request/response messages belong to the frame data.
