# pthread_create()

```c++
#include <pthread.h>

int pthread_create(pthread_t *thread, 
                   const thread_attr *attr,
                   void *(*start_routine*)(void *),
                   void *arg);
```

