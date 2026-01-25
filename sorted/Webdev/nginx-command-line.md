# Nginx - Command Line

```sh
nginx [options] [args]
```

## options

`-s signal`

- signal can be one of the following:
  - stop
  - quit
  - reload
  - reopen

`-g directives`: set global [directives](nginx-directives-list.md)

`-?, -h`

`-t`

`-v`

`-c`

`-p`

## start and stop nginx service

```sh
nginx -s <signal>
```

