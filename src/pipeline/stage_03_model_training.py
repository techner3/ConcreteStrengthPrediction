from src.logging import logger
from src.component import ModelTrainer

def main():
    
    try: 
        logger.info(">>>>>>>>> Model Training Stage 03 Started <<<<<<<<<")
        component_obj=ModelTrainer()
        component_obj.initiate_model_training()
        logger.info(">>>>>>>>> Model Training Stage 03 Completed <<<<<<<<<")

    except Exception as e:
        logger.exception(f"Stage 03 Model Training failed with {e}")
        raise e

if __name__ == '__main__':
    main()