# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas



data = pandas.read_csv("squirrel_data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, red, black]
}
squirrel_data = pandas.DataFrame(squirrel_dict)
squirrel_data.to_csv("sq_data.csv")