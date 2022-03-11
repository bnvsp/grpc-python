"""
gRPC Client
"""
from random import randint
from src.protos import bi_directional_stream_pb2_grpc as pb2_grpc
from src.protos import bi_directional_stream_pb2 as pb2
from src.shared import ClientInfo

class StreamingClientToStreamingServer(ClientInfo):  # pylint: disable=too-few-public-methods
    """
    Client to contrinously stream to server
    """

    def __init__(self) -> None:
        super().__init__(service_stub=pb2_grpc.BiDirectionalStreamStub)

def run_streaming_server_client():
    """run_streaming_server_client
    """
    stream_client_obj = StreamingClientToStreamingServer()

    for response in stream_client_obj.stub.bi_direction_stream(
    create_message()
    ):
        yield response

def create_message():
    """send_message Send stream of messages to server

    Args:
        client_obj (object): Client stub class
    """
    for _ in range(10):
        message = f'Client with message ID: {randint(0, 1000)}'
        yield pb2.ClientRequest(request_message=message)
