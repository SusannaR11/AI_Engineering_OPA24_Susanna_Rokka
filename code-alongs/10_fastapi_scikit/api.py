from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from constants import DATA_PATH, MODELS_PATH
from pydantic import BaseModel, Field

df = pd.read_csv(DATA_PATH / "IRIS.csv")

router = APIRouter(prefix="/api/iris/v1")

app = FastAPI()

# request / response schemas
# use model_development for gt=/lt= values, maybe slightly wider range
# ie df.describe().T min and max values
class Irisinput(BaseModel):
    sepal_length: float = Field(gt=4, lt=8.5)
    sepal_width: float = Field(gt=1.8, lt=5)
    petal_length: float = Field(gt=0.8, lt=7.5)
    petal_width: float = Field(gt=0, lt=3)

class PredictionOutput(BaseModel):
    predicted_flower: str


@router.get("")
def read_data():
    return df.to_dict(orient="records") #'records' each record is in a dictionary -
#creates json array of json objects

@router.post("/predict", response_model=PredictionOutput)
def predict_flower(payload: Irisinput):
    data_to_predict = pd.DataFrame(payload.model_dump(), index=[0])
    clf = joblib.load(MODELS_PATH / "Iris_classifier.joblib")
    prediction = clf.predict(data_to_predict)
    return {"predicted_flower": prediction[0]}

# trick to check 'predict' on api: copy CURL response and paste into terminal window, it should return the prediction:
# curl -X 'POST' \
#   'http://127.0.0.1:8000/api/iris/v1/predict' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "sepal_length": 5,
#   "sepal_width": 2.8,
#   "petal_length": 1.8,
#   "petal_width": 1
# }'

# comment out comd + K + C


app.include_router(router=router)


# navigate into project root folder, then run
# uvicorn api:app --reload