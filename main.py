from src.MLOps_project_dev_v1 import logger
from src.MLOps_project_dev_v1.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# import os
# os.chdir("mlops_project_with_deployment/")

stage_name = "Data Ingestion Stage"


try:
    logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
