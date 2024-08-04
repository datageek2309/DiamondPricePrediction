import os,sys
import pickle
from src.exception import CustomExpection
from src.logger import logging

def save_object(file_path:str,obj:object)->None:
    try:
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj=obj,file=file_obj)
    except Exception as e:
        raise CustomExpection(e,sys)
    
def load_preprocessor_obj(file_path:str)->object:
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"rb") as file:
            preprocessor=pickle.load(file)
        return preprocessor
    except Exception as e:
        raise CustomExpection(e,sys)