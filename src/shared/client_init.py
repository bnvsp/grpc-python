"""
Shared Client Atributes
"""
from grpc._channel import Channel
from src.config import (
    HOST,
    PORT
)

class ClientInfo:  # pylint: disable=too-few-public-methods
    """
    Client Attributes
    """
    def __init__(self) -> None:
        self.host: str = HOST
        self.server_port: int = PORT
        self.channel: Channel = None
        self.stub = None
