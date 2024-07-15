import os
import logging
from datetime import datetime
from config.config import (
    ROOT_DIR
)

def custom_logger(log_path = None):

    if not log_path:
        log_path = os.path.join(ROOT_DIR, "logs")
    date_str = datetime.now().strftime("%Y%m%d")
    logging.basicConfig(
        filename=os.path.join(log_path, f"{date_str}_logs.txt"), 
        format='%(asctime)s - %(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO)
    logger = logging.getLogger()

    return logger