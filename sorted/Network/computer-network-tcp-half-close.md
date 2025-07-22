# Half-Close State

- The TCP protocol allows one end to send a FIN segment to the other, indicating that this end has finished sending data, but continues to receive data from the other end.
- Allows data transmission in both directions to be closed independently.
- The [socket](socket.md) network programming interface supports the half-close state through the `shutdown` function.
