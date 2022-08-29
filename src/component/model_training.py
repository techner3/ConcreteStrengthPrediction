import os 
from src.logging import logger
import pycaret.regression as pyreg
from src.config import Configuration
from src.utils import save_dataframe,load_csv_data,save_model

class ModelTrainer:

    def __init__(self):

        self.config_obj=Configuration()
        self.dataTransformation_config=self.config_obj.get_dataTransformation_config()
        self.modelTrainer_config=self.config_obj.get_modelTrainer_config()
        self.modelParams_config=self.config_obj.get_modelParams_config()
        
    
    def model_trainer(self,data):
        
        try: 
            exp=pyreg.setup(data=data, 
                target = self.modelTrainer_config.target,
                fold_shuffle=self.modelParams_config.fold_shuffle,
                log_experiment = self.modelParams_config.log_experiment,
                silent = self.modelParams_config.silent,
                train_size=self.modelParams_config.train_size,
                preprocess= self.modelParams_config.preprocess)
            model=pyreg.compare_models()
            exp_results=pyreg.pull()
            tuned_model=pyreg.tune_model(model)
            finalized_model=pyreg.finalize_model(tuned_model)
            logger.info("Best model found sucessfully")
            return finalized_model, exp_results
        
        except Exception as e:
            logger.exception(f"Model Trainer failed :{e}")
            raise e

    def initiate_model_training(self):
        
        try:
            train_data=load_csv_data(path=self.dataTransformation_config.transformation_trainData_path)
            logger.info("Training Data Loaded successfully")
            trained_model, results=self.model_trainer(data=train_data)
            save_dataframe(data=results,path=self.modelTrainer_config.experimentResults_path)
            logger.info(f"Experiment results saved successfully at {self.modelTrainer_config.experimentResults_path}")
            save_model(model=trained_model, path=self.modelTrainer_config.model_path)
            logger.info(f"Best Model saved successfully at {self.modelTrainer_config.model_path}")

        except Exception as e:
            logger.exception(f"Model Trainer failed :{e}")
            raise e