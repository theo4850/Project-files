#import necessary libraries
import pandas as pd
import plotly.graph_objects as go

#load the dataset
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

#remove missing rows
df.dropna(inplace=True)

#convert data to date type and filter the data based on the timeframe 2016-2019
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
filtered_df = df[(df['year'] >= 2016) & (df['year'] <= 2019)]

#calculate the sales percentage per store for the timeframe
sales = filtered_df.groupby("store_name").agg({'sale_dollars' : 'sum'})
total_sales = filtered_df['sale_dollars'].sum()
sorted_sales = sales.sort_values(by=["sale_dollars"], ascending=False)
percentage_sorted_sales = ((sorted_sales['sale_dollars'] / total_sales) * 100).round(2).head(15).reset_index()

#print the result
print(percentage_sorted_sales)

#Create a new plotly Figure object
fig = go.Figure()

# Add a pie trace to the figure
fig.add_trace(go.Pie(
    labels=percentage_sorted_sales['store_name'],
    values=percentage_sorted_sales['sale_dollars'],
    textinfo='label+percent',
    marker=dict(
        colors=["blue", "red", "green", "yellow"],
        line=dict(color="black", width=1)
    )
))

# Update the layout of the figure
fig.update_layout(
    title='%Sales per Store',
    hovermode='x unified'
)

# Display the figure
fig.show()