"""
gRPC Client
"""

from random import randint
from src.protos import client_stream_pb2_grpc as pb2_grpc
from src.protos import client_stream_pb2 as pb2
from src.shared import ClientInfo

class StreamingClient(ClientInfo):  # pylint: disable=too-few-public-methods
    """
    Client streaming request to server
    """

    def __init__(self) -> None:
        super().__init__(service_stub=pb2_grpc.ClientStreamStub)

def run_streaming_client():
    """run_streaming_client: Run streaming client to get a unary response
    """
    server_response = None
    stream_client_obj = StreamingClient()
    server_response = stream_client_obj.stub.stream_request(
    create_message()
    )
    return server_response

def create_message():
    """send_message Send stream of messages to server

    Args:
        client_obj (object): Client stub class
    """
    for _ in range(10):
        message_id = f'Client with message ID: {randint(0, 1000)}'
        yield pb2.ClientStreamingRequest(client_message=message_id)
