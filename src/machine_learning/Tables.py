import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

## Preprocessing: Convert NaN values to numeric values
def convert_nan_to_numeric(data):
    data = data.values ## convert pandas DataFrame to Numpy ndarray
    imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0) 
    imp.fit(data) 
    data = imp.transform(data) ## data holds necesserry numpy table
    return data

## read csv files
try:
    grades = pd.read_csv('grade_sample.csv') 
    students = pd.read_csv('student_sample.csv') 
except IOError:
    print("CSV file does not exist!")

## Preprocessing: Clean and modify tables
grades = grades.drop((grades[grades.Grade == 'S'] | grades[grades.Grade == 'U'] | grades[grades.Grade == 'W']).index) ##remove rows that has Grade value = S, U or W
grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)
grades = grades.drop(columns=["CourseNum"])
students = students.replace([None],[0])

## create a new table that includes courses and course grades
table = grades.pivot_table(values='Grade', index='StudID', columns='CourseCode', aggfunc='first')
table = table.replace([None,"AA","BA","BB","CB","CC","DC","DD","FD","FF"], [np.nan,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.5,0])
courseList = list(table.columns.values) ##get course name list
##np_table = convert_nan_to_numeric(table)

## REQUIRED table: Course Grade prediction
courseTable = convert_nan_to_numeric(table)

## REQUIRED table: Dropout prediction
dropoutTable = table.copy()
dropoutTable['gpa'] = students['Avg'].values
dropoutTable['Dropout'] = students["Leave"].values
dropoutTable = convert_nan_to_numeric(dropoutTable)
np.place(dropoutTable[:,-1],dropoutTable[:,-1]!=0,[1])

## REQUIRED table: GPA prediction
##gpaTable = table.copy()
##gpaTable['gpa'] = students['Avg'].values
##gpaTable = convert_nan_to_numeric(gpaTable)

## REQUIRED table: Length of study prediction


##############

## data preparation
c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
x = courseTable[:]
course_name = 'ceng241'
course_list = [i.lower() for i in courseList]
class_index = course_list.index('ceng241')
y = x[:,class_index] ## class label
x = np.delete(x,class_index,1) ## remove class column from input data

## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
for i in range(y.size):
        index = c.index(y[i])
        y[i] = index



