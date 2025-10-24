# java.net.URL

## Feature

- The URL class **does not** decode or encode its string content according to the mechanism defined by RFC2396
- **The caller is responsible** for encoding escape characters before invoking

## Practical Use

Create Absolute URL

```java
URL url = new URL("/a-guide-to-java-sockets");
URL home = new URL("http://www.example.com");
```

Create Relative URL

```java
URL url = new URL(home, "/a-guide-to-java-sockets");
```

Get URL Component

```java
URL url = new URL("http://www.example.com:80/a-guide-to-java-sockets");
url.getPort();  // 80
url.getHost();  // "www.example.com"
url.getProtocol();  // "http"
```

## Create URL Instance

`URL(String spec)`

`URL(String protocol, String host, int port, String file)`

```java
public void test() {
  String protocol = "http";
  String host = "www.example.com";
  String file = "/articles?topic=java&version=8";
  URL url = new URL(protocol, host, file);
}
```

`URL(String protocol, String host, int port, String file, URLSTreamHandler handler)`

`URL(String protocol, String host, String file)`

`URL(URL context, String spec)`

`URL(URL context, String spec, URLStreamHandler handler)`

## Method

- `new URL(String);` Construct a URL object

- `public InputStream openStream();`: Obtain resource content

  - Equivalent to `openConnection().getInputStream()`
