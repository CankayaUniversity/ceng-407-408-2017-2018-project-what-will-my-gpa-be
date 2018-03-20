##
## Efnan GÜLKANAT, Sergen İSPİR

import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

grades= pd.read_csv('grade_sample.csv') ## read csv from file
grades = grades.drop(grades[grades.Grade == 'S'].index) ##Remove vektor where grade is S
grades = grades.drop(grades[grades.Grade == 'U'].index) ##Remove vektor where grade is U
grades = grades.drop(grades[grades.Grade == 'W'].index) ##Remove vektor where grade is W
grades.sort_values("StudID", inplace=True)
grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)
result=grades.drop(grades.columns[[2,3]], axis=1)
vector=result.pivot_table(values='Grade', index='StudID', columns='CourseCode', aggfunc='first')

students=pd.read_csv('student_sample.csv')
students.sort_values("StudID", inplace=True)

vector['GPA']=students['Avg'].values ## add graduation GPA column

row,column=vector.shape
for i in range(row):
    for j in range(column):
        if vector.iloc[i,j]=="AA":
            vector.iloc[i,j]=4.0
        if vector.iloc[i,j]=="BA":
            vector.iloc[i,j]=3.5
        if vector.iloc[i,j]=="BB":
            vector.iloc[i,j]=3.0
        if vector.iloc[i,j]=="CB":
            vector.iloc[i,j]=2.5
        if vector.iloc[i,j]=="CC":
            vector.iloc[i,j]=2.0
        if vector.iloc[i,j]=="DC":
            vector.iloc[i,j]=1.5
        if vector.iloc[i,j]=="DD":
            vector.iloc[i,j]=1.0
        if vector.iloc[i,j]=="FD":
            vector.iloc[i,j]=0.5
        if vector.iloc[i,j]=="FF":
            vector.iloc[i,j]=0
        if vector.iloc[i,j] is None:
            vector.iloc[i,j]=np.nan

## Preprocessing
data = vector.values ## convert pandas DataFrame to Numpy ndarray
imp = Imputer(missing_values='NaN', strategy='median', axis=0) 
imp.fit(data) 
data = imp.transform(data) ## data holds necesserry data table
