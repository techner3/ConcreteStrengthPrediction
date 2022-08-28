from src.logging import logger
from src.component import DataIngestion

def main():
    
    try: 
        logger.info(">>>>>>>>> Data Ingestion Stage 01 Started <<<<<<<<<")
        component_obj=DataIngestion()
        component_obj.initiate_data_ingestion()
        logger.info(">>>>>>>>> Data Ingestion Stage 01 Completed <<<<<<<<<")

    except Exception as e:
        logger.exception(f"Stage 01 Data Ingestion failed with {e}")
        raise e

if __name__ == '__main__':
    main()