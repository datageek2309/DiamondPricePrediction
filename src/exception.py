import sys,os
from src.logger import logging




class CustomExpection(Exception):

    def __init__(self,error_message:str,error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message=self.error_message_detail(error=error_message,error_detail=error_detail)
    
    @staticmethod
    def error_message_detail(error:str,error_detail:sys)->str:
        try:
            _,_,exc_tb=error_detail.exc_info()
            file_name=exc_tb.tb_frame.f_code.co_filename
            error_message=f"Error occured in python script name - {file_name} line number - {exc_tb.tb_lineno} error message -- {error}"
            return error_message
        except Exception as e:
            logging.info(f"Error occured while creating Custom Exception Class - {e}")

    def __str__(self) -> str:
        return self.error_message
