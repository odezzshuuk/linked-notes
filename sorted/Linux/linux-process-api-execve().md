# execve()

```cpp
#include <unistd.h>

extern char **environ;

int execve(const char *pathname, char *const argv[],
           char *const envp[]);
int execl(const char *pathname, const char *arg, ...
                /* (char  *) NULL */);
int execlp(const char *file, const char *arg, ...
                /* (char  *) NULL */);
int execle(const char *pathname, const char *arg, ...
           /*, (char *) NULL, char *const envp[] */);
int execv(const char *pathname, char *const argv[]);
int execvp(const char *file, char *const argv[]);
int execvpe(const char *file, char *const argv[],
            char *const envp[]);
int fexecve(int fd, char *const argv[], char *const envp[]);                       
```

