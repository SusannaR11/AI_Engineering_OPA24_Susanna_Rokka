import pandas as pd
from constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "Europe_Bike_Sales.csv")

class DataExplorer:
    def __init__(self, limit = 100):
        self._df = df.head(limit) #private attribute in this class


if __name__ == "__main__":
    data_explorer = DataExplorer()

    print(data_explorer._df)
