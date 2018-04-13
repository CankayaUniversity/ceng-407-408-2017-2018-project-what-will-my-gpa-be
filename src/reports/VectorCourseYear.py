import csv
import pandas as pd

def course_list():
    courses=grades.CourseCode.unique()
    course_list=sorted(courses.tolist())
    return course_list

def get_course_avg(course): 
    keys = grades.columns[[0, 1, 4, 7]]
    courses = grades[keys]["CourseCode"].tolist()
    years = grades[keys]["Year"].tolist()
    letters = grades[keys]["Grade"].tolist() 

    stat_val = {}
    
    for i in range(len(years)):
        year = years[i]
        stat_val[year] = [0, 0]
   
    n_letters = len(letters)
    n_records = len(courses)
    
    for i in range(n_records):
        if (courses[i] == course):
            year = years[i]
            letter = letters[i]
            stat = stat_val[year] 
            stat[0] += letter
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
        labels.append(key)
    return values,labels       
      

dosya='grade2.csv'
grades= pd.read_csv(dosya)
grades.sort_values("StudID", inplace=True)
grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)

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

cName="CENG241"
values,labels=get_course_avg(cName)
