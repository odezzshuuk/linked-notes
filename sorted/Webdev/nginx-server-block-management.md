# Nginx - Server Block Management

> sites-available and sites-enabled are not requirement for nginx

## What Is A Server Block

- Is a configutation block that defines setting of a server
- this is a [`server { }`](nginx-directives-list.md#server) block
- also called **virtual host**

## 2 methods to create Virtual Host

1. directly add `server` block `nginx.conf`
2. use [`sites-available` and `sites-enabled`]

> `sites-available` and `sites-enabled` are not requirement for nginx

## Introduction To sites-available and sites-enabled

- sites-available
  - path: `/etc/nginx/sites-available`
  - A directory containing all of your virtual host files
  - nginx will not directly read files in `site-available`
  - nginx will not use any of the files in this directory unless they are linked to the `sites-enabled` directory
- sites-enabled
  - path: `/etc/nginx/sites-enabled`
  - A directory of [symlinks]() to files in `sites-available`
  - nginx will read all configuration file in this directory

why separate `sites-available` and `sites-enabled`?

- provide a convenient way to manage virtual host
- when create a configuration in `sites-available`, it doesn't automatically take effect

## Illustration Code

`/etc/nginx/nginx.conf`

```
http {
    include /etc/nginx/sites-enabled/*;
}
```

`/etc/nginx/sites-available/example.com`

```
server {
    listen 80;
    server_name example.com;
    location / {
        root /data/www;
    }
}
```

Enable A Server Block configuration

- create a symlink to the configuration file in `sites-enabled`

```sh
ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com
```

Disable Server Block configuration

- remove the symlink

```sh
rm /etc/nginx/sites-enabled/example.com
```
