# SSL/TLS - Digital Certificates

## What It Is

> Known as **SSL certificate** or **X.509 certificate**.

- A file with various formats, such as `.pem, .crt, .cer, .der`.
- A certificate may be valid for multiple hostnames, [Subject Alternative Names (SANs)**](#subject-alternative-name-san).

## Feature

- Contains **public key**.
- Contains the information.

## Take A Look

> Certificate of YouTube.

General information of **certificate content**:

```
Issued To

  Common Name (CN): `*.google.com`
  Organization (O): `<Not part of certificate>`
  Organizational Unit (OU): `<Not part of certificate>`

Issued By

  Common Name (CN): `GTS CA 1C3`
  Organization (O): `Google Trust Services LLC`
  Organizational Unit (OU): `<Not part of certificate>`

Validity Period

  Issued On: Monday, 8 June 2020 at 4:20:08 PM
  Expires On: Monday, 31 August 2020 at 4:20:08 PM

Fingerprints

  SHA256 Fingerprint: `E4:5F:6F:3B:9F:5F:9B:9F:2B:8F:1B:5F:9F:5F:9F:5F:9F:5F:9F:5F`
  SHA1 Fingerprint: `E4:5F:6F:3B:9F:5F:9B:9F:2B:8F:1B:5F:9F:5F:9F:5F:9F:5F:9F:5F`
```

- Its [CA](ssl-tls-certificate-authority.md) is `GTS CA 1C3`.
- Issued to `*.google.com`.

Look at detail:

- [SAN](#subject-alternative-name-san)

```
Not Critical
DNS Name: *.google.com
DNS Name: *.appengine.google.com
DNS Name: *.bdn.dev
DNS Name: *.origin-test.bdn.dev
DNS Name: *.cloud.google.com
...
```

## Self-Signed Certificate

How to get a self-signed certificate:

- Like [OpenSSL](linux-openssl.md).

## Public Trusted Certificate

How to get a public trusted certificate:

- Send a certificate signing request (CSR) to a [CA](ssl-tls-certificate-authority.md).

---

## Subject Alternative Name (SAN)

## Wildcard Certificate
