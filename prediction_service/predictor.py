import os
import pandas as pd
from src.utils import load_model
class ConcreteData:

    def __init__(self,
                 cement: float,
                 blast_furnace_slag: float,
                 fly_ash: float,
                 water: float,
                 superplasticizer: float,
                 coarse_aggregate: float,
                 fine_aggregate: float,
                 age: int):

        try:
            self.cement = cement
            self.blast_furnace_slag = blast_furnace_slag
            self.fly_ash = fly_ash
            self.water = water
            self.superplasticizer = superplasticizer
            self.coarse_aggregate = coarse_aggregate
            self.fine_aggregate = fine_aggregate
            self.age = age

        except Exception as e:
            raise  e

    def get_concrete_data_as_dict(self):

        try:
            input_data = {
                "cement": [self.cement],
                "blast_furnace_slag": [self.blast_furnace_slag],
                "fly_ash": [self.fly_ash],
                "water": [self.water],
                "superplasticizer": [self.superplasticizer],
                "coarse_aggregate": [self.coarse_aggregate],
                "fine_aggregate": [self.fine_aggregate],
                "age": [self.age]}
            return input_data

        except Exception as e:
            raise e

    def get_concrete_input_data_frame(self):

        try:
            housing_input_dict = self.get_concrete_data_as_dict()
            return pd.DataFrame(housing_input_dict)

        except Exception as e:
            raise e


class ConcreteStrengthPredictor:

    def __init__(self):

        try:
            self.model_path = "prediction_service/models/model.pkl"
            self.scalar_path= "prediction_service/models/scaler.pkl"

        except Exception as e:
            raise e

    def predict(self, X):

        try:
            scalar = load_model(path=self.scalar_path)
            model = load_model(path=self.model_path)
            X=pd.DataFrame(scalar.transform(X))
            result = model.predict(X)
            return result

        except Exception as e:
            raise e