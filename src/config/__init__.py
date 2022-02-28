"""
Configuration
"""
import os

HOST = "localhost"
PORT = 5000
__CURRENT_DIR = os.path.dirname(__file__)
_LOG_CONFIG_FILE = os.path.abspath(
    os.path.join(__CURRENT_DIR, "logger_config.yaml")
)
