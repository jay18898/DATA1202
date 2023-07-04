import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import BarChart, Series, Reference

pd.set_option("display.max_column",500)

file_name = "AB_NYC_2019 -ascii.csv"

raw_df = pd.read_csv(file_name)

# Average number_of_reviews per neighbourhood_group
neighbourhood_analysis  = raw_df.groupby(["neighbourhood_group"])["number_of_reviews"].mean().reset_index()


wb = Workbook()

ws1 = wb.active
ws1.column_dimensions['A'].width = 20
ws1.column_dimensions['B'].width = 20

chart1 = BarChart()
chart1.type = "col"
chart1.style = 10
chart1.title = "Neighbourhood Rating"
chart1.y_axis.title = 'Average Rating'
chart1.x_axis.title = 'Neighbourhood'

for r in dataframe_to_rows(neighbourhood_analysis, index=False, header=True):
    ws1.append(r)

last_row = len(ws1["A"])

data = Reference(ws1, min_col=2, min_row=1, max_col=2, max_row=last_row)
cats = Reference(ws1, min_col=1, min_row=2, max_col=1, max_row=last_row)

chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)

chart1.shape = 4
ws1.add_chart(chart1, "F1")

wb.save("Week9.xlsx")