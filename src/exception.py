import sys
from src.logger import logging

def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):

    def __init__(self, error_msge: object , error_dtls:sys):
        super().__init__(error_msge)
        self.error_message = error_message_details(error_msge,error_details=error_dtls)

    def __str__(self) -> str:
        return self.error_message