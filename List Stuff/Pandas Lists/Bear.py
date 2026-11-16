import pandas as pd

park_info = pd.read_csv("national_parks_sample.csv")
"""
#Can return multiple records based on arguments
parkloc = park_info.loc[(park_info["Region"] == "Southeast") & 
(park_info["CampingAvailable"] == "Yes")],
["Park", "StateOrStates", "AnnualVisitorsThousands", "TrailMiles"]
"""
#Can return records based on index
#parkiloc = park_info.iloc[4]

# parkloc = park_info.query("Park == 'Everglades'")[["Park", "Region", "TrailMiles"]]



print(parkloc)