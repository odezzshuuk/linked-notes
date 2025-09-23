# Thread Class

## Starting a Thread

- start()

## Waiting for a Thread to Finish

- join()
- join(long millis) throws InterruptedException
  - Wait for at most millis milliseconds
  - If millis is 0, it means wait indefinitely

## Daemon Threads

- When all running threads are daemon threads, the Java Virtual Machine will exit.
- setDaemon(boolean daemon) sets the thread as a daemon thread
  - Must be called before start()
- isDaemon(): Checks if the thread is a [daemon thread]()

## Priority

- For threads on the same core, the higher the priority, the more time slices the thread gets

## Thread Interruption

## Methods

- Thread.sleep(): Blocks the current thread for the specified number of milliseconds
- interrupt(): Interrupts the thread
- static yield(): Hints to the scheduler that the current thread is willing to yield its current use of the processor; the scheduler may ignore this hint

***

- currentThread(): The current thread object
- isAlive(): Whether the thread is active
- isInterrupted()
- getPriority(): Gets the thread's priority

