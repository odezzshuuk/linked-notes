# Entity and Encoding

- HTTP entity headers describe the content of an HTTP message.
- HTTP/1.1 defines 10 basic header fields:
  - [Content-Type](http-content-type.md): Entity object type
  - Content-Length: Length of the entity after encoding
  - Content-Language: Human language matching the object
  - Content-Encoding: Any transformations applied to the object data (e.g., compression)
  - Content-Location: Alternate location from which the object can be obtained when requested
  - Content-Range: If this is a partial entity, this header specifies which part of the whole it is
  - Content-MD5: Checksum of the entity body content
  - Last-Modified: Date and time when the transmitted content was created or last modified on the server
  - Expires: Date and time when the entity data will expire
  - Allow: Various request methods allowed for this resource, such as GET, HEAD
  - ETag: Unique validation code for this specific instance of the document
  - Cache-Control: Indicates how the document should be cached

