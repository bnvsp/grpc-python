"""
gRPC Client
"""
import sys
import grpc
from src.protos import unary_pb2_grpc as pb2_grpc
from src.protos import unary_pb2 as pb2
from src.shared import ClientInfo

class SampleClient(ClientInfo):  # pylint: disable=too-few-public-methods
    """
    Client to interact with gRPC server
    """

    def __init__(self) -> None:
        super().__init__()
        try:
            grpc.channel_ready_future(self.channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit("Trouble connecting to server... \nAborting client process..!!")
        else:
            self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """get_url Fetch response

        Args:
            message (_type_): _description_
        """

        message = pb2.InitiateRequest(msg=message)

        return self.stub.invoke_server(message)
