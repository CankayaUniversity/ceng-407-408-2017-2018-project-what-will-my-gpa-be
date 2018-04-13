import csv
import pandas as pd

#Efnan Gülkanat
def get_courses(grades_filename)
	grades = pd.read_csv(filename)
	grades.sort_values("StudID", inplace = True)
	grades['CourseCode'] = grades['CourseCode'].apply(str) + grades['CourseNum'].apply(str)
	result = grades.drop(grades.columns[[2,3]], axis=1)
	vector = result.pivot_table(values = 'Grade', index = 'StudID', columns = 'CourseCode', aggfunc = 'first')
	students = pd.read_csv('student_sample.csv')
	students.sort_values("StudID", inplace=True)

