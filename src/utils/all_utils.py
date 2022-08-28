from datetime import datetime
import os 
import yaml


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