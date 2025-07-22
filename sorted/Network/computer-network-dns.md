# DNS

## What Is DNS

- DNS: Domain Name System
- Is a Service that translates [domain name](computer-network-domain-name.md) to [IP address](computer-network-ip-address.md).
- Like a phonebook.
- Provides services:
  - Host aliasing
  - Mail server aliasing
  - Load distribution

## Why DNS

1. [Routers](computer-network-router.md) deal with fixed-length [IP addresses](computer-network-ip-address.md).
2. Users are better at remembering [domain names](computer-network-domain-name.md).

## What Happens When Typing A Domain Name In Browser



## DNS Query and Response Message

<table align="center">
	<tr align ="center">
		<td>16-bit Identification</td>
		<td>16-bit Flags</td>
	</tr>
	<tr align ="center">
		<td>16-bit Number of Questions</td>
		<td>16-bit Number of Answer Resource Records</td>
	</tr>
	<tr align ="center">
		<td>16-bit Number of Authority Resource Records</td>
		<td>16-bit Number of Additional Resource Records</td>
	</tr>
	<tr align ="center">
		<td colspan="2">Query Questions, variable length</td>
	</tr>
	<tr align ="center">
		<td colspan="2">Answers (variable number of resource records, variable length)</td>
	</tr>
	<tr align ="center">
		<td colspan="2">Authority (variable number of resource records, variable length)</td>
	</tr>
	<tr align ="center">
		<td colspan="2">Additional Information (variable number of resource records, variable length)</td>
	</tr>
</table>

- 16 bits

| QR    | opcode | AA    | TC   | RD   | RA   | zero  | rcode |
| ----- | ------ | ----- | ---- | ---- | ---- | ----- | ----- |
| 1 bit | 4 bits | 1 bit | 1bit | 1bit | 1bit | 3bits | 4bits |
