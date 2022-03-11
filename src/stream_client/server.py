"""
gRPC Python Server
"""
# from signal import (
#     signal,
#     SIGTERM
# )

from src.protos import client_stream_pb2_grpc as pb2_grpc
from src.protos import client_stream_pb2 as pb2
from src.shared.server_init import run_server

class UnaryServer(pb2_grpc.ClientStreamServicer):  #pylint: disable=too-few-public-methods
    """UnaryServer: Unary response servicer
    """

    def __init__(self) -> None:
        pass

    def stream_request(self, request_iterator, context):
        """stream_request: Handle streaming request

        Args:
            request_iterator (_type_): _description_
            context (_type_): _description_
        """
        client_ids = []

        for each_element in request_iterator:
            client_ids.append(
                each_element.client_message.split("ID:")[1].strip()
            )

        result = {
            "response_code":1,
            "response_status":f'Client IDs: {", ".join(client_ids)}'
        }

        return pb2.UnaryResponse(**result)

def run_stream_client_server():
    """run_server Configure unary server
    """

    run_server(
        server_class=pb2_grpc.add_ClientStreamServicer_to_server,
        service_class=UnaryServer,
        buffer_descriptor=pb2.DESCRIPTOR,
        service_name='ClientStream'
    )
