# XSI IPC

- InterProcess Communication, abbreviated as IPC
- Child processes can inherit IPC resources from parent processes through fork()
- XSI IPC resource types: [[Message Queue]], [[linux-systemv-semaphore]], [Shared Memory](linux-shared-memory-segment.md)

## Similar Features

- Identifier
  - Functions similar to file descriptors
  - Identifiers for the same type of IPC resources will not be duplicated
  - Access methods: [[msgget() function]], [[semget() function]], [[shmget() function]]
- Key
  - Data type key_t
  - Facilitates reference by multiple processes
  - Can be a specified positive integer constant
  - Functions similar to a filename
  - [[ftok() function]] returns the key needed to generate an identifier for IPC resources
- Permission structure, [[ipc_perm structure]]

## Three get functions

- Similar parameters key and flag
- When key is IPC_PRIVATE parameter, or is unrelated to current IPC structure of a certain type, the IPC_CREAT flag bit needs to be set in flag