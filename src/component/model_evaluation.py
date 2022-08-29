import os 
import numpy as np
from src.logging import logger
from src.config import Configuration
from src.component import DataTransformation
from sklearn.metrics import r2_score,mean_squared_error
from src.utils import load_csv_data, create_directory,save_json,load_model

class ModelEvaluator:

    def __init__(self):

        self.config_obj=Configuration()
        self.dataTransformation_config=self.config_obj.get_dataTransformation_config()
        self.modelTrainer_config=self.config_obj.get_modelTrainer_config()
        self.modelEvaluator_config=self.config_obj.get_modelEvaluator_config()

    def model_predictor(self,data,model):
        
        try:
            predictions=model.predict(data)
            return predictions

        except Exception as e:
            logger.exception(f"Model Predictor failed :{e}")
            raise e

    def model_evaluator(self,actual_values, predictions):
        
        result_dict=dict()
        try:
            result_dict["r2_score"]=r2_score(actual_values, predictions)
            result_dict["rmse"]=np.sqrt(mean_squared_error(actual_values, predictions))
            return result_dict

        except Exception as e:
            logger.exception(f"Model Evaluator failed :{e}")
            raise e

    def initiate_model_evaluation(self):
        
        try:
            test_data=load_csv_data(self.dataTransformation_config.transformation_testData_path)
            logger.info("Test Data loaded successfully")
            test_feature, label=DataTransformation.separate_target(data=test_data,target=self.modelTrainer_config.target)
            logger.info("Test feature and Target separated successfully")
            model=load_model(path=self.modelTrainer_config.model_path)
            predictions=self.model_predictor(data=test_feature,model=model)
            logger.info("Predictions Done")
            result=self.model_evaluator(actual_values=label,predictions=predictions)
            logger.info("Metrics calculated")
            save_json(data=result,path=self.modelEvaluator_config.test_results_path)
            logger.info(f"Test Results Saved at {self.modelEvaluator_config.test_results_path}")

        except Exception as e:
            logger.exception(f"Model Evaluation failed :{e}")
            raise e