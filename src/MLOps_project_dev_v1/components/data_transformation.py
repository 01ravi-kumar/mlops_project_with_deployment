import os
from src.MLOps_project_dev_v1.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from src.MLOps_project_dev_v1 import logger 
import pandas as pd


class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config 

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
