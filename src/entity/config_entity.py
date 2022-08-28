from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
                                ["target","raw_data_path","ingestion_trainData_path","ingestion_testData_path"])

DataTransformationConfig=namedtuple("DataTransformationConfig",
                                     ["transformation_trainData_path","transformation_testData_path","scaler_path"])