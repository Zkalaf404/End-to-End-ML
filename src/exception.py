import sys
import logging
import os
from datetime import datetime

# Create the log filename with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory for the logs
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.error("An error occurred: %s", str(CustomException(e, sys)))
        raise CustomException(e, sys)
