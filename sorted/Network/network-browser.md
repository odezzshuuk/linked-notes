# Browser

## Subresource Integrity

[Subresource Integrity]()

- Enables browsers to verify the integrity of the resources they fetch, checking for potential tampering.
- The principle allows the browser to provide a cryptographic hash value of the resource to be fetched; the cryptographic hash value of the fetched resource must match.

How it helps:

- When using a [CDN](/sorted/frontend/cdn.md), it prevents attackers from tampering with resources fetched from the CDN.
