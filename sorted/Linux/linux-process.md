# Linux - Process

## What Is This

- process is an instance of program
- process context: text, data, virtual address space, heap, shared memory, user stack

## Process State

- Running
- Waiting
- uninterruptible Sleep
- Stopped
- Zombie
- Dead
- Paging

## Kernel Space

- where the code and data of the [kernel]() is stored and execute under
- What processes run in kernel space?
  - operating system kernel
  - device drivers

## User Space

- where normal user processed run
- the key difference between kernel space
  - access level
    - kernel space has full access to the underlying hardware
    - user space has limited access to the underlying hardware

## Asynchronous

[futex](linux-futex.md)

## Daemon

[Daemon](linux-daemon.md)

## Process Priority

- final process priority = [NI Priority]() + current priority
- if a process is started without setting a priority, it will use 0 as default
- 进程的优先级字段，数值越小优先级越高

## Adjust Process Priority

`nice`

- `nice [-n] num command`
- Adjust the priority of a process when it is started
- 以优先级 num 启动，若 num 为空，默认是 10
- 优先级字段编号越小，优先级越高
- 设定范围 0~19

`renice`: adjust already running process priority

