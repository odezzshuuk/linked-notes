# C Preprocessor - pragma

## What's For

- Control the behavior of the compiler in some way

```c
int main() {
    #pragma message "Compiling " __FILE__ " at " __TIME__
    return 0;
}
```


