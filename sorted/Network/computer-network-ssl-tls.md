# Computer Network - SSL/TLS

* [What It Is](#what-it-is)
* [Feature](#feature)
* [Entity in SSL/TLS](#entity-in-ssltls)
* [Steps For Client To Trust A Server](#steps-for-client-to-trust-a-server)
* [Trust Of Chain](#trust-of-chain)
* [VS SSH](#vs-ssh)
* [Question](#question)

## What It Is

- **Used to ensure client talking to the correct server**.
- A cryptographic protocol.
- Abbreviation of Secure [Socket](computer-network-socket.md) Layer.
- Which [Https](computer-network-https.md) is based on.
- More popularly protocol is TLS (Transport Layer Security).

## Feature

- Server holds the [private key](computer-network-asymmetric-key.md#private-key).
- Server sends digital certificate to client.

## Entity in SSL/TLS

[Digital Certificates](ssl-tls-digital-certificates.md)

[Certificate Authority](ssl-tls-certificate-authority.md)

Session Key

- Used to encrypt and decrypt **data**.
- A [symmetric key](computer-network-cryptographic-key.md#symmetric-key).

## Steps For Client To Trust A Server

1. Client [handshakes](computer-network-reliable-transmission.md#three-way-handshake) with server.
2. Server Hello

- Client sends hello message to server, in this message it tells server:
  - What TLS version it supports.
  - Which [cipher suite](#cipher-suite) it supports.
- Server sends hello message to client, in this message it tells client:
  - What TLS version it chooses.
  - Which cipher suite it chooses.
- Server then sends another [packet](computer-network-tcp-segment-structure.md) to client, which contains:
  - [Digital certificate](ssl-tls-digital-certificates.md).
  - Which contains the [public key](computer-network-asymmetric-key.md#public-key).
- Server sends FIN to client, which means the handshake is done.

3. Certificate Verification. The Verification on my understanding:

- Client [public key](computer-network-asymmetric-key.md#public-key) which:
  - Stored in pre-installed [digital certificate](ssl-tls-digital-certificates.md) which:
    - Issued by Root [CA](ssl-tls-certificate-authority.md).
- Will be decrypted by [private key](computer-network-asymmetric-key.md#private-key).
  - Stored in Root CA.

4. Key Exchange

- Generate [Session Key](#session-key) by server's public key.
- Used to encrypt and decrypt data between client and server.

5. Secure Data Transfer

- Use [Session Key](#session-key) to encrypt and decrypt data between client and server.

## Trust Of Chain

[Trust Of Chain](ssl-tls-chain-of-trust.md)

## VS SSH

[ssh](computer-network-ssh.md)

- More emphasis on **communication** between client and server.

## Question

Certificate Verification is online or offline?

- Locally is offline.
- **Maybe browser will do online verification**.

Does digital certificate contain the private key?

