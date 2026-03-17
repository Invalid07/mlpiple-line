# data ingestion will bring data from define soruce  like database , mongo db and more ....

import pandas as pd 
import os 
from sklearn.model_selection import train_test_split
import logging

# storing every thing inside log 
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)    #(jis naam ka banana chahate ho )

# configure logging
logger = logging.getLogger('DataIngestion')     #('data ingestion is the name of logger ')
logger.setLevel('DEBUG')                        # settinf level for logger to debug

console_handler = logging.StreamHandler()      # console handler for logging to console
console_handler.setLevel('DEBUG')               # setting level for console handler to debug
logger.addHandler(console_handler)              # adding console handler to logger

# file_path
file_path = os.path.join(log_dir, 'data_ingestion.log')  # creating file path for log file inside log directory
file_handler = logging.FileHandler(file_path)
file_handler.setLevel('DEBUG')
logger.addHandler(file_handler)

# file formate
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

