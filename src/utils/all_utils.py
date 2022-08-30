import os 
import yaml
import joblib
import json
import pandas as pd
from datetime import datetime

def create_directory(name):

    try:
        os.makedirs(name, exist_ok=True)

    except Exception as e:
        raise e

def current_time_stamp()->str:

    try:
        return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

    except Exception as e:
        raise e

def read_yaml(config_path)-> dict:

    try:
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
        return config

    except Exception as e:
        raise e

def load_csv_data(path)->pd.DataFrame:

        try:
            data=pd.read_csv(path)
            return data

        except Exception as e:
            raise e

def save_dataframe(data,path):

    try:
        data.to_csv(path,index=False)

    except Exception as e:
        raise e

def save_model(model,path):
    
    try:
        joblib.dump(model,path)

    except Exception as e:
        raise e

def save_json(data,path):

    try: 
        with open(path, 'w', encoding ='utf8') as json_file:
            json.dump(data, json_file)

    except Exception as e:
        raise e

def load_model(path):

    try:
        model=joblib.load(path)
        return model
    
    except Exception as e:
        raise e

def get_log_dataframe(file_path):

    try:
        data={
        "Message":[]
        }
        with open(file_path) as log_file:
            for line in log_file.readlines():
                data["Message"].append(line)
        log_df = pd.DataFrame.from_dict(data)
        return log_df
    
    except Exception as e:
        raise e