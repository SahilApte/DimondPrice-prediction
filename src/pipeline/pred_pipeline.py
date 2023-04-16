import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object



class PredictPipeline:
    def __inti__(self):
        pass
    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path = model_path) 
            preprocessor = load_object(file_path=preprocessor_path)
            data_scale = preprocessor.transform(features)
            pred = model.predict(data_scale) 
            return pred 
        except Exception as e:
            raise CustomException(e,sys)                     
    
class CustomData:
    def __init__(self,carat:  float,cut:str, 
                    color:str, depth:float,table:float,
                    x :float,y:float,z:float,clarity:str):
        self.carat = carat
        self.table = table
        self.cut = cut
        self.color = color
        self.depth = depth
        self.x = x
        self.y = y
        self.z = z
        self.clarity = clarity
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "carat":[self.carat],
                "table":[self.table],
                "cut":[self.cut],
                "color":[self.color],
                "depth":[self.depth],
                "clarity":[self.clarity],
                "x":[self.x],
                "y":[self.y],
                "z":[self.z]
            }    
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)

 
    