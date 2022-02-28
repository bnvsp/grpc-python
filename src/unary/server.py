"""
gRPC Python Server
"""
# from signal import (
#     signal,
#     SIGTERM
# )
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import grpc
from src.protos import unary_pb2_grpc as pb2_grpc
from src.protos import unary_pb2 as pb2
from src.config import PORT
# from src.config.log_config import LogMessage

class SampleService(pb2_grpc.UnaryServicer):  # pylint: disable=too-few-public-methods
    """SampleService
    """

    def __init__(self, *args, **kwargs) -> None:
        pass

    # @LogMessage.log_info(log_msg="Invoked Server", capture_time=True)
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


def run_server():
    """run_server: Configure server and run
    """

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )
    pb2_grpc.add_UnaryServicer_to_server(SampleService(), server)

    # Server Reflection
    server_names = (
        pb2.DESCRIPTOR.services_by_name['Unary'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(server_names, server)
    port_info = f'[::]:{PORT}'

    server.add_insecure_port(port_info)
    server.start()


    # def handle_sigterm(*_):
    #     """Handle_sigterm: Signal Handler to stop the service
    #     with the help of external resource such as Kubernetes
    #     """
    #     print("Received Shutdown signal")
    #     rpc_event = server.stop(30) # Returns active rpc events
    #     rpc_event.wait(30)
    #     print("Shutdown complete")

    # signal(SIGTERM, handle_sigterm())

    server.wait_for_termination()
