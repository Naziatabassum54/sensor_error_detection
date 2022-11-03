import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME


#defining the constant values for the training pipeline
TARGET_COLUMN = "class"
PIPELINE_NAME:str = "sensor"
ARTIFACT_DIR:str = "artifact"
FILE_NAME:str = "sensor.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

PREPROCESS_FILE_NAME:str = "preprocessing.pkl"
MODEL_FILE_NAME:str = "model.pkl"
SCHEMA_FILE_PATH:str = os.path.join("config","schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"


#Data Ingestion related constant starts with DATA_INGESTION VAR NAME

DATA_INGESTION_COLLECTON_NAME :str="sensor"
DATA_INGESTION_DIR_NAME :str= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2