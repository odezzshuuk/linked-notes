# Web - API Design - gRPC Style

## What It Is

- High-performance Remote procedure call(RPC) framework
- Developed by Google

## Features

- Binary serialization for compactness
- Code generating from [Protobuf schema](web-api-design-glossary.md#protocol-buffers(protocolbuf))
- Bidirectional streaming
- Less human readable

## How to Define On Server

- Define Services and messages in a `.proto` file
- Use frameworks: `grpc-node`, `grpc-dotnet`, `grpc-go`

`.proto` file

```proto
syntax = "proto3";

package userapi;

service UserService {
  rpc GetUser (GetUserRequest) returns (User);
}

message GetUserRequest {
  string id = 1;
}

message User {
  string id = 1;
  string name = 2;
  string email = 3;
}
```

Implement server

```ts
// user_server.ts
import * as grpc from "@grpc/grpc-js";
import * as protoLoader from "@grpc/proto-loader";

const packageDef = protoLoader.loadSync("user.proto");
const grpcObj = grpc.loadPackageDefinition(packageDef) as any;
const userService = grpcObj.userapi.UserService;

const server = new grpc.Server();

server.addService(userService.service, {
  GetUser: (call: any, callback: any) => {
    const id = call.request.id;
    callback(null, { id, name: "Alice", email: "alice@example.com" });
  },
});

server.bindAsync("0.0.0.0:50051", grpc.ServerCredentials.createInsecure(), () => {
  server.start();
  console.log("gRPC server running on port 50051");
});
```

## How to Access On Client

- Use generated client code from the same `.proto` file
- Call method like `client.GetUser({ id: 1})`

```ts
// user_client.ts
import * as grpc from "@grpc/grpc-js";
import * as protoLoader from "@grpc/proto-loader";

const packageDef = protoLoader.loadSync("user.proto");
const grpcObj = grpc.loadPackageDefinition(packageDef) as any;
const client = new grpcObj.userapi.UserService("localhost:50051", grpc.credentials.createInsecure());

client.GetUser({ id: "1" }, (err: any, response: any) => {
  if (err) console.error(err);
  else console.log(response);
});
```

## When To Use

- **Internal** microservice communication
- real-time or low-latency system
- [IoT](computer-network-general-glossary.md#iot)

