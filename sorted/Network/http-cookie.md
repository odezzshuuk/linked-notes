# Cookie

- [feature](#feature)
- [How it works](#how-it-works)
- [set cookie to client](#set-cookie-to-client)
- [cookies in request](#cookies-in-request)
- [cookies properties](#cookies-properties)
- [access to cookies by browser console](#access-to-cookies-by-browser-console)
- [security problem](#security-problem)
- [Session cookies and persistent cookies](#session-cookies-and-persistent-cookies)

## feature

- Stored on the **client-side**.
- Only stores string type data.
- Single cookie size limit is 4KB.
- Each **hostname** has corresponding cookies.
- **automatically** sent by browser to server.
- When cookie HttpOnly property is true, client-side javascript cannot access to cookie.

![cookie.svg](cookie.svg)

## How it works

- When a user first visits the server, the server sets a cookie in the response message using the **Set-Cookie** [header field](http-response-message.md).
- When visiting again, the browser sends the cookie to the server; the request message carries the **Cookie** [header field](http-request-message.md).

## set cookie to client

- The server sets cookies via the **Set-Cookie** [header field](http-response-message.md).

Use [nodejs express](nodejs-express-api-response.md)

```js
import express from `express`;
const app = express();
app.get('/', (req, res) => {
  res.cookie('sky', 'blue');
  res.cookie('name', 'value', { maxAge: 900000, httpOnly: true });
  res.send('cookie set'); // cookie set
});
app.listen(3000);
```

The response message contains `Set-Cookie` related fields:

```http
Set-Cookie: name=value; Max-Age=900000; Path=/; HttpOnly
Set-Cookie: sky=blue; Path=/
```

When visiting the server again, the browser sends the Cookie to the server. The Cookie field looks like:

```http
Cookie: sky=blue; name=value
```

## cookies in request

```http
cookies: key1=value1; key2=value2; key3=value
```

## cookies properties

- key
- value
- Domain
- Path
- Expires: Expiry date of cookie in [GMT]()
- Secure: marked the cookies to be used with HTTPS only
- HttpOnly
  - true: cookie can only be accessed by the web server
  - false: cookie can be accessed by client side script
- SameSite
  - Strict:
  - Lax: default value
  - None:

> Max-Age: convenient to set expire time

---

SameSite:

- If the value is Strict, it prevents the browser from sending cookies across all cross-site requests. Although it can prevent CSRF attacks, it also prevents cookies from being sent to regular links, such as a user logged into Github being unable to access other links published on Github.
- If the value is Lax

## access to cookies by browser console

Only can access to cookies which flag **`HttpOnly` is false**.

`document.cookies`

## security problem

- [csrf](web-csrf.md) attack

[best example](https://github.com/learnwebcode/youtube-cookies-and-more/tree/main/01-cookies)

## Session cookies and persistent cookies

- Session cookies
  - A temporary cookie.
  - Expires when the browser is closed.
- Persistent cookies
  - A long-term valid cookie.
  - Achieved by setting an expiration time.
- The only difference in expiration time between session cookies and persistent cookies:
  - Session cookies:
    - Set `Max-Age` to 0.
    - Set `Expires` to a past time.
  - Persistent cookies:
    - Set `Max-Age` to a positive number.
    - Set `Expires` to a future time.
