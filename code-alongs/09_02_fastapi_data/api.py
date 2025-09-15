from fastapi import FastAPI, Query
from data_processing import DataExplorer
from constants import DATA_PATH

data_explorer = DataExplorer() # instantiate object class DataExplorer

app = FastAPI()

@app.get("/api/sales")
async def read_sales(): #limit: int = Query(100, gt=0, lt=150000)):
    ##implement this code to return json data in this end point
    #data = DataExplorer(app.state.df, limit)
    return data_explorer.json_response()

@app.get("/api/summary")
async def read_summary_data():
    return data_explorer.json_response()
    #data = DataExplorer(app.state.df)
#    return data_explorer.summary().json_response()
 #   """shows summary statistics"""
 #   return data.json_response()


# to run API:
# uvicorn api:app --reload
# navigate to /docs for swagger ui

