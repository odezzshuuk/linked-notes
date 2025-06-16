# Timeout Retransmission

- Retransmission Timeout ($RTO$)
- Round-Trip Time ($RTT$) of [network-message](network-message.md) segment: Acknowledgement receipt time - Packet sending time
- Setting the timeout timer:
  - Too short: Causes unnecessary retransmissions
  - Too long: Reduces communication efficiency
  - Must consider which networks are traversed and how much delay they will introduce

## TCP's RTO Selection

- RFC 2988 (Computing TCP's Retransmission Timer): A timer mechanism for TCP
- TCP uses an adaptive algorithm:
  - Weighted average RTT ($RTT_s$):
  - Each time a new RTT is measured, $RTT_s$ is recalculated

$$
\begin{aligned}
& RTT_s = (1 - \alpha) \times (RTT_{s0}) + \alpha \times(RTT) \\
& RTT_s —— Updated $RTT_s$ \\
& RTT_{s0} —— Original $RTT_s$ \\
& RTT —— New RTT sample \\
& \alpha —— Smoothing factor (tentative), 0 < \alpha < 1
\end{aligned}
$$

