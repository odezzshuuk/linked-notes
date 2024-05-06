# Linux - Universal Socket Address Struct

## New Struct

- `sa_family`:
- `__ss_align`:
- `__ss_padding[128-sizeof(__ss_align)`:

## Old Struct 

- `sin_family`: `sa_family_t` 
- `sa_data[14]` : `char`, address value

```c
#include <bits/socket.h>
struct sockaddr
{
  sa_family_t sa_family;  // sa_family_t
  char sa_data[14];  // 
}
```

