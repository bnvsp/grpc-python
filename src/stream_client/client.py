"""
gRPC Client
"""
import sys
import grpc
from src.protos import client_stream_pb2_grpc as pb2_grpc
from src.protos import client_stream_pb2 as pb2
from src.shared import ClientInfo

class StreamingClient(ClientInfo):  # pylint: disable=too-few-public-methods
    """
    Client to contrinously stream to server
    """

    def __init__(self) -> None:
        super().__init__()
        try:
            grpc.channel_ready_future(self.channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit("Trouble connecting to server... \nAborting client process..!!")
        else:
            self.stub = pb2_grpc.ClientStreamStub(self.channel)
