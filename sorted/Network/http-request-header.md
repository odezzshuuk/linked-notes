# Request Header

## Typical Request Header

```http
GET /api/data HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Accept: application/json
Accept-Language: en-US,en;q=0.9
Referer: https://www.example.com/
Connection: keep-alive
```

## Referer

- Allows the server to identify the source of the request.
- When a client **clicks on a link** or makes a request to the server, the browser will add the `Referer` header to the request.

## Host

- Specifies the domain name of the server which the client wants to connect to.
- This is essential when a single web server hosts multiple websites.

## Connection

`Connection: close`:

`Connection: Keep-Alive`: Represents the client's wish to keep the connection open, default in HTTP/1.1.

- If `Connection: Keep-Alive`, then add `Keep-Alive` header.
- `Keep-Alive: timeout=5, max=1000`
  - timeout: idle time for connection to be kept open.
  - max: maximum number of requests before the server closes the connection.

```
GET / HTTP/1.1
Host: www.example.com
Connection: Keep-Alive
Keep-Alive: timeout=5, max=1000
```

`Connection: Upgrade`: Represents the client's wish to upgrade to another protocol, like HTTP/2.0, HTTPS, [WebSocket](javascript-websocket.md).

- If `Connection: Upgrade`, then add `Upgrade` header.
  - `Upgrade: websocket`: Represents the client's wish to upgrade to WebSocket protocol.

```
GET / HTTP/1.1
Host: www.example.com
Connection: Upgrade
upgrade: HTTP/2.0, HTTPS, WebSocket
```

- If the server decides to upgrade, the `101` [response status code]() will be sent.
- Response sent to original using new protocol.

## User-Agent

- Browser type of the request sender.

## Accept-Language

- Language that the client wants to receive.

