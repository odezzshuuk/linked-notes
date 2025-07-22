# Http - Request Method

## GET

- Retrieves data specified by [URI](computer-network-uri.md).
- Sends data in [query string](computer-network-url.md#query-string).
- Data length is limited by URL or browser.
- Can be cached by browser because it's considered safe.
- **Considered idempotent**:
  - Meaning multiple identical requests should have the same effect as a single request.
  - Has no side effect on the server.

## POST

- Often used to submit forms, upload files.
- Sends data in [request body](http-request-message.md#request-body).
- Data length is not limited.
- **Not considered idempotent**: because it may **change server** state.

## PUT

- Commonly used to **update** existing resources.
- **Considered idempotent** like [GET](#get).

## DELETE

## PATCH

## HEAD

## OPTIONS

- Requests information about communication options available for the target resource or server, including:
  - Allowed methods
  - Headers
  - Authentication requirements
  - Supported content types
  - ...
- Often used in the context of Cross-Origin Resource Sharing.

