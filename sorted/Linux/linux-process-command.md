# Linux - Process Command

## Query Process

[ps](linux-ps.md)

## Stop Process

[kill](linux-kill.md)

## Jobs 

[jobs](linux-jobs.md)

> `crtl + z`: suspend process

## pstree

options

- `-A`: use ACSCII character to connect each program tree
- `-p`: show PID
- `-u`: show PID's owner

> bash can be a parent program

- `pstree` can show parent-child relationship

## top

monitor system information

- continously monitor system information

output of `top` command looks like

```
top - 11:46:11 up 2 days, 17:22,  3 users,  load average: 0.09, 0.22, 0.32
Tasks: 336 total,   4 running, 331 sleeping,   0 stopped,   1 zombie
%Cpu(s): 11.1 us,  9.7 sy,  0.0 ni, 76.5 id,  0.0 wa,  2.3 hi,  0.3 si,  0.0 st
MiB Mem :   1750.8 total,    103.7 free,   1623.5 used,    181.3 buff/cache
MiB Swap:   2048.0 total,   1143.2 free,    904.8 used.    127.3 avail Mem

top - 11:49:15 up 2 days, 17:25,  3 users,  load average: 1.12, 0.65, 0.46
Tasks: 332 total,   2 running, 330 sleeping,   0 stopped,   0 zombie
%Cpu(s):  9.1 us,  8.2 sy,  0.0 ni, 80.1 id,  0.0 wa,  2.4 hi,  0.2 si,  0.0 st
MiB Mem :   1750.8 total,    103.2 free,   1624.1 used,    181.3 buff/cache
MiB Swap:   2048.0 total,   1143.2 free,    904.8 used.    126.7 avail Mem

    PID     USER  PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+              COMMAND
3879207 usernam+  20   0  295832  67380   2524 S   1.2   3.8  29:34.68         tmux: server
   1058   tomcat  20   0 2770428  34288   3756 S   0.2   1.9   4:57.73                 java
   2543 usernam+  20   0    6304   3008   2092 S   0.2   0.2   1:33.39          dbus-broker
   2617 usernam+  20   0 3414524  60628  15100 S   0.2   3.4  11:21.36          gnome-shell
   2712 usernam+   9 -11  545664   6332   5060 S   0.2   0.4   2:40.71          wireplumber
   2932 usernam+  20   0  535188   9380   7356 S   0.2   0.5   6:54.81             vmtoolsd
1879914 usernam+  20   0 1141544 150776  16640 S   0.2   8.4   2:52.60                 node
```

first 5 lines informations is summary of system information

- line 1: refresh time, uptime, login user count, system load: average load in last 1 minute; average load in last 5 minutes; average load in last 15 minutes
- line 2: total process count, running process count, sleeping process count, stopped process count, zombie process count
- line 3: user space CPU usage percentage, priority process CPU usage percentage, idle CPU percentage, I/O wait percentage, hard interrupt CPU usage percentage, soft interrupt CPU usage percentage
- line 4: physical memory total, used memory, free memory, cache memory
- line 5: virtual memory usage, first 3 items same as line 4, last item is swap memory total

meaning of each field following the system information

| fields  | description                                                                       |
| ------- | --------------------------------------------------------------------------------- |
| PID     | Process ID                                                                        |
| USER    | user                                                                              |
| PR      | process priority                                                                  |
| NI      | nice value, negative value means high priority, positive value means low priority |
| VIRT    | process use virtual memory size                                                   |
| RES     | process use physical memory size, unit is Kb, RES = CODE + DATA                   |
| SHR     | shared memory size, unit is Kb                                                    |
| %CPU    | CPU time usage percentage from last update to now                                 |
| %MEM    | process use physical memory percentage                                            |
| TIME+   | process use CPU time total, unit is 1/100 second                                  |
| COMMAND | process name                                                                      |

- shortcut for `top` UI
  - 1: show multi-core CPU usage
  - p: order by CPU usage
  - m: order by memory usage
  - n: order by PID
  - k: [kill](linux-kill.md)
  - r: [renice]() process

## fg

## bg
