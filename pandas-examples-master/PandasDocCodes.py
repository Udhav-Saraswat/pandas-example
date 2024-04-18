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

air_quality.head()

air_quality.plot()
plt.show()


air_quality["station_paris"].plot()
plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

air_quality.plot.box()
plt.show()