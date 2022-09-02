# Concrete Strength Prediction

![my badge](https://img.shields.io/badge/Python-3-blue)
![my badge](https://img.shields.io/badge/Machine-Learning-brightgreen)
![my badge](https://img.shields.io/badge/Flask-App-green)
![my badge](https://img.shields.io/badge/Py-Caret-yellowgreen)
![my badge](https://img.shields.io/badge/AI-OPS-orange)
![my badge](https://img.shields.io/badge/-Heroku-purple)
![my badge](https://img.shields.io/badge/-GIT-green)
![my badge](https://img.shields.io/badge/-DVC-darkblue)

# About The Project

The project has been developed to predict the strength of concrete based on a amount of various things added to make concrete such as cement, water, fly ash, coarse aggregate, fine aggregate, superplasticizer, blast furnace and its age.

# Project Description 

Initally, the raw data has been analysed to understand the data and the data has been pre processed by checking null values, checking duplicates etc... The processed data is then scaled and then passed it for model training. The best model si fine tuned and is used for the prediction. A web app has been developed for this project which takes a CSV file as an input and returns the predictions as a result. The app is deployed in Heroku.

# Dataset Used

This dataset is part of the Kaggle and more information about the dataset can be found below.

Dataset : [Link](https://www.kaggle.com/datasets/elikplim/concrete-compressive-strength-data-set)

# Project Structure

<img width="146" alt="image" src="https://user-images.githubusercontent.com/58848985/188082159-4d6c7ad1-d8e5-4d61-99c0-0cec3dcdda0f.png">

* .dvc - This directory contains file related to dvc
* .github - This directory contains files related github actions and workflows
* Documents - This directory contains all the documents such HLD, LLD etc.. related to this project
* artifacts - This directories contains all the artifacts with respect to each stage in the training pipeline
* configs - This directory contains config.yaml and params.yaml necessary for training pipeline
* logs - The directory contains logs of the each stage
* notebooks - This directory contains notebooks used for EDA 
* prediction_service - This directory contains all the saved models, the files necessary for the frontend for the webapp and also predictor script

# Preview of the Web App

WebApp : [Link](https://concretestrength33.herokuapp.com/)

Home page :

<img width="958" alt="image" src="https://user-images.githubusercontent.com/58848985/188081955-72f12fd4-9d36-4f8c-a19f-e52f0d7db732.png">

Docker:

The webapp also been dockerized.You can use the below comman to pull the docker image with respect to this project.

```docker pull techner3/concretestrength```

# Points to Note : 

* The app may take while to load ,Please bear with it 
* Please refer to the documentation for more detailed understanding 
