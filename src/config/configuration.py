import os 
from src.constant import CONFIG_PATH,PARAMS_PATH
from src.utils import read_yaml, create_directory
from src.entity import DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig,ModelParamsConfig,ModelEvalutorConfig
class Configuration:

    def __init__(self):

        self.config=read_yaml(CONFIG_PATH)
        

    def get_dataIngestion_config(self)->DataIngestionConfig:

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

    def get_dataTransformation_config(self)->DataTransformationConfig:

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

    def get_modelTrainer_config(self)->ModelTrainerConfig:

        try:
            trainer_dir=os.path.join(self.config["artifacts"]["dir"],
                                        self.config["artifacts"]["trainer"])
            model_dir=self.config["model_dir"]
            create_directory(trainer_dir)
            create_directory(model_dir)
            modelTrainer_config=ModelTrainerConfig(
                                target=self.config["target"],
                                model_path=os.path.join(model_dir,
                                                        self.config["model_file"]),
                                experimentResults_path=os.path.join(trainer_dir,
                                                        self.config["artifacts"]["results"])
            )
            return modelTrainer_config

        except Exception as e:
            raise e

    def get_modelParams_config(self)->ModelParamsConfig:

        try:
            self.params=read_yaml(PARAMS_PATH)
            modelParams_config=ModelParamsConfig(
                fold_shuffle=self.params["fold_shuffle"],
                train_size=self.params["train_size"],
                log_experiment=self.params["log_experiment"],
                preprocess=self.params["preprocess"],
                silent=self.params["silent"],
            )
            return modelParams_config

        except Exception as e:
            raise e

    def get_modelEvaluator_config(self)->ModelEvalutorConfig:

        try:
            evaluator_dir=os.path.join(self.config["artifacts"]["dir"],
                                        self.config["artifacts"]["evaluator"])
            create_directory(evaluator_dir)
            modelEvalutor_config=ModelEvalutorConfig(
                        test_results_path=os.path.join(evaluator_dir,self.config["artifacts"]["result_file"]),
            )
            return modelEvalutor_config

        except Exception as e:
            raise e