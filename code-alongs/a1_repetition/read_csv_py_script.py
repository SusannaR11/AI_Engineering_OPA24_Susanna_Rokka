import pandas as pd
from pathlib import Path

DATA_PATH= Path(__file__).parents[2] /"data"

df = pd.read_csv(DATA_PATH/"Europe_Bike_Sales.csv", index_col=0, parse_dates=True)
#df.head()
print(df.head())