# IPv4 Datagram

> In the following table, each row is a length, that is, 32 bits is a length

<table align="center">
	<tr align ="center">
		<td>4-bit<br>Version</td>
		<td>4-bit<br>Header Length</td>
		<td colspan ="2">8-bit Type Of Service
			<br>(TOS)
		</td>
		<td colspan = "4">16-bit Total Length (bytes)</td>
	</tr>
	<tr align="center">
		<td colspan = "4">16-bit Identification</td>
		<td>3-bit<br>Flags</td>
		<td colspan ="3">13-bit Fragment Offset</td>
	</tr>
	<tr align="center">
		<td colspan = "2">8-bit Time To Live<br>(TTL)</td>
		<td colspan = "2">8-bit Protocol</td>
		<td colspan ="4">16-bit Header Checksum</td>
	</tr>
	<tr align="center">
		<td colspan = "8">32-bit Source IP Address</td>
	</tr>
	<tr align="center">
		<td colspan = "8">32-bit Destination IP Address</td>
	</tr>
	<tr align="center">
		<td colspan = "8">Options, max 40 bytes</td>
	</tr>
	<tr align="center">
		<td colspan = "8">Data</td>
	</tr>
</table>

- 4-bit version number: Specifies the version of the IP protocol. For IPv4, its value is 4. Other extended versions of the IPv4 protocol (such as SIP and PIP protocols) have different version numbers (and their header structures are also different from Figure 2-1).
- 4-bit header length: Identifies how many 32-bit words (4 bytes) are in the IP header, generally the starting position of the [computer-network-transport-layer-datagram](computer-network-transport-layer-datagram.md). Since 4 bits can represent a maximum of 15, the maximum length of the IP header is 60 bytes.
- 8-bit Type Of Service (TOS):
  - Includes a 3-bit precedence field (now ignored).
  - 4-bit TOS field:
    - Minimum delay
    - Maximum throughput
    - Highest reliability
    - Minimum cost
	- Applications set according to actual needs.
  - 1-bit reserved field (must be 0).
- 16-bit total length: Refers to the total length of the IP datagram.
  - The unit of length is bytes.
  - The maximum length is 65535 ($2^{16}-1$) bytes.
  - Datagrams exceeding the MTU limit will be fragmented for transmission.
- 16-bit identification:
  - Uniquely identifies each datagram sent by the host.
  - Randomly generated.
  - Increments by 1 for each sent value.
  - All fragments of the same data have the same identification value.
- 3-bit flags
- 13-bit fragment offset
- 8-bit Time To Live
- 8-bit protocol
- 16-bit header checksum
- 32-bit source IP address and destination IP address
- Optional field 40 bytes:
  - Record route
  - Timestamp
  - Loose source routing
  - Strict source routing
