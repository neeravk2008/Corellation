import csv
import plotly.express as px

with open('coffee_sleep.csv') as f:
    df=csv.DictReader(f)
    graph=px.scatter(df,x='Coffee in ml',y='sleep in hours')
    graph.show()