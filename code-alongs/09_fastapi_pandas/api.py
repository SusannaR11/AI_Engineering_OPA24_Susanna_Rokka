from fastapi import FastAPI, Query, APIRouter
from contextlib import asynccontextmanager # in order to load data only once
import pandas as pd
from constants import DATA_PATH
from data_processing import DataExplorer


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.df = pd.read_csv(DATA_PATH / "Europe_Bike_Sales.csv", index_col=0, parse_dates=True)
    yield
    del app.state.df

app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix= "/api/sales") #simplify code/look in swagger

@router.get("/summary")
async def read_summary_data():
    data= DataExplorer(app.state.df)
    #print(data)
    return data.summary().json_response()

@router.get("/kpis")
async def read_kpis(country: str = Query(None)):
    data = DataExplorer(app.state.df)
    return data.kpis(country)

@router.get("")
async def read_sales(limit: int = Query(100, gt=0, lt=150000)):
    data = DataExplorer(app.state.df, limit)
    return data.json_response()

app.include_router(router)


# localhost /docs to see Swagger interface and interactive 
# interface to test and document api
























# uv pip install ipykernel fastapi uvicorn