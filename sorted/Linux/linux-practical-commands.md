# Linux - Practical Command

* [list installed package](#list-installed-package)
* [remove related package](#remove-related-package)
* [switch between suspend process and command line](#switch-between-suspend-process-and-command-line)

## list installed package

```sh
dpkg-query --show --showformat='${Package}\n'
```

## remove related package

```sh
sudo apt remove $(dpkg-query --show --showformat='${Package}\n' | grep -i 'package-name')
```

