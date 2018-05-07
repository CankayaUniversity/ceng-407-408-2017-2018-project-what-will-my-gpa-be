import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

class Tables:
    def __init__(self):
        self.dropoutTable = None
        self.dropoutLabel = None
        self.dropout_imp = None
        self.courseTable = None
        self.course_imp = None
        self.graduationTable = None
        self.graduationLabel = None
        self.graduation_imp = None
        self.studyTable = None
        self.studyLabel = None
        self.study_imp = None
        self.courseList = None
    
    def convert_nan_to_numeric(self, data):
        data = data.values ## convert pandas DataFrame to Numpy ndarray
        imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0) 
        imp.fit(data) 
        data = imp.transform(data) ## data holds necesserry numpy table
        return data, imp

    def read_data(self, grade_file, student_file):
        ## read csv files
        try:
            grades = pd.read_csv("grade/" + grade_file) 
            students = pd.read_csv("student/" + student_file)
        except IOError:
            print("CSV file does not exist!")
            return
        
        ## Preprocessing: Clean and modify tables
        grades = grades.drop((grades[grades.Grade == 'S'] | grades[grades.Grade == 'U'] | grades[grades.Grade == 'W']).index) ##remove rows that has Grade value = S, U or W
        t=grades.copy()
        grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)
        grades = grades.drop(columns=["CourseNum"])
        students = students.replace([None],[0])

        ## create a new table that includes courses and course grades
        table = grades.pivot_table(values='Grade', index='StudID', columns='CourseCode', aggfunc='first')
        table = table.replace([None,"AA","BA","BB","CB","CC","DC","DD","FD","FF"], [np.nan,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.5,0])
        self.courseList = list(table.columns.values) ##get course name list
        self.courseList = [x.lower() for x in self.courseList]

        ## required table: Dropout prediction
        self.dropoutTable = table.copy()
        self.dropoutTable['gpa'] = students['Avg'].values
        self.dropoutLabel = students["Leave"].values
        np.place(self.dropoutLabel,self.dropoutLabel!=0,[1])
        self.dropoutTable, self.dropout_imp = self.convert_nan_to_numeric(self.dropoutTable)

        ## required table: Course grade prediction
        self.courseTable, self.course_imp = self.convert_nan_to_numeric(table.copy())

        ## required table: length study prediction
        self.studyTable = table.copy()
        self.studyTable['gpa'] = students['Avg'].values
        self.studyTable, self.study_imp = self.convert_nan_to_numeric(self.studyTable)

        self.studyLabel = students['Graduate'] - students['Entry']
        self.studyLabel = self.studyLabel.values
        indx=[0,1]
        for j in range(self.studyLabel.shape[0]):
                if self.studyLabel[j]<=0:
                        indx = np.append(indx,j)
        indx = indx[::-1]
        for j in range(len(indx)):
            self.studyTable = np.delete(self.studyTable,indx[j],axis=0)
            self.studyLabel = np.delete(self.studyLabel,indx[j])

        ## required table: gpa prediction
        self.graduationTable = table.copy()
        self.graduationTable, self.graduation_imp = self.convert_nan_to_numeric(self.graduationTable)
        self.graduationLabel = students['Avg']
        

#### Preprocessing: Convert NaN values to numeric values
##def convert_nan_to_numeric(data):
##    data = data.values ## convert pandas DataFrame to Numpy ndarray
##    imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0) 
##    imp.fit(data) 
##    data = imp.transform(data) ## data holds necesserry numpy table
##    return data, imp
##

##def read_data(grade_file, student_file):
##    ## read csv files
##    try:
##        grades = pd.read_csv(grade_file) 
##        students = pd.read_csv(student_file)
##    except IOError:
##        print("CSV file does not exist!")
##        return
##
##
##    ## Preprocessing: Clean and modify tables
##    grades = grades.drop((grades[grades.Grade == 'S'] | grades[grades.Grade == 'U'] | grades[grades.Grade == 'W']).index) ##remove rows that has Grade value = S, U or W
##    t=grades.copy()
##    grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)
##    grades = grades.drop(columns=["CourseNum"])
##    students = students.replace([None],[0])
##
##    ## create a new table that includes courses and course grades
##    table = grades.pivot_table(values='Grade', index='StudID', columns='CourseCode', aggfunc='first')
##    table = table.replace([None,"AA","BA","BB","CB","CC","DC","DD","FD","FF"], [np.nan,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.5,0])
##    courseList = list(table.columns.values) ##get course name list
##    courseList = [x.lower() for x in courseList]

##    ## REQUIRED table: Course Grade prediction
##    courseTable, course_imp = convert_nan_to_numeric(table.copy())
##
##    ## REQUIRED table: Dropout prediction
##    dropoutTable = table.copy()
##    dropoutTable['gpa'] = students['Avg'].values
##    dropoutLabel = students["Leave"].values
##    np.place(dropoutLabel,dropoutLabel!=0,[1])
##    dropoutTable, dropout_imp = convert_nan_to_numeric(dropoutTable)
##
##    ## REQUIRED table: GPA prediction
##    graduationTable = table.copy()
##    graduationTable, graduation_imp = convert_nan_to_numeric(graduationTable)
##    graduationLabel = students['Avg']
##
##    ## REQUIRED table: Length of study prediction
##    studyTable = table.copy()
##    studyTable['gpa'] = students['Avg'].values
##    studyTable, study_imp = convert_nan_to_numeric(studyTable)
##
##    studyLabel = students['Graduate'] - students['Entry']
##    studyLabel = studyLabel.values
##    indx=[0,1]
##    for j in range(studyLabel.shape[0]):
##            if studyLabel[j]<=0:
##                    indx = np.append(indx,j)
##    indx = indx[::-1]
##    for j in range(len(indx)):
##        studyTable = np.delete(studyTable,indx[j],axis=0)
##        studyLabel = np.delete(studyLabel,indx[j])
