# pthread_jion()

```c++
#include <pthread.h>
int pthread_join(pthread_t thread, void **retval)
```

- Waits for the thread 'thread' to finish. If retval is not NULL, the value provided to pthread_exit() by the target thread is copied to the object pointed to by retval.
- This is essentially a blocking wait.
- Returns 0 on success, or an error number on failure.
- Parameters:
  - thread: 
  - retval: If the retval parameter is not NULL, the exit status will be copied to the address pointed to by retval.

