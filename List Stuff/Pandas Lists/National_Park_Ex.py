import pandas as pd

park_info = pd.read_csv("national_parks_sample.csv")

"""#Changes the value of a specific cell
park_info.at[1, "Waterfalls"] = "Yes"

#Filters out all the locations that don't have a waterfall
print(park_info.loc[park_info["Waterfalls"] == "Yes"])

#Gets the 3rd row (Doesn't use column/row names)
print(park_info.iloc[2])

#Gets the 3rd row (Can use column/row names)
print(park_info.loc[2])

#Gets the value of a specific cell
print(park_info.at[1, "Waterfalls"])"""

"""
#For each row, iterates through each column and gives the values for each individual row
for row, col in park_info.iterrows():
    print(row, col)
    print()"""
    
print(park_info.query("HighestPointFeet >= 10000 and AnnualVisitorsThousands < 601")[["Park", "HighestPointFeet", "AnnualVisitorsThousands"]])