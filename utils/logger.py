import os
import logging
from datetime import datetime

def custom_logger():
    dir_name = os.path.dirname(os.path.dirname(__file__))    # chat_interface directory
    logging.basicConfig(
        filename=os.path.join(dir_name, "logs", "logs.txt"), 
        level=logging.INFO)
    logger = logging.getLogger()

    return logger