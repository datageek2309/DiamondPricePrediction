import os,sys
from src.logger import logging
from src.exception import CustomExpection
import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from dataclasses import dataclass
from src.utils import save_object,model_eval
from typing import List,Tuple

@dataclass
class ModelTrainerConfig:
    
    os.makedirs(os.path.dirname(os.path.join("artifacts","model.pkl")),exist_ok=True)
    trained_model_path:str=os.path.join("artifacts","model.pkl")

class ModelTrainer:

    """This class loads the Preprocessor object and trains the data wuth different models"""

    def __init__(self) -> None:
        self.model_trainer=ModelTrainerConfig()

    def initiate_model_training(self,X_train:np.array,y_train:np.array,X_test:np.array,y_test:np.array)->None:
        try:
            models={
                "Linear":LinearRegression(),
                "Ridge":Ridge(),
                "Lasso":Lasso(),
                "ElasticNet":ElasticNet(),
                "DecisionTree":DecisionTreeRegressor(),
                # "NaiveBuyers":GaussianNB(),
                "KNearestNeighbours":KNeighborsRegressor(),
                # "RandomForest":RandomForestRegressor(),
                # "AdaBoost":AdaBoostRegressor(),
                # "GradientBoost":GradientBoostingRegressor(),
                # "SVMLinear":LinearSVC(),
            }
            
            # We train and get the best model here
            best_model_name:str=model_eval(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test,models=models)
            best_model=models[best_model_name]

            save_object(
                file_path=self.model_trainer.trained_model_path,
                obj=best_model
            )
            logging.info("Best MOdel is saved into model.pkl file")
        except Exception as e:
            logging.info("Error has occured while Model Training")
            raise CustomExpection(e,sys)