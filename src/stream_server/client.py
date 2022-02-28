"""
gRPC Client
"""
import sys
import grpc
from src.protos import unary_pb2_grpc as pb2_grpc
from src.protos import unary_pb2 as pb2
from src.shared import ClientInfo

class UnaryClient(ClientInfo):
    """UnaryClient Clent stub with unary request

    Args:
        ClientInfo (_type_): _description_
    """

    def __init__(self) -> None:
        super().__init__()
        try:
            grpc.channel_ready_future(self.channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit("Trouble connecting to server... \nAborting client process..!!")
        else:
            self.stub = pb2_grpc.UnaryStub(self.channel)
