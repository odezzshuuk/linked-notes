# Nginx - Log

## default log file

- access.log: `/var/log/nginx/access.log`
- error.log: `/var/log/nginx/error.log`

## enable access log

```
```

## Set up Access Log

```c
http {
    access_log /var/log/nginx/access.log;
    server {
        listen 80;
        server_name example.com;
        access_log /var/log/nginx/example.com.access.log;
    }
}
```
