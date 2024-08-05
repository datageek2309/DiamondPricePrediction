import os,sys
from src.logger import logging
from src.exception import CustomExpection
from src.utils import load_obj
import pandas as pd
from dataclasses import dataclass
from typing import List

class PredictPipeline:

    def __init__(self) -> None:
        pass

    def predict(self,features:List[str,int,float])->None:

        try:
            # Getting the paths of objects stored
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            # Loading them
            preprocessor=load_obj(preprocessor_path)
            model=load_obj(model_path)

            #Performing the prediction
            transformed_data=preprocessor.tranform(features)
            predicted_result=model.predict(transformed_data)
            return predicted_result
        except Exception as e:
            logging.info("Error has occured while Predicting Data")
            raise CustomExpection(e,sys)
        
class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)


