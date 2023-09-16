from src.MLOps_project_dev_v1 import logger
from src.MLOps_project_dev_v1.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MLOps_project_dev_v1.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MLOps_project_dev_v1.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.MLOps_project_dev_v1.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

stage_name = "Data Ingestion Stage"


try:
    logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Data Validation Stage"


try:
    logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Data Transformation Stage"


try:
    logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Model Trainer Stage"


try:
    logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e