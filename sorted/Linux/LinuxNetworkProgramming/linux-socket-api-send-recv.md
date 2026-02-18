# linux socket api - send and recv

```c++
#include <sys/types.h>
#include <sys/socket.h>

ssize_t send(int sockfd, void *buf, size_t len, int flags);
ssize_t recv(int sockfd, const void *buf, size_t len, int flags);
```
