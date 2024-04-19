
import pandas as pd
import pd as pd
from matplotlib import pyplot as plt

air_quality_no2 = pd.read_csv("pandas_lib_code_dump/doc/data/air_quality_no2_long.csv",
                              parse_dates=True)


air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]


air_quality_no2.head()

air_quality_pm25 = pd.read_csv("pandas_lib_code_dump/doc/data/air_quality_pm25_long.csv",
                               parse_dates=True)


air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]


#How to combine data from multiple tables

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
print(air_quality.head())

air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])
print(air_quality_)

stations_coord = pd.read_csv("pandas_lib_code_dump/doc/data/air_quality_stations.csv")
stations_coord.head()

# like left outer join, similar to database-style operations
"""
Multiple tables can be concatenated both column-wise and row-wise using the concat function.

For database-like merging/joining of tables, use the merge function.
"""
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")

print(air_quality.head())


# handle date time
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

air_quality = air_quality.rename(columns={"date.utc": "datetime"})

print(air_quality.head())

air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

print(air_quality["datetime"])

air_quality["datetime"].min(), air_quality["datetime"].max()

air_quality["datetime"].max() - air_quality["datetime"].min()

air_quality["month"] = air_quality["datetime"].dt.month


air_quality.groupby(
    [air_quality["datetime"].dt.weekday, "location"])["value"].mean()

fig, axs = plt.subplots(figsize=(12, 4))

air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(
    kind='bar', rot=0, ax=axs)

plt.xlabel("Hour of the day")  # custom x label using Matplotlib

plt.ylabel("$NO_2 (µg/m^3)$")


# textual data manipulate

titanic = pd.read_csv("data/titanic.csv")

titanic["Name"].str.lower()

titanic["Name"].str.split(",")

titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)

titanic["Name"].str.contains("Countess")

titanic[titanic["Name"].str.contains("Countess")]

titanic["Name"].str.len()

titanic["Name"].str.len().idxmax()

titanic.loc[titanic["Name"].str.len().idxmax(), "Name"]

titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})



