from numpy.lib import corrcoef
import pandas as pd
import plotly_express as px
import csv
import numpy as np


#with open("cups of coffee vs hours of sleep.csv", newline='') as f :
#df = pd.read_csv("cups of coffee vs hours of sleep.csv") 
#fig = px.scatter(df, x="Coffee in ml", y="sleep in hours") 
#ig.show() 

def getDataSource(data_path) :
    coffee = []
    sleep = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x" : coffee, "y" : sleep}

def findCorrelation(dataSource) :
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correltion between coffee and sleep is " , correlation[0,1])

def main() :
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

main() 
