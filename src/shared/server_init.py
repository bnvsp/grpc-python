"""
Configure common server methods
"""
from concurrent import futures
import grpc
from grpc._server import _Server
from grpc_reflection.v1alpha import reflection
from src.config import PORT

class ServerReflection:  # pylint: disable=too-few-public-methods
    """
    Configure server reflection for input service
    """

    @staticmethod
    def enable_for(service_name: str=None, pb_descriptor=None, server_obj: _Server=None):
        """configure_reflection _summary_

        _extended_summary_

        Args:
            service_name (_type_, optional): _description_. Defaults to None.
        """
        if any(not each_var for each_var in (service_name, pb_descriptor, server_obj,)):
            raise ValueError("Invalid arguments passed for Server reflection")

        server_names = (
            pb_descriptor.services_by_name[service_name].full_name,
            reflection.SERVICE_NAME
        )

        reflection.enable_server_reflection(server_names, server_obj)


def run_server(
    service_class: object=None,
    server_class: object=None,
    buffer_descriptor=None,
    service_name: str=None
):
    """run_server: Configure server and run
    """

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )
    server_class(service_class(), server)

    # Server Reflection
    ServerReflection.enable_for(
        service_name=service_name,
        pb_descriptor=buffer_descriptor,
        server_obj=server
    )

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
