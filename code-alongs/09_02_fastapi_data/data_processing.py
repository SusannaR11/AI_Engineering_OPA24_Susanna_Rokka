import pandas as pd
from constants import DATA_PATH
from pprint import pprint
import json

df = pd.read_csv(DATA_PATH / "Europe_Bike_Sales.csv")

class DataExplorer:
    def __init__(self, limit = 100):
        self._df = df.head(limit) #private attribute in this class
        self._df_full = df

    @property
    def df(self):
        return self._df # ._df is the 'backing variable'
    
    def kpis(self, country: str):
        """filter out KPIs based on country"""
        df_by_country = self._df_full.query("Country.str.casefold() == @country.casefold()")
        return {
            "total_profit": str(df_by_country["Profit"].sum()), #numpy
            "total_cost": str(df_by_country["Cost"].sum()),
            "number_of_purchases": str(len(df_by_country))
        }

    
    def summary(self):
        self._df = (
            self._df_full.describe()
            .T.drop(["count"], axis=1)
            .drop(["Day", "Year"])
            .reset_index()) #for summary statistics. axis=1 throws columns, axis for rows. method chaining (.method().method() ... like in pandas)
        return self

    def json_response(self):
        json_data = self.df.to_json(orient="records")
        #print(type(json_data))
        return json.loads(json_data)

if __name__ == "__main__":
    data_explorer = DataExplorer()
    pprint(data_explorer.summary().json_response()) # for eda
    #pprint(data_explorer.json_response()) # returns a list of dictionaries
                                        #create instance of object, add on ._df
                                        # print(data_explorer.df)
