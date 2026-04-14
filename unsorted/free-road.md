# Free Road

## Set Proxy

linux

- proxy server is known

```bash
export https_proxy=http://127.0.0.1:11001 http_proxy=http://127.0.0.1:11001 all_proxy=socks5://127.0.0.1:11000
```

windows

```bash
export https_proxy=http://192.168.231.1:8100 http_proxy=http://192.168.231.1:8100 all_proxy=socks5://192.168.231.1:810
```

Settings $\rightarrow$ network and Internet $\rightarrow$ proxy $\rightarrow$ proxy ip and port

## Goflyway

[Goflyway](https://github.com/bannedbook/fanqiang/wiki/goflyway%e5%85%8d%e8%b4%b9%e8%b4%a6%e5%8f%b7)

## gofly

[gofly](https://we.gofly.cyou/)

## Auto Response

freeman105@gmail.com

## Reality Domain Test

```sh
for d in statici.icloud.com amd.com www.xilinx.com download.amd.com images.nvidia.com go.microsoft.com aws.com www.intel.com beacon.gtv-pub.com b.6sc.co ; do t1=$(date +%s%3N); timeout 1 openssl s_client -connect $d:443 -servername $d </dev/null &>/dev/null && t2=$(date +%s%3N) && echo "$d: $((t2 - t1)) ms" || echo "$d: timeout"; done
```
