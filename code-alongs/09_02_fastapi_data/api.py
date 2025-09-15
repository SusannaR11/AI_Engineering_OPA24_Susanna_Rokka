from fastapi import FastAPI, Query, APIRouter
from data_processing import DataExplorer
from constants import DATA_PATH

data_explorer = DataExplorer() # instantiate object class DataExplorer

app = FastAPI()
router = APIRouter(prefix="/api/sales")

@router.get("")
async def read_sales(): #limit: int = Query(100, gt=0, lt=150000)):
    ##implement this code to return json data in this end point
    #data = DataExplorer(app.state.df, limit)
    return data_explorer.json_response()

@router.get("/summary")
async def read_summary_data():
    return data_explorer.summary().json_response()
    #data = DataExplorer(app.state.df)
#    return data_explorer.summary().json_response()
 #   """shows summary statistics"""
 #   return data.json_response()

@router.get("/kpis")
async def red_kpis_by_country(country: str):
    """KPI based on country"""
    return data_explorer.kpis(country=country)

# to run API:
# uvicorn api:app --reload
# navigate to /docs for swagger ui

# chart.js for visualising in javascript

app.include_router(router)