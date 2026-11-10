import pandas as pd

"""
student_info = {
    "name": "Zendaya",
    "year": "Freshman",
    "age": 30,
    "graduated": False,
    "fav_class": "IS 303"
}

print(student_info)

df = pd.DataFrame([student_info])
print(df)
"""

# Creates things with 1 collumn
"""
words = ["Bread", "Butter", "Robert", "Larping", "Inquisitive"]

result = pd.DataFrame(words)

print(result)
"""

# Creates things with multiple collumns
"""
words = [["Bread", "Jam"], ["Butter", "Toast"], ["Robert", "Roberta"], ["Larping", "Parling"], ["Inquisitive", "Quisitive"]]

result = pd.DataFrame(words)

print(result)
"""

# Creating Dictionary
"""
student_info = {
    "Name": ["Tom", "LeBron", "George", "LaFawnda"],
    "GPA": [2.7, 4.0, 1.1, 4.5]
    
}

result = pd.DataFrame(student_info)

print(result)
"""

# Gets info from excell and can do stuff using the data
resturaunt_info = pd.read_csv("RestaurantInfo.csv")

print(resturaunt_info)

print(resturaunt_info.at[1,"FoodType"])
resturaunt_info.at[1, "FoodType"] = "ReallyFakeMex"
print(resturaunt_info.at[1, "FoodType"])

print(resturaunt_info.query("Rating >= 10"))