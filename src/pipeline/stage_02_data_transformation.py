from src.logging import logger
from src.component import DataTransformation

def main():
    
    try: 
        logger.info(">>>>>>>>> Data Transformation Stage 02 Started <<<<<<<<<")
        component_obj=DataTransformation()
        component_obj.initiate_data_transformation()
        logger.info(">>>>>>>>> Data Transformation Stage 02 Completed <<<<<<<<<")

    except Exception as e:
        logger.exception(f"Stage 02 Data Transformation failed with {e}")
        raise e

if __name__ == '__main__':
    main()