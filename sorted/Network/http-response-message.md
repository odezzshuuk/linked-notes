# Http - Response Message

* [Example response](#example-response)
* [Status Line](#status-line)
* [Header Lines](#header-lines)
* [Empty Line `<CR><LF>`](#empty-line-`<cr><lf>`)
* [Entity Body](#entity-body)

## Example response

```http
HTTP/1.1 200 OK
Connection: close
Date: Tue, 18 Aug 2000 15:11:03 GMT
Server: Apache/2.2.3 (CentOS)
Last-Modified: Tue, 18 Aug 2000 15:13:03 GMT
Content-Length: 6821
Content-Type: text/html

entity body
```

- Message in above example includes:
  - One Status Line
  - 6 Header Lines
  - One empty Line
  - Entity body
- Content-Type is restricted in [MIME](computer-network-mime-type.md).

## Status Line

Format: `<HttpVersion> <xxx> <status>`

- HttpVersion: HTTP version
- xxx: status code
- status: status code description

Official definition of `<xxx> <status>`, refer to [RFC1945-page26](https://tools.ietf.org/html/rfc1945#page-26).

- 200 OK: Request successful and response data is included in the response message.
- 201 Created: Request successful, and a new resource has been created.
- 202 Accepted: Request accepted for processing, but the processing has not been completed.
- 204 No Content
- 301 Moved Permanently: Request resource is permanently moved to another location; the new location is defined in the Location header line of the response message. The client application will automatically get the new URL.
- 302 Moved Temporarily: Request resource is temporarily moved to another location.
- 304 Not Modified:
- 400 Bad Request: General error code, indicates that the request is invalid.
- 401 Unauthorized: Request needs authentication.
- 403 Forbidden: Request is refused by the server.
- 404 Not Found: Requested resource is not found.
- 500 Internal Server Error
- 501 Not Implemented: Server does not support the functionality required to fulfill the request.
- 502 Bad Gateway: Server as gateway or proxy, receives invalid response from upstream server.
- 503 Service Unavailable: Server is unavailable for now (due to overload or maintenance).
- 505 HTTP Version Not Supported: Server does not support the HTTP protocol version used in the request.

> When the server responds with status 302, some browsers will send an empty request.

- 101 Switching Protocols: Server will switch to another protocol as client request.

Status code category:

| category | description       | meaning                                                        |
| :------: | :---------------- | :------------------------------------------------------------- |
|   1xx    | status code       | Not used, but reserved for future use                          |
|   2xx    | success code      | The action was successfully received, understood, and accepted |
|   3xx    | redirect code     | Further action must be taken in order to complete the request  |
|   4xx    | client error code | Server can't handle the request                                |
|   5xx    | server error code | Server raised error when handling the request                    |

## Header Lines

6 Common Header Lines:

- `Connection`
- `Date`
- `Server`
- `Last-Modified`
- `Content-Length`
- `Content-Type`: Response body content type, for example `Content-Type: text/html`.

## Empty Line `<CR><LF>`

- `<CR>`: Carriage Return, ASCII code is 13.
- `<LF>`: Line Feed, ASCII code is 10.

## Entity Body

- Loads the response content.

