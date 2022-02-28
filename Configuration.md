# Setup & Usage Guide

- Configure virtual environment

  ```powershell
  python -m pip install --upgrade pip
  python -m venv env
  ./env/Scripts/activate
  ```

- Installing gRPC toolkit

  ```powershell
  > python -m pip install grpcio
  > python -m pip install grpcio-tools
  ```

- Create `.proto` protobuf file

  ![Protobuf sample code](res/protobuf-sample-code.png)

- Generate stubs using below command

  ```powershell
  > (env) python -m grpc_tools.protoc --proto_path=. --python_out=.\src\ --grpc_python_out=.\src\ .\protos\*.proto
  ```

- Create Server service which uses generated stubs to take request as input and returns the response.

- Create Client service which uses generated stubs to send the request and wait for the response.

- **Enable Server Reflection**:

  - Install grpcio-reflection package

  ```powershell
  (env) > python -m pip install grpcio-reflection
  ```

  - Import reflection module `from grpc_reflection.v1alpha import reflection` in server code.

  - Configure reflection service by adding the service names

  ```python
    # Server Reflection
    server_names = (
        pb2.DESCRIPTOR.services_by_name['Unary'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(server_names, server)
  ```
