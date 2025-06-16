# linux -command netstat

* [Description](#description)
* [Output](#output)
* [Practical Usage](#practical-usage)

## Description

- `sudo apt install net-tools`

`netstat -[a/n/t/u/l/p/c]`

- `-r` routing table
- `-n` show numerical address
- `-a` show both listening and non-listening sockets
- `-t` Only TCP
- `-u` Only UDP
- `-l` Show Only Listening Sockets
- `-c` print the selected information every second

## Output

- Proto: the protocol tcp, udp, udpl, raw
- Local Address: Address and port number
- Foreign Address: Address and port of remote end of the socket
- stat: [state of the socket](tcp-status.md)

## Practical Usage

1. display all listening ports with corresponding process and PID

```sh
sudo netstat -tulpn
```

2. dipslay all connections to a port 80 with the process and PID

```sh
sudo netstat -tulpn | grep :80
```

- **sudo** is required for process and PID display
- the output like this

```sh
tcp        0      0 0.0.0.0:27017           0.0.0.0:*               LISTEN      3270/rootlesskit
tcp6       0      0 :::27017                :::*                    LISTEN      3270/rootlesskit
```

3. display all open ports with their process and PID

```sh
sudo netstat -tunlp
```

4. display all connections for specific ip address and port

```sh
netstat -an | grep <ip_address>:<port>
```

