import os
import sys
import logging


log_dir = "log"

log_filepath = os.path.join(log_dir,"running_logs.log")
## Creating the logs directory 
os.makedirs(log_dir,exist_ok=True)

format_msg = "[%(asctime)s - %(levelname)s - %(module)s]: %(message)s"
logging.basicConfig(level=logging.INFO,
                    format = format_msg,
                    handlers=[
                        logging.FileHandler(log_filepath),
                        logging.StreamHandler(sys.stdout)
                        ]
                    )
logger = logging.getLogger("CNNclassifier")