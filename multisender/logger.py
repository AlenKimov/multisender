from loguru import logger
from datetime import datetime
from os import makedirs
from pathlib import Path

# Настройки
from definitions import LOG_DIR


# FMT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>"


def set_up_logger():
    makedirs(LOG_DIR, exist_ok=True)
    log_file_name = f"{datetime.now().strftime('%d-%m-%Y')}.log"
    log_file_path = Path(LOG_DIR, log_file_name)
    # logger.add(log_file_path, format=FMT, level="DEBUG", rotation='1 day')
    logger.add(log_file_path, level="DEBUG", rotation='1 day')


set_up_logger()
