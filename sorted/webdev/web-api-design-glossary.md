# Web - API Design Glossary

* [EndPoint](#endpoint)
* [Protocol Buffers(ProtocolBuf)](#protocol-buffers(protocolbuf))


## EndPoint

- API's URL or function that client can request or call to interact with server

## Protocol Buffers(ProtocolBuf)

- A data format developed by Google
- For faster and smaller serializing structured data 

```proto
message User {
  string id = 1;
  string name = 2;
  string email = 3;
}
```

Data in air Looks like

```
00001010 00100001 01001100 ...
```
