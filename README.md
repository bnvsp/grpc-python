# API Timeline

![API Timeline](res/API-Timeline.png)

## How RPC works

![RPC Workflow](res/RPC-Flow.png)

1. Client initiates the request.
2. The request along with metadata will be packed by the client stub.
3. RPC buffer code will serialize the client request to server.
4. The server RPC will receive the binary.
5. TODO
6. TODO

## gRPC

- General purpose RPC (Remote Procedure Call) an open-source API framework developed by Google.

- Transport layer of gRPC is HTTP and implemented in HTTP/2 version.

- Protocol buffer is being used as default Interface Descriptive Language.
  - Schema is defined in `.proto` file, schema determines how data is being structured.
  - `protoc` is used to generate stubs (data access classes) for selected programming language by providing respective `.proto` file as input.
  - At runtime, messages are compressed and serialized in binary format.

- A Client-Response model that supports Data Streaming with Event Driven Architecture.
  - Uniary streaming. (Single Request-Single Response)
  - Server-side streaming.
  - Client-side streaming.
  - Bi-directional streaming

- Efficient Parsing: Since messages are transferred in binary format which reduces size of encoded message making it less CPU-intensive for pasring. This results in faster exchange of messages even with slower CPU devices.

- Essential Schema: By enforsing to adhere strict schema, this ensures data structure intact so that protobufs can concentrate more on serialization/deserialization.

## Advantages of using Protobuf

Please refer [Statistics](Statistics.md) for more details

## Configuring Python environment

Please refer [Configuration](Configuration.md) to setup `Python` environment and configure gRPC service
