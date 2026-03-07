#  Linux - sigaction()

```c
#include <signal.h>

int sigaction(int signum, const struct sigaction *act,
              struct sigaction *oldact);
```

## sigaction struct

[sigaction struct](linux-system-struct-sigaction.md)
