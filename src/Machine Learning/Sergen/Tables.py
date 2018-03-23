##Sergen İSPİR

import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

## Functions
def get_courseGradeTable():
    try:
        grades = pd.read_csv('grade_sample.csv') ## read csv from file
    except IOError:
        print("CSV file does not exist!")
        
    grades = grades.drop((grades[grades.Grade == 'S'] | grades[grades.Grade == 'U'] | grades[grades.Grade == 'W']).index)
    grades = grades.drop((grades[grades.CourseCode != 'CENG']).index)
    grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)
    grades = grades.drop(columns=["CourseNum"])
    table = grades.pivot_table(values='Grade', index='StudID', columns='CourseCode', aggfunc='first')
    table = table.replace([None,"AA","BA","BB","CB","CC","DC","DD","FD","FF"], [np.nan,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.5,0])

    ## Preprocessing: Convert NaN values to numeric values
    data = table.values ## convert pandas DataFrame to Numpy ndarray
    imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0) 
    imp.fit(data) 
    courseGradeData = imp.transform(data) ## data holds necesserry numpy table

    return courseGradeData

def get_dropoutTable():
    try:
        grades = pd.read_csv('grade_sample.csv') ## read csv from file
        students = pd.read_csv('student_sample.csv') 
    except IOError:
        print("CSV file does not exist!")
        
    

