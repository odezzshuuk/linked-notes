# Compute Network - URL

- [What is this](#what-is-this)
- [Common Format](#common-format)
- [Host and Port](#host-and-port)
- [User Name and Password](#user-name-and-password)
- [Parameter](#parameter)
- [Query String](#query-string)
- [Fragment](#fragment)
- [Relative URL](#relative-url)
- [Encoding Mechanism](#encoding-mechanism)
- [VS URI](#vs-uri)

## What is this

- Uniform Resource Locator

For URL address: `http://www.baidu.com/someDepartment/picture.gif`

- `http:` protocol
- `www.baidu.com`: host name
- `/someDepartment/picture.gif`: resource path

## Common Format

`<scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<frag>`

| component | description | default value |
| --------- | ----------- | ------------- |
| scheme    | protocol    | no default    |
| user      | user name   | Anonymous     |
| password  |             |               |
| host      |             |               |
| port      |             |               |
| path      |             |               |
| params    |             |               |
| query     |             | no default    |
| frag      |             | no default    |

## Host and Port

```
http://www.baidu.com:80/index.gif access resource by host name
http://161.58.228.45:80/index.html access resource by ip address
```

> HTTP of TCP protocol, default port is 80.

## User Name and Password

```
ftp://ftp.prep.ai.mit.edu/pub/gnu
ftp://anonymous@ftp.prep.ai.mit.edu/pub/gnu
ftp://anonymous:mypasswd@ftp.prep.ai.mit.edu/pub/gnu
http://joe:joespasswd@www.joes-hardware.com/sales
```

## Parameter

## Query String

<center>
http://www.joes-hardware.com/inventory-checkj.cgi?item=12345&quantity=1
</center>

- Right of `?` is query component.
- `?key1=value1&key2=value2` provides additional parameters to the network server.

> Gateway can be used as an access point to other applications.

## Fragment

- Used to further divide the resource.

## Relative URL

- Omits the [scheme](#common-format), [host](#host-and-port), and other components that can be deduced from the base URL of the owning resource.
- Provides a set of resources portability.

## Encoding Mechanism

> For users who want to include binary data or characters other than common ASCII in the URL.

- Uses `%` followed by two hexadecimal digits to represent one Unicode character.

## VS URI

- More general **concept**.

> **Not** a more **general format**.

- URL is a subset of URI.

[URI](network-uri.md)

