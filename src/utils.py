import os,sys
import pickle
from src.exception import CustomExpection
from src.logger import logging
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import numpy as np

def save_object(file_path:str,obj:object)->None:
    try:
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj=obj,file=file_obj)
    except Exception as e:
        raise CustomExpection(e,sys)
    
def load_obj(file_path:str)->object:
    try:
        with open(file_path,"rb") as file:
            preprocessor=pickle.load(file)
        return preprocessor
    except Exception as e:
        raise CustomExpection(e,sys)
    

def model_eval(X_train:np.array,y_train:np.array,X_test:np.array,y_test:np.array,models:dict[str,object])->str:

    "This function performs model traig and give the best model"
    model_report=dict()
    try:
        for model_name,model_obj in models.items():
            #Train Model
            model_obj.fit(X_train,y_train)

            #Predict Testing Data
            y_test_predict=model_obj.predict(X_test)

            # Get R2 scores for train and test data
            test_model_score=r2_score(y_pred=y_test_predict,y_true=y_test)
            model_report[model_name]=test_model_score
        else:
            # Finding the Best Model
            best_model = max(model_report,key=model_report.get)
            logging.info(f"Best Model found ---- {best_model} with Accuracy {model_report[best_model]}")
        
        return best_model

    except Exception as e:
        logging.info("Error occured while performing Model Evaluation")
        raise CustomExpection(e,sys)