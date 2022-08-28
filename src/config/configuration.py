import os 
from src.entity import DataIngestionConfig
from src.utils import read_yaml, create_directory
from src.constant import CONFIG_PATH
class Configuration:

    def __init__(self):

        self.config=read_yaml(CONFIG_PATH)

    def get_dataIngestion_config(self):

        try:
            ingestion_dir=os.path.join(self.config["artifacts"]["dir"],
                                    self.config["artifacts"]["ingestion"])
            create_directory(ingestion_dir)
            dataIngestion_config=DataIngestionConfig(
                                raw_data_path=self.config["raw_data"],
                                target=self.config["target"],
                                ingestion_trainData_path=os.path.join(ingestion_dir,
                                                        self.config["artifacts"]["train_data"]),
                                ingestion_testData_path=os.path.join(ingestion_dir,
                                                        self.config["artifacts"]["test_data"])
            )
            return dataIngestion_config

        except Exception as e:
            raise e