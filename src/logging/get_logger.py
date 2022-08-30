import os
import logging
import pandas as pd
from src.utils import create_directory,current_time_stamp

LOG_DIR="logs"

create_directory(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR,f"{current_time_stamp()}.log"), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

logger=logging.getLogger("ConcreteStrength")

