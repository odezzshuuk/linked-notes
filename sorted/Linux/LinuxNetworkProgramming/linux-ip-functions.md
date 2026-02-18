# IP

## ipv4 only

```c++
#include <arpa/inet.h>
in_addr_t inet_addr(const char* strptr);
```

```cpp
#include <arpa/inet.h>
int inet_aton(const char* cp, struct in_addr* inp) 
```

```cpp
#include <arpa/inet.h>
char* inet_ntoa(struct in_addr in);
```

## both ipv4, ipv6

```cpp
#include <arpa/inet.h>
int inet_pton(int af, const char* src void* dst)
```

```cpp
const char* inet_ntop(int af, const void* src, char* dst socklen_t cnt)
```
