# Network Programming

## Socket

[Socket](java-socket.md)

## URI, URL, URN

- A URI instance is just a structured string that supports syntax, canonicalization, parsing, and relativization operations
- A URL instance represents syntactic components
  - Supports parsing syntax
  - Looking up hosts
  - Opening network IO operations to specified resources

## URL类


[Net](java-net-url.md)

URLDecoder: HTML解码工具类

- Used to decode strings in application/x-www-form-urlencoded format

***

> [URL](http-url-and-uri): Uniform Resource Locator

## URI Class

[URI](network-uri.md)

- Applications **should not** attempt to construct or parse URIs directly from the string of a File or Path instance
- Use Path.toUri() and File.toURI() to create URIs
- Syntax: `[scheme:]scheme-specific-part[#fragment]`
- A URI instance consists of the following 9 parts:
  - scheme: String
  - scheme-specific-part: String
  - authority: String
  - user-info: String
  - host: String
  - port: int
  - path: String
  - query: String
  - fragment: String

Methods

1. Information

Decoded information

- `String getAuthority()`
- `String getFragment()`
- `String getHost()`
- `String getPath()`
- `int getPort()`
- `String getQuery()`
- `String getUserInfo()`

原始信息

- `String getRawAuthority()`
- `String getRawFragment()`
- `String getRawPath()`
- `String getRawQuery()`
- `String getRawUserInfo`

## 因特网地址: InetAdderss类

- 静态方法getByName(): 返回代表某个主机的InetAddress对象

```java
InetAddress address = InetAddress.getByName("time-a.nist.gov");
```

- 静态方法getAllByName(String host): 给定一个主机的名称，根据配置的系统解析器，返回其IP地址的数组。

```java
InetAddress[] addresses = InetAddress.getByName("time-a.nist.gov");
```

- getHostAddress(): 返回IP地址字符串
- getHostName(): 返回主机名称
