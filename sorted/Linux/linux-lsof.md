# Linux - Command lsof

## What is lsof used for

- List open files
- Usually used to check network status

## Practical Use

check specific ports status

```sh
lsof -i:8080
```

check listening ports

```sh
lsof -i -P | grep -i "listen"
```

check which port occupied by specific process

```sh
lsof -i -P -n | grep pid
```

## Options

`-i address`: list internet and x.25 (HP-UX) **network files**

- if `address` is not specified, all internet files are listed
- sample `address` value
  - `-i4`: IPv4
  - `TCP:25`: TCP and port25
  - `@172.217.27.14`: internet address 172.217.27.14

`-n`: inhibit the conversion of network numbers to host name

`-p` 

- list the files for the process

`-P`: inhibit the conversion of port numbers to port names for network files

