import os,sys
from src.logger import logging
from src.exception import CustomExpection
from src.components.data_ingestion import DataIngestion
from dataclasses import dataclass

@dataclass
class Trainer:
    data_ingestion=DataIngestion()


class TrainingPipeline:
    def __init__(self) -> None:
        self.data_ingetsion=Trainer()

    def run_pipeline(self):
        train_data_path,test_data_path=self.data_ingetsion.data_ingestion.initiate_data_ingestion()
        return train_data_path,test_data_path


if __name__=="__main__":
    obj=TrainingPipeline()
    obj.run_pipeline()