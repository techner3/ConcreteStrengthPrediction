from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
                                ["raw_data_dir","target","ingestion_trainData_path","ingestion_testData_path"])