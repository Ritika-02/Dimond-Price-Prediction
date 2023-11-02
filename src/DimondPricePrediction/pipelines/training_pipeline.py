from src.DimondPricePrediction.components.data_ingestion import DataIngestion


import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customException
import os
import sys


obj = DataIngestion()

obj.initiate_data_ingestion()
 