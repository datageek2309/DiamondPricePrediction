import os,sys
from src.logger import logging
from src.exception import CustomExpection
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from dataclasses import dataclass
from typing import List,Tuple

@dataclass
class TrainingConfig:
    data_ingestion_obj=DataIngestion()
    data_tranformation_obj=DataTransformation()


class TrainingPipeline:

    """This is a pipeline which runs all the components"""
    
    def __init__(self) -> None:
        self.trainer=TrainingConfig()

    def run_pipeline(self)->Tuple[str]:
        train_data_path,test_data_path=self.trainer.data_ingestion_obj.initiate_data_ingestion()
        train_arr,test_arr,preprocessor_obj_path=self.trainer.data_tranformation_obj.initiate_data_transforamtion(
            train_data_path=train_data_path,
            test_data_path=test_data_path
        )
        return train_data_path,test_data_path


if __name__=="__main__":
    obj=TrainingPipeline()
    obj.run_pipeline()