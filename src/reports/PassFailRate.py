
#Efnan Gülkanat
import csv
import pandas as pd
path = "data/"

def get_pass_val(course,filename):
    grades = pd.read_csv(path+filename)
    grades.sort_values("StudID", inplace=True)
    grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)
    grades = grades.drop(grades[grades.Grade == 'S'].index) 
    grades = grades.drop(grades[grades.Grade == 'U'].index) 
    grades = grades.drop(grades[grades.Grade == 'W'].index)
    keys = grades.columns[[0, 1, 4, 7]]
    courses = grades[keys]["CourseCode"].tolist()
    letters = grades[keys]["Grade"].tolist()
    years = grades[keys]["Year"].tolist()
     
    letters_list = set(["FF", "NA","FD"])
    
    years_set = set(years)
    years_list = list(years_set)
    stat_val = dict()
    for i in range(len(years_list)):
        year = years_list[i]
        stat_val[year] = [0, 0]
    
    n_records = len(courses)
    for i in range(n_records):
        if (courses[i] == course):
            year = years[i]
            letter = letters[i]
            if letter in letters_list:
                stat = stat_val[year] 
                stat[1] += 1
                stat_val[year] = stat 
            else:
                stat = stat_val[year] 
                stat[0] += 1
                
       
    valueskalankısı = []
    valuesgecenkısı = []
    labels=[]   
                
    for item in stat_val.values():
        valuesgecenkısı.append(item[0])
    for key in stat_val:
        labels.append(key)
        stat = stat_val[key] 
        valueskalankısı.append(stat[1])
        
          
    return valueskalankısı,valuesgecenkısı,labels   
         



def get_pass_file(course,filename):
    if not filename:
        filename="grade2.csv"
        valueskalankısı,valuesgecenkısı,labels=get_pass_val(course,filename)
        return valueskalankısı,valuesgecenkısı,labels
    else:
        valueskalankısı,valuesgecenkısı,labels=get_pass_val(course,filename)
        return valueskalankısı,valuesgecenkısı,labels

course='CENG241'
filename=[]
valueskalankısı,valuesgecenkısı,labels=get_pass_file(course,filename)
