import os
from pathlib import Path
from src.MLOps_project_dev_v1.config.configuration import ConfigurationManager
from src.MLOps_project_dev_v1.components.data_transformation import DataTransformation
from src.MLOps_project_dev_v1 import logger





stage_name = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"),"r") as f:
                status = f.read().split(" ")[-1]

            if status=="True":
                congif = ConfigurationManager()
                data_transformation_config = congif.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception ("Data schema is invalid.")
        except Exception as e:
            raise e
        

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
