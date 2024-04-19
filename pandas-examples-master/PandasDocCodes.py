import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df)

# every col is a series in a df
series = df["Age"]

print(series)


# creating series from scratch
ages = pd.Series([22, 35, 58], name="Age")

# add to all val
print(ages.add(10))

# row prefix x axis
print(ages.add_prefix("Age - "))

print(ages.describe())

# importing data from csv

titanic = pd.read_csv("data/data.csv")


# first 8 head, last 8 tail
print(titanic.head(8))


# dump df to excel, by default root path is considered
titanic.to_excel("Generated/titanic.xlsx", sheet_name="passengers", index=False)

# reading that excel now
titanic = pd.read_excel("Generated/titanic.xlsx", sheet_name="passengers")


# selection
age_sex = titanic[["Age", "Sex"]]
print(age_sex)
print(type(age_sex))
print(titanic[["Age", "Sex"]].shape)  # rows and col info

# filtering
above_35 = titanic[titanic["Age"] > 35]
print(above_35)
print(titanic["Age"] > 35)


# | or &
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23)

#
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names)


# rows 10 till 25 and columns 3 to 5.
var = titanic.iloc[9:25, 2:5]

# plotting in graph
air_quality = pd.read_csv("data/airQualityData.csv", index_col=0, parse_dates=True)
"""
air_quality.head()

air_quality.plot()
plt.show()


air_quality["station_paris"].plot()
plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

air_quality.plot.box()
plt.show()
"""

# add columns
air_quality["new_col"] = air_quality["station_london"]*1000

print(air_quality)


# rename col
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

print(air_quality_renamed)

# stats
titanic[["Age", "Fare"]].median()

titanic[["Age", "Fare"]].describe()

titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)


# group by, selection of columns (rectangular brackets [] as usual)
titanic[["Sex", "Age"]].groupby("Sex").mean()
titanic.groupby("Sex").mean(numeric_only=True)
titanic.groupby("Sex")["Age"].mean()
titanic["Pclass"].value_counts() # same to titanic.groupby("Pclass")["Pclass"].count()


# sorting
titanic.sort_values(by="Age").head()

titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()

# filter for no2 data only , long to wide format
air_quality = pd.read_csv("data/no2data.csv", index_col=0, parse_dates=True)

no2 = air_quality[air_quality["parameter"] == "no2"]

# use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)


no2_subset.pivot(columns="location", values="value")

no2.pivot(columns="location", values="value").plot()

air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
)


# Wide to long format, we add a new index to the DataFrame with reset_index()
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
no_2 = no2_pivoted.melt(id_vars="date.utc")


#
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


