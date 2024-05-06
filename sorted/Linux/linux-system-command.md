# Linux - System

* [uname](#uname)
* [alternatives](#alternatives)
* [export](#export)
* [systemctl](#systemctl)

## env

[env command](linux-env.md)

## uname

- print system information

```bash
$ uname -s
Linux
```

## alternatives

[alternatives](linux-command-alternatives.md)

## export

```shell
export [-fnp] [name]=[value]
```

## systemctl

query service status

```bash
systemctl status service_name
```

start a service, set active status to success

```bash
sudo systemctl start service_name
```

mount service

- for example start service when system boot, or mount a hardware
- units may be enabled without being started and started without being enabled

```bash
sudo systemctl enable service_name
```

enable and start a service

```bash
sudo systemctl enable --now service_name
```
