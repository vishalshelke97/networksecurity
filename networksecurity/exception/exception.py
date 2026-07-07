import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        self.error_message = error_message
        _,_,exec_tb = error_detail.exc_info()

        self.line_number = exec_tb.tb_lineno
        self.file_name = exec_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return f"Error occurred in script: [{self.file_name}] at line number: [{self.line_number}] with error message: [{self.error_message}]"
        

if __name__ == "__main__":
    try:
        logger.logging.info("This is an info message")
        a = 1/0
    except Exception as e:
        raise NetworkSecurityException("Division by zero error", sys) from e