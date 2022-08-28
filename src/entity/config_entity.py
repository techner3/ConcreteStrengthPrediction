from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
                                ["raw_data_path","target","ingestion_trainData_path","ingestion_testData_path"])