"""
gRPC Python Server
"""
# from signal import (
#     signal,
#     SIGTERM
# )

from src.protos import bi_directional_stream_pb2_grpc as pb2_grpc
from src.protos import bi_directional_stream_pb2 as pb2
from src.shared.server_init import run_server


class StreamingServerToStreamingClient(pb2_grpc.BiDirectionalStreamServicer):
    """StreamingServerToStreamingClient Send streaming response to streaming client request

    Args:
        pb2_grpc (_type_): _description_
    """

    def __init__(self) -> None:
        pass

    def bi_direction_stream(self, request_iterator, context):
        """bi_direction_stream

        Args:
            request_iterator (_type_): _description_
            context (_type_): _description_
        """

        for message in request_iterator:
            serv_msg = f'Server responded to {message}'

            response_msg = {
                "response_code": 200,
                "response_message": serv_msg
            }

            yield pb2.ServerResponse(**response_msg)


def run_streaming_client_server():
    """run_server Configure unary server
    """

    run_server(
        server_class=pb2_grpc.add_BiDirectionalStreamServicer_to_server,
        service_class=StreamingServerToStreamingClient,
        buffer_descriptor=pb2.DESCRIPTOR,
        service_name='BiDirectionalStream'
    )
