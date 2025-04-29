# new_list = []
# with open("/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/25-)day25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     for d in data:
#         new_list.append(d.strip())
    
# print(new_list)

# import csv

# with open("/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/25-)day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)


import pandas

# data = pandas.read_csv("/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/25-)day25/weather_data.csv")

# temp_list = data["temp"].to_list()
# avarage = sum(temp_list) / len(temp_list)
# print(avarage)
# print(data["temp"].mean())
# print(data["temp"].max())

# data["temp"] = data.temp
# print(data.temp)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/25-)day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "FurColor": ["Grey", "Black", "Red"],
    "Count": [grey_squirrels_count, black_squirrels_count, red_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)