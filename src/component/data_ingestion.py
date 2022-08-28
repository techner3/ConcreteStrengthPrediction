import os
from src.config import Configuration
from src.logging import logger
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils import save_dataframe, load_csv_data

class DataIngestion:

    def __init__(self):

        self.config_obj=Configuration()
        self.dataIngestion_config=self.config_obj.get_dataIngestion_config()
        self.target=self.dataIngestion_config.target
    
    
    def detect_outliers_iqr(self,data)->list:

        outliers = []
        try:
            data = sorted(data)
            q1 = np.percentile(data, 25)
            q3 = np.percentile(data, 75)
            IQR = q3-q1
            lwr_bound = q1-(1.5*IQR)
            upr_bound = q3+(1.5*IQR)
            for i in data: 
                if (i<lwr_bound or i>upr_bound):
                    outliers.append(i)
            return outliers

        except Exception as e:
            logger.exception(f"IQR calculation failed :{e}")
            raise e

    def detecting_outliers(self,data)->list:
        
        outliers_column=[]
        try:
            for feature in data.columns:
                sample_outliers = self.detect_outliers_iqr(data[feature])
                if len(sample_outliers)>0:
                    logger.info(f"Number of Outliers for {feature} : {len(sample_outliers)}")
                    outliers_column.append(feature)
            return outliers_column

        except Exception as e:
            logger.exception(f"Detecting outliers failed :{e}")
            raise e
    
    def detect_and_handle_outliers(self,data)->pd.DataFrame:

        try: 
            outliers_column=self.detecting_outliers(data)

            if self.target in outliers_column:
                outliers_index=[]
                sample_outliers = self.detect_outliers_iqr(data[outliers_column[-1]])
                for outlier in sample_outliers:
                    outliers_index.append(data[data[outliers_column[-1]]==outlier].index.values[0])
                data.drop(data.index[outliers_index],axis=0,inplace=True)
                logger.info("Dependent Feature Outliers handled")
                outliers_column.remove(self.target)
            else: 
                logger.info("No Dependent Feature Outliers present")

            if len(outliers_column)!=None:
                for feature in outliers_column:
                    tenth_percentile = np.percentile(data[feature], 10)
                    ninetieth_percentile = np.percentile(data[feature], 90)
                    data.loc[data[feature]<tenth_percentile,feature]=tenth_percentile
                    data.loc[data[feature]>ninetieth_percentile,feature]=ninetieth_percentile
                logger.info("Independent Features Outliers handled")
            else:
                logger.info("No Independent features Outliers present")

            return data

        except Exception as e:
            logger.exception(f"Handling Outliers failed :{e}")
            raise e

            
    def train_test_split(self,data):

        try:
            (X_train, X_test, y_train, y_test) = train_test_split(data.drop(self.target,axis=1),
                                                              data[self.target], 
                                                              test_size=0.20,
                                                              random_state=101)
            logger.info(f"Train Test Split done successfully")
            logger.info(f"Number of training samples: {len(X_train)}")
            logger.info(f"Number of testing samples: {len(X_test)}")
            train_data=pd.concat([X_train,y_train],axis=1)
            save_dataframe(data=train_data,
                            path=self.dataIngestion_config.ingestion_trainData_path)
            logger.info(f"Train Data saved succesfully at {self.dataIngestion_config.ingestion_trainData_path}")
            test_data=pd.concat([X_test,y_test],axis=1)
            save_dataframe(data=test_data,
                           path=self.dataIngestion_config.ingestion_testData_path)
            logger.info(f"Test Data saved succesfully at {self.dataIngestion_config.ingestion_testData_path}")
            
        except Exception as e:
            logger.exception(f"Train test split failed :{e}")
            raise e

    def initiate_data_ingestion(self):

        try:
            data=load_csv_data(path=self.dataIngestion_config.raw_data_path)
            logger.info(f"Raw Data Loaded successfully from {self.dataIngestion_config.raw_data_path}")
            data=self.detect_and_handle_outliers(data=data)
            self.train_test_split(data=data)

        except Exception as e:
            logger.exception(f"Data Ingestion failed :{e}")
            raise e

    
    