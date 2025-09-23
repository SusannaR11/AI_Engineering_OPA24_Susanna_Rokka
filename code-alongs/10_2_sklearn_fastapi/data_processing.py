import pandas as pd 
from constants import DATA_PATH
from pydantic import BaseModel, Field
import json

df = pd.read_csv(DATA_PATH / "IRIS.csv") #index_col=0)

class IrisData:
    def __init__(self):
        self.df = df # expose dataframe

    def to_json(self):
        return self.df.to_dict(orient= "records")

# request / response schemas (define datatypes for input). validation for dtype
class IrisInput(BaseModel):
    sepal_length: float = Field()
    sepal_width: float = Field()
    petal_length: float = Field()
    petal_width: float = Field()

# output:
class PredictionOutput(BaseModel):
    predicted_flower: str


if __name__ == "__main__":
    iris = IrisData()
    print(iris.to_json())