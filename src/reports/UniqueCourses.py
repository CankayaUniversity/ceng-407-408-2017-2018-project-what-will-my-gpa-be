
# coding: utf-8

# In[1]:



import csv
import pandas as pd


path="data/"
def course_listt(filename):
    
    grades= pd.read_csv(path+filename)
    grades.sort_values("StudID", inplace=True)


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
    courses=grades.CourseCode.unique()
    course_list=sorted(courses.tolist())
    return course_list

def course_file_list(filename):
    if not filename:
        filename="grade2.csv"
        courses=course_listt(filename)
        return courses
    else:
        courses=course_listt(filename)
        return courses

filename=[]
courses=course_file_list(filename)


