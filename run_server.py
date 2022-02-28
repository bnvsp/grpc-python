"""
gRPC Client service runner
"""

import sys
from src.unary import server as unary_server
from src.config.log_config import LogMessage

def main() -> None:
    """main:
    Launcher module
    """
    LogMessage.configure()
    unary_server.run_server()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down server...")
        sys.exit(0)
