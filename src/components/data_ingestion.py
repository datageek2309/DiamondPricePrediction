import os,sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomExpection
from dataclasses import dataclass
from typing import List,Tuple
from pathlib import Path


#Creating Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    
    raw_data_path:str=os.path.join("artifacts","raw_data.csv")
    train_data_path:str=os.path.join("artifacts","train_data.csv")
    test_data_path:str=os.path.join("artifacts","test_data.csv")
    file_path:str=Path(r"notebooks\data\gemstone.csv")


## Creating Data Ingestion Class
class DataIngestion:

    """This class basically reads the raw file and creats three files namely
    raw data,trian data and test data in artifacts folder"""

    def __init__(self)->None:
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self)->Tuple[str]:
        try:
            raw_data=pd.read_csv(self.ingestion_config.file_path)
            # Creating/Copying Raw data file
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            if os.path.dirname(self.ingestion_config.raw_data_path):
                raw_data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Raw data is created")
            # Splitting the data into train and test data
            X_train,X_test=train_test_split(raw_data,test_size=0.3,random_state=42)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            if os.path.dirname(self.ingestion_config.train_data_path):
                X_train.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logging.info("Train Data is created")
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            if os.path.dirname(self.ingestion_config.test_data_path):
                X_test.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Test Data is created")
            logging.info("Data Ingestion is Completed")
            return self.ingestion_config.train_data_path,self.ingestion_config.test_data_path
        except Exception as e:
            logging.info("Error occured while initiating Data Ingestion")
            raise CustomExpection(e,sys)
           
