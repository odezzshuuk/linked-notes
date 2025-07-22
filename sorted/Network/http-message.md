# HTTP Message

## What Is This

- Is a [formatted message](#message-format) used to transfer data between client and server.
- Divided into two parts:
  - [request message](#request-message)
  - [response message](#response-message)

## Message format

- Encode character set: ISO-8859-1

<table>
  <tr>
    <td>message header</td>
  </tr>
  <tr>
    <td>empty line(CR+LF)</td>
  </tr>
  <tr>
    <td>message body</td>
  </tr>
</table>

> CRLF: abbreviations of Carriage Return and Line Feed
>> CR: `\r`, CR, 13, 1010
>> LF: `\n`, LF, 10, 1001

## Request Message

[request message](http-request-message.md)

## Response Message

[response message](/sorted/network/http-response-message.md)

## Content Encode

[content encode](http-content-encode.md)

## Take a look at message header

- Stored in format `key: value`.

Use response message as example:

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 55743
Connection: keep-alive
Cache-Control: s-maxage=300, public, max-age=0
Content-Language: en-US
Date: Thu, 06 Dec 2018 17:37:18 GMT
ETag: "2e77ad1dc6ab0b53a2996dfd4653c1c3"
Server: meinheld/0.6.1
Strict-Transport-Security: max-age=63072000
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Vary: Accept-Encoding,Cookie
Age: 7

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>A simple webpage</title>
</head>
<body>
  <h1>Simple HTML5 webpage</h1>
  <p>Hello, world!</p>
</body>
</html>

```

Header fields in the above message are:

- `Content-Type`
- `Content-Length`
- `Connection`
- `Cache-Control`
- `Content-Language`
- `Date`
- `ETag`
- `Server`
- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `X-XSS-Protection`
- `Vary`
- `Age`


