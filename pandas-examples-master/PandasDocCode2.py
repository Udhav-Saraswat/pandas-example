
import pandas as pd

air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv",
                              parse_dates=True)


air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]


air_quality_no2.head()

air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",
                               parse_dates=True)


air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]


#How to combine data from multiple tables

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
print(air_quality.head())