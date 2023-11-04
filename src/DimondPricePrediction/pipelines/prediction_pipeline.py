import os
import sys
import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customException
from src.DimondPricePrediction.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            # Collecting the path of pkl files
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")

            # loading the data
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            # transforming the data
            scaled_data = preprocessor.transform(features)

            # getting the prediction
            pred = model.predict(scaled_data)

            # returning the prediction
            return pred



        except Exception as e:
            raise customException(e,sys)



# creating 2nd class

class CustomData:
    
    # Initializing the independent variable
    def __init__(self, carat:float, depth:float, table:float, x:float, y:float, z:float, cut:str, color:str, clarity:str ):

        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut 
        self.color = color
        self.clarity = clarity


    #  Creating a Dataframe
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat' : [self.carat],
                'depth' : [self.depth],
                'table' : [self.table],
                'x'     : [self.x],
                'y'     : [self.y],
                'z'     : [self.z],
                'cut'   : [self.cut],
                'color' : [self.color],
                'clarity' : [self.clarity]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info("DataFrame Gathered")
            return df
        
        except Exception as e:
            logging.info('Exception occured during prediction pipeline')
            raise customException(e,sys)