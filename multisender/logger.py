from loguru import logger
from datetime import datetime
from os import makedirs
import sys
from pathlib import Path

from definitions import LOG_DIR


FMT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>"


def set_up_logger():
    logger.remove()
    makedirs(LOG_DIR, exist_ok=True)
    log_file_name = f"{datetime.now().strftime('%d-%m-%Y')}.log"
    log_file_path = Path(LOG_DIR, log_file_name)
    logger.add(log_file_path, format=FMT, level="DEBUG", rotation='1 day')
    logger.add(sys.stderr, colorize=True, format=FMT, level="DEBUG")


set_up_logger()
