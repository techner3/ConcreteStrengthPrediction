import os 
import pandas as pd
from src.logging import logger
from src.config import Configuration
from sklearn.preprocessing import StandardScaler
from src.utils import save_dataframe,load_csv_data,save_model


class DataTransformation:

    def __init__(self):

        self.config_obj=Configuration()
        self.dataIngestion_config=self.config_obj.get_dataIngestion_config()
        self.dataTransformation_config=self.config_obj.get_dataTransformation_config()
        self.target=self.dataIngestion_config.target
        self.scaler=StandardScaler()

    @staticmethod
    def separate_target(data: pd.DataFrame,target:str):
        
        try:
            label=data[target]
            feature=data.drop(target,axis=1)
            return feature, label

        except Exception as e:
            logger.exception(f"Separation of Target feature failed :{e}")
            raise e

    def preprocess_data(self,train_data: pd.DataFrame,test_data: pd.DataFrame):
        
        try:
            train_data=self.scaler.fit_transform(train_data)
            logger.info("Preprocesing of Train Data completed")
            test_data=self.scaler.transform(test_data)
            logger.info("Preprocesing of Test Data completed")
            return pd.DataFrame(train_data), pd.DataFrame(test_data)

        except Exception as e:
            logger.exception(f"Preprocessing of data failed :{e}")
            raise e

    def initiate_data_transformation(self):
        
        try: 
            train_data=load_csv_data(path=self.dataIngestion_config.ingestion_trainData_path)
            test_data=load_csv_data(path=self.dataIngestion_config.ingestion_testData_path)
            train_data, train_target=self.separate_target(data=train_data,target=self.target)
            logger.info("Target Feature Separated for Train Data")
            test_data, test_target=self.separate_target(data=test_data,target=self.target)
            logger.info("Target Feature Separated for Test Data")
            train_data, test_data=self.preprocess_data(train_data=train_data, test_data=test_data)
            train_data=pd.concat([train_data,train_target],axis=1)
            test_data=pd.concat([test_data,test_target],axis=1)
            save_dataframe(data=train_data,
                            path=self.dataTransformation_config.transformation_trainData_path)
            logger.info(f"Transformed Train Data saved successfully at {self.dataTransformation_config.transformation_trainData_path}")
            save_dataframe(data=test_data,
                            path=self.dataTransformation_config.transformation_testData_path)
            logger.info(f"Transformed Test Data saved successfully at {self.dataTransformation_config.transformation_trainData_path}")
            save_model(model=self.scaler,path=self.dataTransformation_config.scaler_path)
            logger.info(f"Scaler saved successfully at {self.dataTransformation_config.scaler_path}")
            

        except Exception as e:
            logger.exception(f"Data Transformation failed :{e}")
            raise e
            
