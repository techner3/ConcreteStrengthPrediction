import os 
from src.constant import CONFIG_PATH
from src.utils import read_yaml, create_directory
from src.entity import DataIngestionConfig,DataTransformationConfig
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

    def get_dataTransformation_config(self):

        try:
            transformation_dir=os.path.join(self.config["artifacts"]["dir"],
                                    self.config["artifacts"]["transformation"])
            model_dir=self.config["model_dir"]
            create_directory(transformation_dir)
            create_directory(model_dir)
            dataTransformation_config=DataTransformationConfig(
                                transformation_trainData_path=os.path.join(transformation_dir,
                                                        self.config["artifacts"]["transformation_train"]),
                                transformation_testData_path=os.path.join(transformation_dir,
                                                        self.config["artifacts"]["transformation_test"]),
                                scaler_path=os.path.join(model_dir,self.config["scaler_file"])
            )
            return dataTransformation_config

        except Exception as e:
            raise e