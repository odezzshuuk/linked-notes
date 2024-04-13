# Linux - Jobs

## Switch Between Suspend Process And Command Line

when use `ctrl + z` to suspend process

- resume most recent suspended process

```sh
fg
fg %1
```

- check background process use `jobs`, which which get:

```sh
[1]+  Running                 command1 &
[2]-  Running                 command2 &
```

- `+` means the most recently started job
- `-` means the second most recently started job
- `jobs -l`: Display process IDs in addition the default information
- `jobs -p`: Display only the process IDs of background jobs
- `jobs -r`: Display only running background jobs
- `jobs -s`: Display Display only stopped background jobs


