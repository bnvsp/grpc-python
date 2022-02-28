"""
gRPC Client service runner
"""

from src.unary import client as unary_client

def main() -> None:
    """main:
    Launcher module
    """

    client_obj = unary_client.SampleClient()
    response = client_obj.get_url("Hello")
    print(response)
    client_obj.channel.close()

if __name__ == "__main__":
    main()
