"""
gRPC Client service runner
"""

import sys

from src.stream_bi_directional.server import run_streaming_client_server
# from src.stream_client.server import run_stream_client_server
# from src.stream_server.server import run_streaming_server
# from src.unary.server import run_unary_server
from src.config.log_config import LogMessage

def main() -> None:
    """main:
    Launcher module
    """
    LogMessage.configure()
    run_streaming_client_server()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down server...")
        sys.exit(0)
