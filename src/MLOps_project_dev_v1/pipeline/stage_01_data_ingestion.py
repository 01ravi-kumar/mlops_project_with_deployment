from src.MLOps_project_dev_v1.config.configuration import ConfigurationManager
from src.MLOps_project_dev_v1.components.data_ingestion import DataIngestion
from src.MLOps_project_dev_v1 import logger


stage_name = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            congif = ConfigurationManager()
            data_ingestion_config = congif.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>>>> stage: {stage_name} started <<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage: {stage_name} completed <<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e