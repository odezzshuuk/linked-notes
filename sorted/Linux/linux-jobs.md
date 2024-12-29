# Linux - Jobs

## Features

- **single process or multiple processes** wrapped with job meta information, such as job id, job status...
- An shell-level abstraction of single or multiple processes
- Can be managed by command such as `fg`, `bg`, `jobs`
- **Shell dependency**
- When a job is created, one or more processes are created
- But Not vice versa, process can exist without job

## Switch Between Suspend Process And Command Line

Suspend current job

- `ctrl + z`: suspend current job

Resume most recent suspended process

```sh
fg
```

Resume a job by job id

```
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


