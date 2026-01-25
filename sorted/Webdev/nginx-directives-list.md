# Nginx - Directives

## Top Level Directives

- `events`: General connection processing
- `http`: HTTP traffic
- `mail`: Mail traffic
- `stream`: [TCP/UDP](computer-network-tcp.md) traffic

## Traffic Handling Context

- `http`: HTTP traffic
- `mail`: Mail traffic
- `stream`: [TCP/UDP](computer-network-tcp.md) traffic

## server

- In each [traffic handling context](#traffic-handling-context), you can include one or more `server` blocks

```py
user nobody; # a directive in the 'main' context

events {
    # configuration of connection processing
}

http {
    # Configuration specific to HTTP and affecting all virtual servers  

    server {
        # configuration of HTTP virtual server 1       
        location /one {
            # configuration for processing URIs starting with '/one'
        }
        location /two {
            # configuration for processing URIs starting with '/two'
        }
    } 
    
    server {
        # configuration of HTTP virtual server 2
    }
}

stream {
    # Configuration specific to TCP/UDP and affecting all virtual servers
    server {
        # configuration of TCP virtual server 1 
    }
}
```

## server_name

> **Not To Define A [Domain Name](computer-network-domain-name.md)** Which map to an ip address or port
> Domain name can be defined in [/etc/hosts](linux-system-directory.md#/etc) for local test

- Used to define which server should be matched when a request is received
- Essentailly is to match the [`Host` header](http-request-header.md#Host) in the request

## upstream

- use to define a group of servers
- commonly used for defining [server cluster] for [load balancing]()

```conf
http {
    upstream backend_hosts {
        server backend1.example.com weight=5;
        server backend2.example.com:8080;
    }

    server {
        listen 80; 
        server_name www.domain.com;
        location / {
            proxy_pass http://backend_hosts;
        }
    }
}
```

- `www.domain.com` will be forwarded to one of the servers defined in `backend_hosts`



