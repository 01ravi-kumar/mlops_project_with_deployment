from src.MLOps_project_dev_v1 import logger

from src.MLOps_project_dev_v1.components.model_evaluation import ModelEvaluation
from src.MLOps_project_dev_v1.config.configuration import ConfigurationManager


stage_name = "Model Evalutaion Stage"

class ModelEvalutaionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config= ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e
        

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
        obj = ModelEvalutaionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
