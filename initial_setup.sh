

echo "Creating project structure."
mkdir src src/component configs notebooks raw_data src/pipeline src/utils src/logger src/config 
echo "Project structure created."

echo "Started necessary files creation"
touch src/__init__.py src/component/__init__.py src/config/__init__.py configs/config.yaml configs/params.yaml src/pipeline/__init__.py src/logger/__init__.py src/config/configuration.py src/logger/get_logger.py
touch src/component/data_ingestion.py src/component/data_transformation.py src/component/model_training.py  src/component/model_evaluation.py
touch src/pipeline/stage_01_data_ingestion.py src/pipeline/stage_02_data_transformation.py src/pipeline/stage_03_model_training.py src/pipeline/stage_04_model_evaluation.py
touch src/utils/__init__.py src/utils/all_utils.py
touch setup.py
touch test.py
touch README.md
touch requirements.txt
touch .gitignore
echo "Necessary files created."

echo "Virtual environment creation started."
conda create -p venv python=3.7 -y
echo "Virtual environment created."

