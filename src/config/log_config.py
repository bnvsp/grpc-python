"""
Configure Logging
"""
import logging
from logging import Logger
from logging.config import dictConfig
from functools import wraps
from datetime import datetime
import yaml

class LogMessage:  # pylint: disable=too-few-public-methods
    """
    Configure logging
    """

    logger:Logger

    @classmethod
    def configure(cls) -> None:
        """configure: Configure logger from YAML file

        Returns:
            Logger: logger object
        """
        from src.config import _LOG_CONFIG_FILE  # pylint: disable=import-outside-toplevel

        with open(_LOG_CONFIG_FILE, "r", encoding="utf-8") as config_file:
            configuration = yaml.safe_load(config_file.read())
            if configuration:
                dictConfig(configuration)

        cls.logger = logging.getLogger(__name__)


    @staticmethod
    def log_info(log_enable=True, log_msg: str=None, capture_time: bool=False):
        """log_decor: Decorator function for logging

        Args:
            func (obj): Function to be wrapped
        """
        def actual_decor(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                """wrapper: Execute Wrapper function

                Returns:
                    None
                """

                start_time = datetime.now()

                func(*args, **kwargs)

                end_time = datetime.now()

                if log_enable and log_msg:
                    LogMessage.log_message(
                        LogMessage.logger,
                        message=log_msg
                    )

                    if capture_time is True:
                        time_stamp_message = f'\
                        Time Taken for func {func.__name__} == {end_time-start_time}'
                        LogMessage.log_message(
                            LogMessage.logger,
                            time_stamp_message
                        )

                return func

            return wrapper

        return actual_decor


    @staticmethod
    def log_message(log_obj, message=None) -> None:
        """log_message [summary]

        [extended_summary]

        Args:
            message ([type], optional): [description]. Defaults to None.
        """

        if message:
            log_obj.info(message)
