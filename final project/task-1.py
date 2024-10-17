#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
url = "https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv"
df = pd.read_csv(url)

#check for missing data
print("Missing Data:\n", df.isna().sum())

#remove rows with missing values
df.dropna(inplace=True)

#group by zip code and item number and calculate total sales
popular_item = df.groupby(["zip_code", "item_number"]).agg({"bottles_sold": 'sum'}).reset_index()

#sort by zip code and bottles sold
new_popular_item = popular_item.sort_values(['zip_code', 'bottles_sold'])

#remove duplicate values from zip code column
new_popular_item = new_popular_item.drop_duplicates('zip_code')

#show the table with the results
print(new_popular_item)

#plot the requested graph
plt.figure(figsize=(12, 10))
plt.scatter(new_popular_item["zip_code"], new_popular_item["bottles_sold"], c='red')

#bottom limit for annotation
num = 200

#annotation
for i, item_num in enumerate(popular_item["item_number"]):
    if popular_item["bottles_sold"][i] > num:
        plt.annotate(item_num, (popular_item["zip_code"][i], popular_item["bottles_sold"][i]))

#style the plot
plt.title("Bottles Sold per Zip code")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.ylim(top=1600)
plt.yticks(range(0, 1601, 200))

#show the plot
plt.show()