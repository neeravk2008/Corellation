import csv
import plotly.express as px
import numpy as np

# def plotgraph(path):
#     with open(path) as f:
#        df=csv.DictReader(f)
#        graph=px.scatter(df,x='Temperature',y='Ice-cream Sales')
#        graph.show()

def getdata(path):
    days=[]
    marks=[]

    with open(path) as f:
        df=csv.DictReader(f)
        for row in df:
            days.append(float(row['Days Present']))
            marks.append(float(row['Marks In Percentage']))

    return{'x':days,'y':marks}

def findcorrelation(path):
    corr=np.corrcoef(path['x'],path['y'])
    print(corr[0,1])

def setup():
    path='marks_days.csv'
    data=getdata(path)
    findcorrelation(data)

setup()