from datetime import datetime
import os 


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
