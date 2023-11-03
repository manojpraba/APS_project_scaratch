import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        # logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        # df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        # logging.info(f"Found columns: {df.columns}")
        # if "_id" in df.columns:
        #     logging.info(f"Dropping column: _id ")
        df=pd.read_csv('C:\Ml projects\aps-fault-detection-3ed0c23237711fcb380d479a6b734af781624404\aps-fault-detection-3ed0c23237711fcb380d479a6b734af781624404\aps_failure_training_set1.csv')
        df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)
    