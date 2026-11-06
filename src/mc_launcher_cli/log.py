"""Logging utils"""

import logging
import logging.handlers
from datetime import datetime as DateTime

from mc_launcher_cli.context import PROJECT_DATA


__all__ = [
    "get_logger"
]


datefmt="%Y-%m-%d %H:%M:%S"
fmt_map = {
    "single_thread": "%(asctime)s - %(levelname)s - %(message)s",
    "multi_thread": "%(asctime)s - [%(threadName)s] - %(levelname)s - %(message)s"
}


def get_logger(
        name: str,
        console: bool = True,
        file: bool = True,
        multi_thread: bool = False
):
    """
    Args:
        console:
            output to console.
            输出到控制台
        file:
            output to file.
            输出到文件
    """
    
    if multi_thread:
        formatter = logging.Formatter(
            datefmt=datefmt,
            fmt=fmt_map.get("multi_thread")
        )
    else:
        formatter = logging.Formatter(
            datefmt=datefmt,
            fmt=fmt_map.get("single_thread")
        )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    if file:
        log_file = PROJECT_DATA.LOGS / f"{name}_{DateTime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log"
        file_handler = logging.handlers.RotatingFileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
