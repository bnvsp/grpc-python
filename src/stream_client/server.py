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
