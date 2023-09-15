import os
from src.MLOps_project_dev_v1 import logger
from src.MLOps_project_dev_v1.config.configuration import ConfigurationManager
from src.MLOps_project_dev_v1.components.data_validation import DataValidation




stage_name = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        try:
            congif = ConfigurationManager()
            data_validation_config = congif.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e