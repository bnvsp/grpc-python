"""
gRPC Python Server
"""
# from signal import (
#     signal,
#     SIGTERM
# )

from src.protos import unary_pb2_grpc as pb2_grpc
from src.protos import unary_pb2 as pb2
from src.shared.server_init import run_server

class SampleService(pb2_grpc.UnaryServicer):  # pylint: disable=too-few-public-methods
    """SampleService
    """

    def __init__(self, *args, **kwargs) -> None:
        pass

    def invoke_server(self, request, _context):  # pylint: disable=no-self-use
        """invoke_server: Send single response to client's message

        Args:
            request (_type_): _description_
            _context (_type_): _description_

        Returns:
            _type_: _description_
        """

        message = request.msg
        result = f'Sample server has started and received message {message} from client'
        result = {
            "msg":result,
            "rcvd":True,
        }

        return pb2.FetchResponse(**result)

def run_unary_server() -> None:
    """run_unary_server: Run server
    """
    run_server(
        server_class=pb2_grpc.add_UnaryServicer_to_server,
        service_class=SampleService,
        buffer_descriptor=pb2.DESCRIPTOR,
        service_name='Unary'
    )
