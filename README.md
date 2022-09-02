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



* data_given - This directory contains the data that has been given for both training as well as predicting 
* data - This directory contains good and bad data after validation of files with respect to everything in schema for training and prediction
* frontend - This directory contains files related to frontend of the web app
* logs - This directories contains logs file that has been generated during both training and prediction
* mlruns - This directory contains all the logs from the experimentation of finding the best model
* notebooks - This directory contains notebooks used for EDA and testing purposes
* savedModels - This directory contains all the saved models for each cluster and also clustering and scaling models
* savedModel - This directory contains plots geenrated udring training
* schema - This directaory contains schema as JSon file used for data validation 
* src - This directory contains the source code for this project
* test_dir - This directory contains data used for tesing the web app

# Preview of the Web App

WebApp : [Link](https://concretestrength33.herokuapp.com/)

Home page :




# Points to Note : 

* The app may take while to load ,Please bear with it 
* Please refer to the documentation for more detailed understanding 
