"""
gRPC Client
"""

from src.protos import server_stream_pb2_grpc as pb2_grpc
from src.protos import server_stream_pb2 as pb2
from src.shared import ClientInfo

class UnaryClientWithStreamResponse(ClientInfo):  # pylint: disable=too-few-public-methods
    """UnaryClient Clent stub with unary request

    Args:
        ClientInfo (_type_): _description_
    """

    def __init__(self) -> None:
        super().__init__(service_stub=pb2_grpc.ServerStreamStub)


def run_unary_client(test_message=None):
    """get_url Fetch response

    Args:
        message (_type_): _description_
    """

    if test_message is None:
        test_message = "Hello from Client"

    uc_obj = UnaryClientWithStreamResponse()

    message = pb2.ClientRequest(req_message=test_message)

    for resp in uc_obj.stub.stream_response(message):
        yield resp
