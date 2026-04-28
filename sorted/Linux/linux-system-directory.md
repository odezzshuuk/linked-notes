# linux System Directory

* [/bin](#/bin)
* [/sbin](#/sbin)
* [/usr](#/usr): system program
* [/usr/bin](#/usr/bin)
* [/usr/sbin](#/usr/sbin)
* [/usr/local/bin](#/usr/local/bin)
* [/usr/src](#/usr/src)
* [/boot(not really understand)](#/boot(not-really-understand))
* [/etc](#/etc): config
* [/opt](#/opt): add-on program
* [/home](#/home)
* [/lib](#/lib)
* [/dev](#/dev)
* [/media](#/media)
* [/mnt](#/mnt)
* [/proc](#/proc)
* [/root](#/root)
* [/sys](#/sys)
* [/tmp](#/tmp)
* [/var](#/var)
* [Some other directory may have](#some-other-directory-may-have)
* [Summary of Diverse bin directories](#summary-of-diverse-bin-directories)
* [Summary](#summary)

## /bin

- stands for [binary](executable-file.md)
- system core function for all user
- Do not change with **different linux distributions**
- like `ls`, `cp`, `mv`, `mkdir`

## /sbin

- Stand For System [Binary](executable-file.md)
- executable files used by system administrator or root user
- and system [daemons](linux-daemon.md) or [services]()
- like `fdisk`, `ifconfig`, `shutdown`

## /usr

- Abbreviations of **Unix System Resources**, NOT **user**
- Stores **programs**, **library**, ~~data~~ for all users

> Like `Program Files` in windows

## /usr/bin

- [distribution](linux-distribution.md)-management program

## /usr/sbin

- same relationship to /usr/bin as /sbin to /bin 

## /usr/local/bin

- program compiled locally from source code

## /usr/src

- kernel source code default directory

## /boot(not really understand)

- ...

## /etc

- system related **configuration** files
- no binary here
- it is recommended to backup this directory

Useful files in this directory

- `/etc/passwd`: store user's information
- `/etc/shadow`: store user's password
- `/etc/profile`: [set environment variable](linux-system-environment.md)
- `/etc/hosts`: map hostname to locally ip addresses on without external [DNS](computer-network-dns.md)

```
127.0.0.1    localhost example.com 
::1 localhost ip6-localhost ip6-loopback
```
## /opt

- for add-on software packages
- for packages who are not part of [package management system](linux-software-install.md)

## /home

- **cd ~** enter home directory
- user's main directory
- every user have a directory whose name is same as user's name

## /lib

- lib is abbreviation of library
- like .dll in windows

## /dev

- device driver

`/dev/null`

- a special file that discards all data written to it

`dev/stdin`, `dev/stdout`, `dev/stderr`

- special file link to [`/proc/self/fd/0`, `/proc/self/fd/1`, `/proc/self/fd/2`](linux-file-descriptor.md#3-standard-file-descriptors)

## /media

- ...

## /mnt

- mount
- ...

## /proc

> `proc` is abbreviation of process

- `/proc` is a pseudo-filesystem
- content in this directory is not in **hard disk** but in **memory**

`/proc/self`

- a symbolic link to the process directory of the current process

## /root

- 

## /sys

- This is a significant change in the Linux 2.6 kernel. This directory contains the installation of the new file system called sysfs, which was introduced in the 2.6 kernel.
- This `sysfs` file system integrates information from three different file systems
  - `proc` file system: which provides information related to processes
  - `devfs` file system, which deals with devices
  - `devpts` file system, which handles pseudo-terminals
- this File system serves as an intuitive reflection of the kernel's device tree
- when a [kernel object]() is created, corresponding files and directories are also created in the kernel object subsystem

## /tmp

- Abbreviation of temporary, so this directory is used to store temporary files
- Such as sockets, PID files
- Files can be deleted at any time, especially on REBOOT

## /var

- variable data files that change over time
- commnon directory
  - `/var/log`: log files
  - `/var/run`: typically holds process id files and socket files

## Some other directory may have

/run

- /selinux
- /lost+found

## Summary of Diverse bin directories

`/bin`: program like `ls`, `cp`, `mv`, `mkdir`, `echo`
`/usr/bin`: program like  
`/usr/local/bin`: 
`/sbin`
`/usr/sbin`

## Summary

![linux1](/image/linux-directory-structure.png)
