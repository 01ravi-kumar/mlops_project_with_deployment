import os
import urllib.request as request
import zipfile
from src.MLOps_project_dev_v1 import logger
from src.MLOps_project_dev_v1.utils.common import get_size
from pathlib import Path
from src.MLOps_project_dev_v1.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config: DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
            
            logger.info(f"{filename} downloaded! with the following header:{headers}")
        else:
            logger.info(f"file already exist of size :{get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)


