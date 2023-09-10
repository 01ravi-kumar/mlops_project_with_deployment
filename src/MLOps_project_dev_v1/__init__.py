import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

dir = "mlops_project_with_deployment"
log_dir = "logs"
log_path = os.path.join(dir,log_dir)
log_filepath = os.path.join(log_path,"running_logs.log")
os.makedirs(log_path,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger("MLOps_project_dev_v1_logger")