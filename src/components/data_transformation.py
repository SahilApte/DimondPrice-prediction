import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.exception import CustomException
from src.logger import logging
from sklearn.base import BaseEstimator, TransformerMixin

from src.utils import save_object

class FilterData(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X[(X["depth"]<75) & (X["depth"]>45)]
        X = X[(X["table"]<80) & (X["table"]>40)]
        X = X[(X["x"]<30)]
        X = X[(X["y"]<30)]
        X = X[(X["z"]<30) & (X["z"]>2)]
        X = X.drop(X[X["x"]==0].index)
        X = X.drop(X[X["y"]==0].index)
        X = X.drop(X[X["z"]==0].index)
        
        return X

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts',"Preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    def get_data_transformer_obj(self):
        try:
            object_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
            overall_pipeline = Pipeline(
                steps = [
                    
                    ("Scalar",StandardScaler(with_mean=False, with_std=True))
                ],
                
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("encoder", OneHotEncoder()),
                    ("Scalar",StandardScaler(with_mean=False, with_std=True))
                ]
            )
            logging.info("features transormed")
            logging.info("Categorical features Encoded")
            preprocessor = ColumnTransformer(
                [
                    ("categorical",cat_pipeline, object_cols),
                    ("numerical",overall_pipeline, numerical_cols)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)  
        
        
        
    def  initiate_data_transform(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("reading data completed")
            logging.info("obtaining preprocessing obj")
            filter_obj = FilterData()
            df_filtered = filter_obj.transform(train_df)
            df_test_filtered = df_filtered = filter_obj.transform(test_df)
            logging.info("data filtered")
            preprocessing_obj = self.get_data_transformer_obj()
            target_column_name = "price"
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
            
            input_feature_train_df=df_filtered.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=df_filtered[target_column_name]

            input_feature_test_df=df_test_filtered.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=df_test_filtered[target_column_name]
            
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
            
         
        
        
        
                 