
#Efnan Gülkanat
import csv
import pandas as pd
import numpy
path="datastudent/"
def get_sex_success(filename):
    grades = pd.read_csv(path+filename)
    grades.sort_values("Graduate", inplace=True)
    grades=grades[pd.isnull(grades['Graduate']) != True]

    keys = grades.columns[[0, 3, 5, 6]]
    numcourses = len(grades[keys]["StudID"].tolist())
    years = grades[keys]["Graduate"].tolist()
    avgs = grades[keys]["Avg"].tolist()
    sex = grades[keys]["Sex"].tolist()
    #print(years)
    stat_val = {}
    for i in range(numcourses):
        year = years[i]
        stat_val[year] = [0, 0]
   
    countm=0
    countf=0
    for i in range(numcourses):
        year=years[i]
        cins=sex[i] 
        avg = avgs[i]
        if(cins=='M'):
            stat = stat_val[year] 
            stat[1] += avg
            stat_val[year] = stat 
            countm+=1
        else:
            stat = stat_val[year] 
            stat[0] += avg
            stat_val[year] = stat
            countf+=1
        

    
    
    for key in stat_val:
         if(countm!=0 and countf!=0):
            stat_val[key][1] = stat_val[key][1] / countm
            stat_val[key][0] = stat_val[key][0] / countf
  

    valuesf = []
    valuesm = []
    labels=[]   
                
    for item in stat_val.values():
        valuesm.append(float(format(round(item[0],2))))
    for key in stat_val:
        labels.append(int(key))
        stat = stat_val[key] 
        valuesf.append(float(format(round(stat[1],2))))
        
          
    return valuesm,valuesf,labels 
      




def get_sex_file(filename):
    if not filename:
        filename="student.csv"
        valuesm,valuesf,labels=get_sex_success(filename)
        return valuesm,valuesf,labels
    else:
        valuesm,valuesf,labels=get_sex_success(filename)
        return valuesm,valuesf,labels

filename=[]
valuesm,valuesf,labels=get_sex_file(filename)

