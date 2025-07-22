# Http - Request Message

## Typical Request Message

```http
GET /api/data HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Accept: application/json
Accept-Language: en-US,en;q=0.9
Referer: https://www.example.com/
Connection: keep-alive

<content>
```
> When the request method is POST, the content is the form provided by the user.

## Request Line

`GET /api/data HTTP/1.1` request line

- First line of the request message, including:
  - [request method](http-request-method.md)
  - [URI](computer-network-uri.md)
  - request version

Request method, including GET, POST, HEAD, PUT, DELETE.

- [Method detail](http-request-method.md)

## Header Fields

[request-header](http-request-header.md)

## Empty Line

Represents `<CR><LF>`.

- `<CR>`
- `<LF>`

## Request Body

- When the request method is GET, the request body is empty.
- When the request method is POST, the request body is the [form](html-element-form.md) provided by the user.

