"""
gRPC Client service runner
"""

import os
import sys
from src.unary.client import run_unary_client
from src.stream_server.client import run_unary_client as run_streaming_server_client
from src.stream_client.client import run_streaming_client
from src.stream_bi_directional.client import run_streaming_server_client as run_bi_direct_client

class ClientMethodMap:
    """
    Map client methods to respective RPC category
    """

    UNARY = run_unary_client
    STREAM_CLIENT = run_streaming_client
    STREAM_SERVER = run_streaming_server_client
    BI_DIRECTION_STREAM = run_bi_direct_client

    IS_SERVER_STREAMING = {
        "UNARY": False,
        "STREAM_CLIENT": False,
        "STREAM_SERVER": True,
        "BI_DIRECTION_STREAM": True,
    }


def main() -> None:
    """main:
    Launcher module
    """


    client_src_path = os.path.join(os.path.dirname(__file__), "src")
    client_contents = os.listdir(client_src_path)
    skip_py_files = ["__init__.py", "__pycache__"]
    skip_contents = skip_py_files + ["config", "protos", "shared"]
    active_server = ""
    for content in client_contents:
        if content in skip_contents:
            continue
        server_client_dir = os.path.join(client_src_path, content)

        active_server = [
            each_file for each_file in os.listdir(server_client_dir) if "_active" in each_file
        ]

        if active_server:
            active_server = active_server[0].split("_active")[0]
            break

    if active_server:
        client_module = getattr(ClientMethodMap, active_server)

        if client_module:
            print("-----------"*10)
            print(f'\nFound {active_server} as active server, hence launching respective client module: {client_module.__name__} \n')
            print("-----------"*10 + "\n")
            response = client_module()

            if ClientMethodMap.IS_SERVER_STREAMING[active_server] is True:
                for resp in response:
                    print(resp)
            else:
                print(response)
    else:
        print("Cannot find any active Server\nAborting Client...")
        sys.exit(0)


if __name__ == "__main__":
    main()
