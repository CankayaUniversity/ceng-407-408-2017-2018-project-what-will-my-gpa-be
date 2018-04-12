
import csv
import pandas as pd


def get_semester_success(studID,course): 
    dosya='grade2.csv'
    grades= pd.read_csv(dosya)
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

    grades=grades[grades.StudID==studID]
    
    if grades.empty==True:
        return 0,0
    
    
    keys = grades.columns[[0, 1, 4, 5, 7]]
    numcour = len(grades[keys]["StudID"].tolist())
    courses = grades[keys]["CourseCode"].tolist()
    semester = grades[keys]["Semester"].tolist()
    years = grades[keys]["Year"].tolist()
    letters = grades[keys]["Grade"].tolist() 


    stat_val = {}
    for i in range(numcour):
        semesters = semester[i]
        stat_val[semesters] = [0, 0]
    for i in range(numcour):
        if (courses[i] == course):
            letter = letters[i]
            semes=semester[i]
            stat = stat_val[semes] 
            stat[0] += letter
            stat[1] += 1
            stat_val[semes] = stat 
    
     
    
    for key in stat_val:
        if(float(stat_val[key][1])!=0):
            stat_val[key][0] = stat_val[key][0] / float(stat_val[key][1])
            
            
            
   
    semesters1 = []
    values1=[]
                
    for item in stat_val.values():
        values1.append(float(format(round(item[0],2))))
    for key in stat_val:
        semesters1.append(key)   
        
    return semesters1,values1
      

def get_semester_ıd(studID): 
    dosya='grade2.csv'
    grades= pd.read_csv(dosya)
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

    grades=grades[grades.StudID==studID]
    
    if grades.empty==True:
        return 0,0
    
   
    keys = grades.columns[[0, 1, 4, 5, 7]]
    numcour = len(grades[keys]["StudID"].tolist())
    courses = grades[keys]["CourseCode"].tolist()
    semester = grades[keys]["Semester"].tolist()
    years = grades[keys]["Year"].tolist()
    letters = grades[keys]["Grade"].tolist() 


    stat_val = {}
    for i in range(numcour):
        semesters = semester[i]
        stat_val[semesters] = [0, 0]
    for i in range(numcour):
        letter = letters[i]
        semes=semester[i]
        stat = stat_val[semes] 
        stat[0] += letter
        stat[1] += 1
        stat_val[semes] = stat 
    
     
    
    for key in stat_val:
        if(float(stat_val[key][1])!=0):
            stat_val[key][0] = stat_val[key][0] / float(stat_val[key][1])
            
            
            
   
    semesters = []
    values=[]   
                
    for item in stat_val.values():
        values.append(float(format(round(item[0],2))))
    for key in stat_val:
        semesters.append(key)   
        
    return semesters,values
      


studID=219
course='CENG'
semesters,values=get_semester_success(studID,course)
semestersıd,valuesıd=get_semester_ıd(studID)
