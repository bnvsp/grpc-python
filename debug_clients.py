"""
gRPC Client service runner
"""

# from src.unary import client as unary_client
# from src.stream_server import client as stream_server_client
from src.stream_client import client as stream_client
# from src.stream_bi_directional import client as stream_client_server

def main() -> None:
    """main:
    Launcher module
    """

    # # Unary client for Unary Server
    # response = unary_client.run_unary_client(test_message="Message from unary client")
    # print(response)

    # # Unary client for Streaming Server
    # for resp in stream_server_client.run_unary_client(
    #     test_message="Hello from Client1"
    # ):
    #     print(resp)

    # Streaming client with Unary response Server
    server_response = stream_client.run_streaming_client()
    print("Server response: ", server_response)

    # # Streaming client with streaming server
    # for server_response in stream_client_server.run_streaming_server_client():
    #     print(server_response)

if __name__ == "__main__":
    main()
