
import csv
import pandas as pd


def getsuccess(course,elorm):
    grades= pd.read_csv('grade2.csv')
    grades.sort_values("Year", inplace=True)
    
    grades = grades.drop(grades[grades.Grade == 'S'].index) 
    grades = grades.drop(grades[grades.Grade == 'U'].index) 
    grades = grades.drop(grades[grades.Grade == 'W'].index)
    
    grades['Grade'] = grades['Grade'].replace("AA",4.0)
    grades['Grade'] = grades['Grade'].replace("BA",3.5)
    grades['Grade'] = grades['Grade'].replace("BB",3.0)
    grades['Grade'] = grades['Grade'].replace("CB",2.5)
    grades['Grade'] = grades['Grade'].replace("CC",2.0)
    grades['Grade'] = grades['Grade'].replace("DC",1.5)
    grades['Grade'] = grades['Grade'].replace("DD",1.0)
    grades['Grade'] = grades['Grade'].replace("FD",0.5)
    grades['Grade'] = grades['Grade'].replace("FF",0.0)
    grades['Grade'] = grades['Grade'].replace("NA",0.0)
    grades=grades.fillna(0)
    
    grades=grades[grades.CourseCode==cName]
    grades=grades[grades.Elective==elorm]
    
    if grades.empty==True:
        return 0,0
    
    keys = grades.columns[[0, 1, 4, 7]]
    numcourses = len(grades[keys]["CourseCode"].tolist())
    ids = grades[keys]["StudID"].tolist()
    years = grades[keys]["Year"].tolist()
    letters = grades[keys]["Grade"].tolist()
    
    stat_val = {}
    for i in range(numcourses):
        year = years[i]
        stat_val[year] = [0, 0]
   
    for i in range(numcourses):
        letter = letters[i]
        year=years[i]
        stat = stat_val[year] 
        stat[0] += letter
        stat[1] += 1
        stat_val[year] = stat
        
        
        
        
 
    for key in stat_val:
        if(float(stat_val[key][1])!=0):
            stat_val[key][0] = stat_val[key][0] / stat_val[key][1]
                
            
    

    labels = []
    values=[]   
                
    for item in stat_val.values():
        values.append(float(format(round(item[0],2))))
    for key in stat_val:
        labels.append(key)   
        
    return labels,values
      





cName = "CENG"
elorm='E'
labels,values=getsuccess(cName,elorm)