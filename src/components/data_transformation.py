import os,sys
from src.logger import logging
from src.exception import CustomExpection
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer # Handle Missing values
from sklearn.preprocessing import OrdinalEncoder# Convert to Numeric Data
from sklearn.preprocessing import StandardScaler # Handling Feature scaling
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from dataclasses import dataclass
from src.utils import save_object
from typing import List,Tuple

@dataclass
class DataTransformationConfig:
    os.makedirs(os.path.dirname(os.path.join("artifacts","preprocessor.pkl")),exist_ok=True)
    preprocessor_obj_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:

    """This class is used for transforming the data created from Data Ingestion
    using Preprocessor and COlumn Tranformer"""
    
    def __init__(self) -> None:
        self.data_tranformation_config=DataTransformationConfig()

    # Creating this as static method snce we use it inside the class
    @staticmethod
    def get_data_transformation_obj()->None:
        try:
            logging.info("Data Tranforamtion object Creation initated")
            # Define Categorical and Numerical Columns
            categorical_cols=['cut', 'color', 'clarity']
            numerical_cols="carat depth table x y z".split()
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            #NumericalPipeline
            num_pipeline=Pipeline(
                steps=[
                        ('imputer',SimpleImputer(strategy='median')),
                        ('scaler',StandardScaler()),
                ]
            )
            ## Categorical Pipleine
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("ordinalencoder",OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler()),
                ]
            )
            ### Creating the preprocessor
            preprocessor=ColumnTransformer(
                [
                    ("num_pipline",num_pipeline,numerical_cols),
                    ("cat_pipeline",cat_pipeline,categorical_cols),
                ]
            )
            return preprocessor
        except Exception as e:
            logging.info("Error ocuured in Data Tranforamtion object Function")
            raise CustomExpection(e,sys)

    def initiate_data_transforamtion(self,train_data_path:str,test_data_path:str)->Tuple[str,np.array]:
        try:
            logging.info("Data Transformation has started")
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            preprocessor_obj=self.get_data_transformation_obj()
            drop_column=["price","id"]

            #Training Data
            input_feature_train_df=train_data.drop(drop_column,axis=1) # output is dataframe
            target_feature_train_df=train_data['price'] # output is series

            #Testing Data
            input_feature_test_df=test_data.drop(drop_column,axis=1) # output is dataframe
            target_feature_test_df=test_data['price'] # output is series

            # Data Tranformation
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df) # array
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df) # array
            
            # Concatinating  both dependent and independent features
            # train_arr=np.c_([input_feature_train_arr,np.array(target_feature_train_df)])
            # test_arr=np.c_([input_feature_test_arr,np.array(target_feature_test_df)])

            # Saving the preprocessor obj after tranforming the data
            save_object(
                file_path=self.data_tranformation_config.preprocessor_obj_path,
                obj=preprocessor_obj
            )

            return input_feature_train_arr,np.array(target_feature_train_df),input_feature_test_arr,np.array(target_feature_test_df)
        except Exception as e:
            logging.info("Error has occured during Data Tranformation Process")
            raise CustomExpection(e,sys)
            
