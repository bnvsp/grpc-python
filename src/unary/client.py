"""
gRPC Client
"""

from src.protos import unary_pb2_grpc as pb2_grpc
from src.protos import unary_pb2 as pb2
from src.shared import ClientInfo

class UnaryClient(ClientInfo):  # pylint: disable=too-few-public-methods
    """
    Client to interact with gRPC server
    """

    def __init__(self) -> None:
        super().__init__(service_stub=pb2_grpc.UnaryStub)

def run_unary_client(test_message=None):
    """get_url Fetch response

    Args:
        message (_type_): _description_
    """
    uc_obj = UnaryClient()

    if test_message is None:
        test_message = 'Message from Client'

    message = pb2.InitiateRequest(msg=test_message)

    return uc_obj.stub.invoke_server(message)
