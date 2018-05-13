



import csv
import pandas as pd
import numpy
path="datastudent/"
def get_leavg_success(filename):
    grades= pd.read_csv(path+filename)
    grades.sort_values("Leave", inplace=True)
    grades=grades[pd.isnull(grades['Leave']) != True]
    
    keys = grades.columns[[0, 2, 5, 6]]
    numcourses = len(grades[keys]["StudID"].tolist())
    years = grades[keys]["Leave"].tolist()
    avgs = grades[keys]["Avg"].tolist()
    #print(years)
    stat_val = {}
    for i in range(numcourses):
        year = years[i]
        stat_val[year] = [0, 0]
  
    countm=0
    countf=0
    for i in range(numcourses):
        year=years[i]
        avg = avgs[i]
        stat = stat_val[year] 
        stat[0] += avg
        stat[1] += 1
        stat_val[year] = stat 
     
        
   
        
    
    for key in stat_val:
        if(float(stat_val[key][1])!=0):
            stat_val[key][0] = stat_val[key][0] / float(stat_val[key][1])    
          
    values = []
    labels=[]   
                
    for item in stat_val.values():
        values.append(float(format(round(item[0],2))))
    for key in stat_val:
        labels.append(int(key))
    return values,labels   
      
def get_leavg_file(filename):
    if not filename:
        filename="student.csv"
        values,labels=get_leavg_success(filename)
        return values,labels
    else:
        values,labels=get_leavg_success(filename)
        return values,labels

filename=[]
values,labels=get_leavg_file(filename)

