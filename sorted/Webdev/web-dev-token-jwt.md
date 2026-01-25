# JWT Token

## What's This

- JWT: JSON Web Token

## Features

- Header, payload can be decoded, but [signature](#signature) is encrypted, can't be decoded
  - so the data source is reliable is guaranteed by signature
- Although header and payload can be decoded, but any manipulating will cause signature verification failure

## What's For

- Authentication: Guarantee the data source is **reliable**, verify whether the data has been tampered with
- Information exchange: jwt can be treated as a JSON object, can be used to verify whether the content has been tampered with

## How To Use

- Authorization: every request should include jwt, like single sign on

Detail

1. Client send a request to **authorization server**, when authentication success, server return a jwt
2. Client save jwt in [local storage](javascript-bom.md#localstorage) or [cookie](http-cookie.md), add jwt to request header every time
3. When user want to access protected resource, user should send a request with Authorization field in [request header](http-request-header.md)

> jwt should not contain too much information, some servers limit the request header size to 8kb, if you really need to include too much information, you can choose [alternative solution]

- combine jwt with httponly cookie can get extra security

## JWT Structure

[JWT Structure](web-dev-token-jwt-structure.md)

## JWT encode
