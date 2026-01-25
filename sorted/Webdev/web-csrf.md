# CSRF

- CSRF: cross site request forgery
- Tricks a user's browser into visiting a previously [authenticated](springsecurity-authentication.md) website and performing certain operations; because the user is authenticated, the website will consider this request to be the user's own operation

## Take A Look

- nodejs express framework

localhost:3000/

```js
app.get('/', csrfProtection, (req, res) => {
  req.send(`
    <form action="/transfer-money" method="POST">
      <input type="text" name="amount" placeholder="amount" />
      <input type="text" name="to" placeholder="Send to ...">
      <input type="hidden" name="_csrf" value="${req.csrfToken()}">
      <button>Submit</button>
    </form>
  `);
});
```

anotherhost:3000/

```js
app.get("/", (req, res) => {
  res.status(200).send(`
    <h1>Bad Guy SIte Pretending To Be Good Site</h1>
    <form action="http://localhost:3000/transfer-money" method="POST">
      <input name="amount" type="hidden" value="99999" />
      <input name="to" type="hidden" value="Bad Guy"/>
      <button>Click If You Like Puppies</button>
    </form>
   `)
})
```

## CSRF Prevention Cheat Sheet

In short

- framework built-in CSRF protection
- stateful software use [synchronizer token pattern]()
- stateless software use [double submit cookie](#double-submit-cookies)
- **Additional** **deep** measures, at least one of the following:
  - [SameSite Cookie Attribute](/sorted/network/http-cookie.md)
  - Implement user interaction-based protection measures
  - Consider using custom request headers
  - Use [origin header](/sorted/network/http-request-message.md#request-header)
- **Any [XSS] can defeat csrf defense measures**
- Don't use GET in requests that modify state

### SameSite Cookie Attribute

- A method to protect users from CSRF attacks through the browser

### double submit cookies

## demonstrate code

[example](/sorted/code-snippet/javascript/csrf-attack-and-prevention.md)
