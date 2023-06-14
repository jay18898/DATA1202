import pandas as pd

pd.set_option('display.max_columns', 50)

FILE_PATH = '/workspaces/DATA1202/AB_NYC_2019 -ascii.csv' # CHANGE FILE HERE


#   EXTRACT -- LOAD
#   Load into a data frame
raw_df = pd.read_csv(FILE_PATH)

#   Check for errors, check data quality
#   Fill NA of reviews_per_month with -1
raw_df['reviews_per_month'] = raw_df['reviews_per_month'].fillna(-1);

#   FIll NA of last_review with '1900-01-01'
raw_df['last_review'] = raw_df['last_review'].fillna('1900-01-01');
print(raw_df.info())

# Change data type of last_review to date !!!!!
# pd.to_datetime(raw_df['last_review'], format='%y-%m-%d')

#   Transform into insights
#   Filters
#   FIlter dataset for manhatten
"""
SELECT * FROM airbnb

WHERE neighbourhood_group = 'Manhattan'
"""
brooklyn_df = raw_df[raw_df['neighbourhood_group'] == 'Brooklyn']
high_value_brooklyn = brooklyn_df[brooklyn_df['price'] > 150]

#   CASE statement
#   if price between 0  -   100 "cheap"
#   if price between 100  -   150 "moderate"
#   if price between 150  -   200 "average"
#   if price between 200+  "expensive"

raw_df.loc[(raw_df['price'] <= 100), "price_group"] = "cheap"
raw_df.loc[(raw_df['price'] >= 200), "price_group"] = "expensive"

#   Drop/add columns
#   Remove column "host_name"

selected_cols = raw_df[['host_name', 'price_group', 'neighbourhood_group','room_type','price']]

#   Perform joins
#   Aggregates  = Group By
#   Whats the average price by room type by neighbourhood
print(selected_cols.groupby(['neighbourhood_group', 'room_type'])['price'].mean().reset_index())

#   LOAD
#   Write the data to a table, or a view.
