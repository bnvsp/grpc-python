"""
gRPC Client service runner
"""
import os
import sys
from enum import Enum
import re
import click

from src.stream_bi_directional.server import run_streaming_client_server
from src.stream_client.server import run_stream_client_server
from src.stream_server.server import run_streaming_server
from src.unary.server import run_unary_server
from src.config.log_config import LogMessage


class ServerId(Enum):
    """ServerIds
    Enum bindings for respective Server
    """

    UNARY = 1
    STREAM_CLIENT = 2
    STREAM_SERVER = 3
    BI_DIRECTION_STREAM = 4

class ServerModules:  # pylint: disable=too-few-public-methods
    """ServerModules _summary_

    _extended_summary_
    """

    UNARY = run_unary_server
    STREAM_CLIENT = run_stream_client_server
    STREAM_SERVER = run_streaming_server
    BI_DIRECTION_STREAM = run_streaming_client_server

@click.command()
@click.option(
    "--sid/", "-i",
    help="Select appropriate Server ID to start the server",
    default=1,
    required=True,
    type=click.INT
)

def main(sid: str) -> None:
    """
    Please select appropriate Server ID to launch: \n
    # 1 Unary Server \n
    # 2 Streaming Client Unary Server \n
    # 3 Unary Client Streaming Server \n
    # 4 Streaming Client Streaming Server (Bi-directional) \n
    """
    LogMessage.configure()
    active_server_file = ""

    try:
        server_name = ServerId(sid).name
    except ValueError as error:
        click.echo(f'====+ Exception..!! +====\n{str(error)}')
        click.echo("Aborting...")
        sys.exit(0)
    else:
        module = getattr(ServerModules, server_name, None)
        if module is not None:
            click.echo(f"Executing Server: {server_name}")
            try:
                module_dir = re.findall(r'"(.*)"', str(module.__code__))
                if module_dir:
                    module_dir = os.path.abspath(os.path.dirname(module_dir[0]))
                    active_file = f'{server_name}_active'
                    active_server_file = os.path.abspath(os.path.join(module_dir, active_file))
                    with open(active_server_file, "w+", encoding="utf-8"):
                        pass

                module()  # pylint: disable=not-callable

            except KeyboardInterrupt:
                print("Shutting down server...")
                if os.path.exists(active_server_file):
                    os.remove(active_server_file)
                sys.exit(0)
        else:
            click.echo("Server not available")
            sys.exit(0)


if __name__ == "__main__":
    main()  # pylint:disable=no-value-for-parameter
