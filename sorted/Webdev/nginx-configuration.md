# Nginx - Configuration

* [Configuration File](#configuration-file)
* [Configuration File Structure](#configuration-file-structure)
* [How To Write Configuration File](#how-to-write-configuration-file)
* [Setting Up Simple Proxy Server](#setting-up-simple-proxy-server)

## Configuration File

Nginx will read configuration file from this 3 places:

> usually use only one of them

- `/etc/nginx/nginx.conf`
- ~~`/usr/local/nginx/conf/nginx.conf`~~
- ~~`/usr/local/etc/nginx/nginx.conf`~~

## Configuration File Structure

configuration file is made up of **directives**

```
http {
    server {
        listen 80;
        server_name example.com;
        location / {
            root /data/www
        }
    }
}
```

- `server`, `location`, `root`, `index` are directives 
- `server` block is the basic unit of configuration file

Top-Level directives

- `events`
- `http`: 
- `mail`
- `stream`

## How To Write Configuration File

```conf
http {
    server {
        listen 80;
        server_name example.com;
        location / {
            root /data/www
        }
    }
}
```

- location block
  - `/`: The prefix. Use to match the uri from the request
  - `root /data/www`: where server will look for the requested files

for request `http://localhost/some/example.html`

the file `/data/www/some/example.html` will be served

## Setting Up Simple Proxy Server

For nginx config like This

```sh
http {
    server {
        listen 80;

        root /data/up1;

        location / {
            proxy_pass http://localhost:8080;
        }

        location /images {
            root /data;
        }

        location ~ \.(git|jpg|png)$ {
            root /data/images;
        }

    }
}
```

the config file above means:

1. this will be a simple server listening on port 80
2. request uri without [path](computer-network-uri.md) `http:/www.example.com/` will be forward to `http://localhost:8080`
3. other request with [path](computer-network-uri.md) will be served from `/data/up1` directory
4. request to `www.example.com/image/foo.jpg` will be served from `/data/images/foo.jpg`

- If `/images` root write like this `root /data/images;`
- This request will be served from `/data/images/images/foo.jpg`
- generally, the served path is `/root` + `request/uri/path`

5. request ending with `.git`, `.jpg`, `.png` will be mapped to `/data/images` directory

- regular expressoin should be preceded with `~` or `~*`, `~*` means case insensitive
- `\.(git|jpg|png)` is a regular expression matching uri ending with `.git`, `.jpg`, `.png`

