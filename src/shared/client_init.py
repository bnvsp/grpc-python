"""
Shared Client Atributes
"""
import grpc
import sys
from grpc._channel import Channel
from src.config import (
    HOST,
    PORT
)

class ClientInfo:  # pylint: disable=too-few-public-methods
    """
    Client Attributes
    """
    def __init__(self, service_stub=None) -> None:
        self.host: str = HOST
        self.server_port: int = PORT
        self.channel: Channel = grpc.insecure_channel(f'{HOST}:{PORT}')
        if service_stub is None:
            self.stub = None
        else:
            try:
                grpc.channel_ready_future(self.channel).result(timeout=10)
            except grpc.FutureTimeoutError:
                sys.exit("Trouble connecting to server... \nAborting client process..!!")
            else:
                self.stub = service_stub(self.channel)
