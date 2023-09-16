import os
from src.MLOps_project_dev_v1 import logger
from src.MLOps_project_dev_v1.components.model_trainer import ModelTrainer
from src.MLOps_project_dev_v1.config.configuration import ConfigurationManager


stage_name = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config= ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e