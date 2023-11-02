import logging
import os
from datetime import datetime


# creating a log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a Log Folder
log_path = os.path.join(os.getcwd(),"logs")

#created a directory, where above files & folder will be there
os.makedirs(log_path, exist_ok=True)


#Entire log file path
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)


#creating logging configuration

logging.basicConfig(level=logging.INFO,
                    filename= LOG_FILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" 

                    )



if __name__ == '__main__':
    logging.info("Again testing")

