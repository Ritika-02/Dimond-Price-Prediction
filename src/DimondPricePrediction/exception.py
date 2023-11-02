import sys

#sys is the type of error details

class customException(Exception):
    def __init__(self,error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

# exc_tb (execution_traceback) : Tracing complete execution

    def __str__(self):   # str: String representation of an object
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.filename, self.line_no, str(self.error_message))
        


if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise customException(e,sys)