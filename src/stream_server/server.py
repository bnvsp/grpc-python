"""
gRPC Python Server
"""
# from signal import (
#     signal,
#     SIGTERM
# )

from src.protos import server_stream_pb2_grpc as pb2_grpc
from src.protos import server_stream_pb2 as pb2
from src.shared.server_init import run_server


class StreamServer(pb2_grpc.ServerStreamServicer):  #pylint: disable=too-few-public-methods
    """StreamServer: Streaming server
    """

    def __init__(self) -> None:
        pass

    def stream_response(self, request, context):
        """stream_response: Send streaming response

        Args:
            request (_type_): _description_
            context (_type_): _description_
        """

        count = 0
        while True:
            server_message = f'Id: {count} :: {request.req_message}'
            count += 1
            response = {
                "status_code":200,
                "response_message":server_message
            }
            if count >= 10:
                break
            yield pb2.ServerStreamResponse(**response)


def run_streaming_server() -> None:
    """run_streaming_server: Run streaming server
    """
    run_server(
        server_class=pb2_grpc.add_ServerStreamServicer_to_server,
        service_class=StreamServer,
        buffer_descriptor=pb2.DESCRIPTOR,
        service_name='ServerStream'
    )
