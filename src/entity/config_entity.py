from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
                                ["target","raw_data_path","ingestion_trainData_path","ingestion_testData_path"])

DataTransformationConfig=namedtuple("DataTransformationConfig",
                                     ["transformation_trainData_path","transformation_testData_path","scaler_path"])

ModelTrainerConfig=namedtuple("ModelTrainerConfig",["model_path","experimentResults_path","target"])

ModelParamsConfig=namedtuple("ModelParamsConfig",["fold_shuffle","train_size","log_experiment","preprocess","silent"])

ModelEvalutorConfig=namedtuple("ModelEvalutorConfig",["test_results_path"])