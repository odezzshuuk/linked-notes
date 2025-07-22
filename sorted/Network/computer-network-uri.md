# URI

- [Syntax](#syntax)
- [Opaque URI](#opaque-uri)
- [Hierarchical URI](#hierarchical-uri)

## Syntax

`[scheme]://[authority][path][?query][#fragment]`

For example:

```
https://www.example.com/products/laptops?brand=dell&price=1000#section-1`
```

- `https` is the scheme
- `www.example.com` is the authority
- `/products/laptops` is the path
- `brand=dell&price=1000` is the query
- `section-1` is the fragment

## Encoded URI

- URI may have special characters, which cannot be transmitted over the internet.

## Opaque URI

```text
mailto: java-net@www.example.com
news: comp.lang.java
urn:isbn:096139210x
```

## Hierarchical URI

```text
http://exaple.com/languages/java/
sample/a/index.html#28
../../demo/b/index.html
file:///~/calendar
```

- Hierarchical URI syntax that needs further parsing:

`[scheme:][//authority][path][?query][#fragment]`

- Server-based hierarchical URI syntax:

> Currently, almost all URI schemes used are based on server-based hierarchical URI syntax.

`[user-info@][host][:port]`

