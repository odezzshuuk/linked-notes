# Http - Cross-Origin Resource Sharing (CORS) Preflighted Requests

## What It is

- Used to check if the server supports CORS.

## Send Preflighted Request

- Header method is [`OPTIONS`](http-request-method.md#options).
- Browser automatically sends preflighted request.
- Sends an HTTP request to check if the server supports CORS, generally including the following headers:
  - Origin
  - Access-Control-Request-Method
  - Access-Control-Request-Headers

Code that will trigger a preflighted request:

```js
const xhr = new XMLHttpRequest();
xhr.open('POST', 'https://bar.other/resources/post-here/');
xhr.setRequestHeader('X-PINGOTHER', 'pingpong');
xhr.setRequestHeader('Content-Type', 'application/xml');  // cause preflighted request
xhr.onreadystatechange = handler;
xhr.send('<person><name>Arun</name></person>');
```

- Because the `Content-Type` header is `application/xml`, the browser will send a preflighted request.

Interaction process of client and server:

- The first interaction is a preflighted request/response.

1. Client sends preflighted request.

- Contains `OPTIONS` [request line](http-request-message.md#request-line).
- Contains `Origin: http://foo.example` [header field](http-request-header.md).
- Contains `Access-Control-Request-*` [header field](http-request-header.md).

2. Server responds to HTTP preflighted request.

- Includes `Access-Control-Allow-Origin: http://foo.example` [header field](http-response-message.md#header-lines).

3. POST Request

- Will not carry `Access-Control-Request-*` [header field](http-request-header.md).

4. Server side response

- Carries `Access-Control-Allow-Origin` [header field](http-request-header.md).
- Carries `Vary: Accept-Encoding, Origin` [header field](http-request-header.md).

## Condition that will not trigger a preflighted request

- Request method is one of `GET`, `HEAD`, `POST`.
- Contains automatically set header fields:
  - Accept
  - Accept-Language
  - Content-Language
  - Content-Type
    - Only limited to `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`.
- Any [XMLHttpRequest](javascript-bom-xmlhttprequest.md) object has no event listeners registered.
- No [ReadableStream] object is used.

## If the server allows, it will respond to this preflight request.

Generally includes the following header fields:

- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Max-Age: During this time, the browser does not need to send a preflight request again for the same request.
- Access-Control-Allow-Credentials
- Access-Control-Expose-Headers
