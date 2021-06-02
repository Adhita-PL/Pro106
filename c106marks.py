import csv
import numpy as np

def getDataSource(data_path) :
    size_of_tv = []
    average_time = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Marks In Percentage"]))
            average_time.append(float(row["Days Present"])) 
    return{"x" : size_of_tv, "y" : average_time}
    
def findcorrelation(data_source) :
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between the Marks In Percentage and Days Present is", correlation[0,1]) 

def main() :
    data_path = "Student Marks vs Days Present.csv" 
    data_source = getDataSource(data_path)
    findcorrelation(data_source)

main() 