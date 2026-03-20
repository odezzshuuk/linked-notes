# Rust - Sender and Receiver

## What It Is

`Sender<T>` and `Receiver<T>` are the two ends of a Rust channel.

- `Sender<T>` pushes values into the channel with `send()`.
- `Receiver<T>` pulls values out with `recv()`, `try_recv()`, or `recv_timeout()`.

They are commonly created with `std::sync::mpsc::channel()`.

- `mpsc` means **multiple producer, single consumer**.
- Multiple cloned senders can send to one receiver.
- Values are moved across thread boundaries safely.

## Key Features

- Type-safe message passing: each channel carries one type `T`.
- Ownership transfer: sending usually moves `T` to the receiver side.
- Thread-safe coordination without shared mutable state.
- Natural shutdown signal:
	- When all `Sender` handles are dropped, `recv()` returns an error.

## What's It For

Use sender/receiver when you want [**threads**](rust-thread) to communicate with messages,
instead of sharing memory directly.

Typical cases:

- Worker thread sends results back to the main thread.
- Multiple tasks report progress to one logger thread.
- Producer-consumer pipelines where order matters.

## Channel

- A channel is a thread-safe message pipe between tasks/threads.
- You can think of it as a typed FIFO mailbox:
	- `Sender<T>` puts messages in.
	- `Receiver<T>` takes messages out.
- FIFO means first sent is first received for messages in the same stream.
- The channel closes when all senders are dropped.

How To Create

```rust
use std::sync::mpsc;
let (tx, rx) = mpsc::channel();
```

## How It Works

1. Create a channel: `let (tx, rx) = mpsc::channel();`
2. Move `tx` into producer thread(s).
3. Send values with `tx.send(value)`.
4. Receive values with `rx.recv()` (blocking) or `rx.try_recv()` (non-blocking).
5. End stream by dropping all senders.

Behavior summary:

- `send(v)`:
	- `Ok(())` if receiver still exists.
	- `Err(SendError(v))` if receiver is dropped.
- `recv()`:
	- Blocks until a message arrives or channel closes.
	- `Err(RecvError)` when channel is closed and empty.

## Example

This example models a small product-style event pipeline:

- producer services emit domain events
- one consumer worker handles those events centrally
- `Sender<AppEvent>` and `Receiver<AppEvent>` are explicit in function signatures

`thread::spawn` starts background workers.
`move` transfers channel handles into those workers safely.

```rust
use std::sync::mpsc::{self, Receiver, Sender};
use std::thread;
use std::time::Duration;

#[derive(Debug)]
enum AppEvent {
    OrderCreated { order_id: u64 },
    PaymentConfirmed { order_id: u64 },
    Stop,
}

fn spawn_order_service(tx: Sender<AppEvent>) -> thread::JoinHandle<()> {
    thread::spawn(move || {
        for order_id in 1001..=1003 {
            tx.send(AppEvent::OrderCreated { order_id }).unwrap();
            thread::sleep(Duration::from_millis(20));
        }
    })
}

fn spawn_payment_service(tx: Sender<AppEvent>) -> thread::JoinHandle<()> {
    thread::spawn(move || {
        for order_id in 1001..=1003 {
            tx.send(AppEvent::PaymentConfirmed { order_id }).unwrap();
            thread::sleep(Duration::from_millis(35));
        }
    })
}

fn run_audit_worker(rx: Receiver<AppEvent>) {
    while let Ok(event) = rx.recv() {
        match event {
            AppEvent::OrderCreated { order_id } => {
                println!("audit: order created: {order_id}");
            }
            AppEvent::PaymentConfirmed { order_id } => {
                println!("audit: payment confirmed: {order_id}");
            }
            AppEvent::Stop => {
                println!("audit: graceful shutdown");
                break;
            }
        }
    }
}

fn main() {
    let (event_tx, event_rx): (Sender<AppEvent>, Receiver<AppEvent>) = mpsc::channel();

    let order_handle = spawn_order_service(event_tx.clone());
    let payment_handle = spawn_payment_service(event_tx.clone());
    let audit_handle = thread::spawn(move || run_audit_worker(event_rx));

    order_handle.join().unwrap();
    payment_handle.join().unwrap();

    event_tx.send(AppEvent::Stop).unwrap();
    drop(event_tx);

    audit_handle.join().unwrap();
}
```

## Tips and Tricks

- Clone sender for multi-producer usage: `let tx2 = tx.clone();`
- Prefer `for msg in rx` for simple consumer loops.
- Use `try_recv()` for polling loops where blocking is unacceptable.
- Use `recv_timeout()` to combine waiting with time-based fallback logic.
- If messages are large, send lightweight identifiers or `Arc<T>` handles.

## Related Notes

- [Rust - std::sync::mpsc](rust-std-sync-mpsc.md)
- [Rust - std](rust-std.md)
