import os,sys
from src.logger import logging
from src.exception import CustomExpection
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from dataclasses import dataclass
from typing import List,Tuple

@dataclass
class TrainingConfig:
    data_ingestion_obj=DataIngestion()
    data_tranformation_obj=DataTransformation()
    model_trainer_obj=ModelTrainer()


class TrainingPipeline:

    """This is a pipeline which runs all the components"""

    def __init__(self) -> None:
        self.trainer=TrainingConfig()

    def run_pipeline(self)->Tuple[str]:
        try:

            train_data_path,test_data_path=self.trainer.data_ingestion_obj.initiate_data_ingestion()
            X_train,y_train,X_test,y_test=self.trainer.data_tranformation_obj.initiate_data_transforamtion(
                train_data_path=train_data_path,
                test_data_path=test_data_path
            )
            self.trainer.model_trainer_obj.initiate_model_training(X_train,y_train,X_test,y_test)
        except Exception as e:
            raise CustomExpection(e,sys)
        


if __name__=="__main__":
    obj=TrainingPipeline()
    obj.run_pipeline()