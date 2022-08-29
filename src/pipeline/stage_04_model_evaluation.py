from src.logging import logger
from src.component import ModelEvaluator

def main():
    
    try: 
        logger.info(">>>>>>>>> Model Evaluation Stage 04 Started <<<<<<<<<")
        component_obj=ModelEvaluator()
        component_obj.initiate_model_evaluation()
        logger.info(">>>>>>>>> Model Evaluation Stage 04 Completed <<<<<<<<<")

    except Exception as e:
        logger.exception(f"Stage 04 Model Evaluation failed with {e}")
        raise e

if __name__ == '__main__':
    main()