import pandas


data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

#Creating data dictionary with all squirrels counted
data_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirell_count.csv")
print(df)
