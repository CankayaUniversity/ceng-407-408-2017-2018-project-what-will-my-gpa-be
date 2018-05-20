from sklearn.externals import joblib
from Tables import *
import MySQLdb, ML
import pandas as pd
import numpy as np


class AppController:
    def __init__(self):

        self.courses={}

        ## get number of models form database for save more model
        db = MySQLdb.connect("localhost","root","1234","ceng408" )
        cursor = db.cursor()
        query = "SELECT * from models"
        cursor.execute(query)
        self.total_rows = cursor.rowcount
        
        q_dropout = "SELECT path \
                    FROM models \
                    WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","dropout",1)
        q_study_length = "SELECT path \
                        FROM models \
                        WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","study_length",1)
        q_course = "SELECT path,course \
                    FROM models \
                    WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","course_grade",1)
        q_gpa =     "SELECT path\
                    FROM models \
                    WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","gpa",1)
        
        if self.total_rows > 3:
            ## load default models
            try:
                cursor.execute(q_dropout)
                path = cursor.fetchone()
                self.dropout = joblib.load(path[0])
            except IOError as e:
                print("Model file doesn't exist.")
            try:
                cursor.execute(q_study_length)
                path = cursor.fetchone()
                self.study_length = joblib.load(path[0])
            except IOError as e:
                print("Model file doesn't exist.")
            try:
                cursor.execute(q_gpa)
                path = cursor.fetchone()
                self.gpa = joblib.load(path[0])
            except IOError as e:
                print("Model file doesn't exist.")
            try:
                cursor.execute(q_course)
                paths = cursor.fetchall()
                for path in paths:
                    self.courses[path[1]] = joblib.load(path[0])
            except IOError as e:
                print("Model file doesn't exist.")
 

        db.close()

    def update_default_models(self):
        ## get number of models form database for save more model
        db = MySQLdb.connect("localhost","root","1234","ceng408" )
        cursor = db.cursor()
        query = "SELECT * from models"
        cursor.execute(query)
        self.total_rows = cursor.rowcount
        
        q_dropout = "SELECT path \
                    FROM models \
                    WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","dropout",1)
        q_study_length = "SELECT path \
                        FROM models \
                        WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","study_length",1)
        q_course = "SELECT path,course \
                    FROM models \
                    WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","course_grade",1)
        q_gpa = "SELECT path \
                    FROM models \
                    WHERE gradeFile='%s' AND studentFile='%s' AND function='%s' AND isDefault='%d'" % ("default_grade.csv","default_student.csv","gpa",1)

        if self.total_rows != 0:
            ## load default models
            try:
                cursor.execute(q_dropout)
                path = cursor.fetchone()
                self.dropout = joblib.load(path[0])

                cursor.execute(q_study_length)
                path = cursor.fetchone()
                self.study_length = joblib.load(path[0])

                cursor.execute(q_gpa)
                path = cursor.fetchone()
                self.gpa = joblib.load(path[0])

                cursor.execute(q_course)
                paths = cursor.fetchall()
                for path in paths:
                    self.courses[path[1]] = joblib.load(path[0])

            except IOError as e:
                print("One of the model file doesn't exist.")

        db.close()


    ## convert course grades to numeric ones(eg. AA=4, CB = 2.5)
    def courses_to_numeric(self,arr,reverse):
        numeric = [0,0.5,1,1.5,2,2.5,3,3.5,4]
        score   = ["FF","FD","DD","DC","CC","CB","BB","BA","AA"]
        if reverse:
            for i in range(len(arr)):
                        index = score.index(arr[i])
                        arr[i] = numeric[index]
        else:
            for i in range(len(arr)):
                        index = numeric.index(arr[i])
                        arr = np.append(arr,score[index])
                        arr = np.delete(arr,i)
        return arr

    ## prediction functions
    def predict_course_grade(self,vector,course_list,pcourse_name):
        model = joblib.load("models/course_"+pcourse_name+"_model")
        vector=self.courses_to_numeric(vector,True) ##convert course grades to numeric ones(eg. AA=4, CB = 2.5)
        lst = np.empty(courseTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = course_imp.transform(lst)

        class_index = courseList.index(pcourse_name)
        lst = np.delete(lst,class_index,1) ## remove class column from input data
        result = model.predict(lst)
        result = self.courses_to_numeric(result,False)
        return result[0]

    def predict_dropout(self,vector,course_list):
        vector=self.courses_to_numeric(vector,True)
        lst = np.empty(dropoutTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = dropout_imp.transform(lst)
        result = self.dropout.predict(lst)
        if result[0] == 1: return True
        else:   return False

    def predict_gpa(self,vector,course_list,semester):
        vector=self.courses_to_numeric(vector,True)
        lst = np.empty(graduationTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = graduation_imp.transform(lst)
        
        if semester=='0':
            return self.gpa[0].predict(vector)
        elif semester=='1':
            return self.gpa[1].predict(vector)
        elif semester=='2':
            return self.gpa[2].predict(vector)
        elif semester=='3':
            return self.gpa[3].predict(vector)
        elif semester=='4':
            return self.gpa[4].predict(vector)
        elif semester=='5':
            return self.gpa[5].predict(vector)
        elif semester=='6':
            return self.gpa[6].predict(vector)
        elif semester=='graduation':
            result = self.graduation.predict(lst)
            if result<0: result=result*-1
            return "%.2f"%result
         
    def predict_length(self,vector,course_list):
        tb = Tables()
        tb.read_data("default_grade.csv", "default_student.csv")
        vector=self.courses_to_numeric(vector,True)
        lst = np.empty(tb.studyTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[tb.courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = tb.study_imp.transform(lst)
        result = self.study_length.predict(lst)
        return np.round(result[0])


    ## create new models
    def create_new_model(self, grade_file, student_file, predict_function, algorithm_name, parameters, course_name, semester):

        tb = Tables()
        tb.read_data(grade_file, student_file)
        
        if predict_function=='gpa':
             if algorithm_name=='linear':
                 return ML.linear_regression(tb.graduationTable, tb.graduationLabel, parameters)
            
        elif predict_function=='dropout':            
            if algorithm_name=='logistic':
                return ML.logistic_regression(tb.dropoutTable, tb.dropoutLabel, parameters)
            elif algorithm_name=='svm':
                return ML.svm(tb.dropoutTable, tb.dropoutLabel, parameters)
            elif algorithm_name=='mlp':
                return ML.mlp(tb.dropoutTable, tb.dropoutLabel, parameters)

        elif predict_function=='course_grade':
            ##get required table without target label
            c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
            x = tb.courseTable.copy()
            class_index = tb.courseList.index(course_name.lower())
            y = x[:,class_index] ## class label
            x = np.delete(x,class_index,1) ## remove class column from input data
            ## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
            for i in range(y.size):
                    index = c.index(y[i])
                    y[i] = index
            
            if algorithm_name=='logistic':
                return ML.logistic_regression(x,y,parameters)
            elif algorithm_name=='svm':
                return ML.svm(x,y,parameters)
            elif algorithm_name=='mlp':
                return ML.mlp(x,y,parameters)

        elif predict_function=='study_length':
            if algorithm_name=='linear':
                return ML.linear_regression(tb.studyTable, tb.studyLabel, parameters)
            elif algorithm_name=='mlp_regressor':
                return ML.mlp_regressor(tb.studyTable, tb.studyLabel, parameters)

    ## save model for student data
    def save_model(self,grade_file, student_file, prediction_function, algorithm_name, parameters, info, model, isDefault, course_name, semester):
        
        model_path = "models/"
        fname=""

        ##connection to db
        db = MySQLdb.connect("localhost","root","1234","ceng408" )
        cursor = db.cursor()
        
        if prediction_function == 'course_grade':
            fname=prediction_function+"_"+algorithm_name+"_"+course_name.lower()+"_"+str(self.total_rows) ## for giving name to models
            ## check default model for a course and change its isDefault
            update_q = "UPDATE models \
                        SET isDefault = 0 \
                        WHERE function='%s' AND course='%s' AND isDefault = 1" % (prediction_function, course_name)
        else:
            fname=prediction_function+"_"+algorithm_name+"_"+str(self.total_rows) ## for giving name to models
            ## check default model and change its isDefault
            update_q = "UPDATE models \
                        SET isDefault = 0 \
                        WHERE function='%s' AND isDefault = 1" % (prediction_function)
        try:
            cursor.execute(update_q)
            db.commit()
        except :
            db.rollback()
            
        
        ## save model and it's file to database
        if course_name==None and semester==None:
            s = "INSERT INTO models(gradeFile, studentFile, function, algorithm, accuracy, loss, path, paramPath, isDefault) \
                VALUES ('%s','%s','%s', '%s', '%f', '%f', '%s' ,'%s', '%s')" % (grade_file, student_file, prediction_function, algorithm_name, float(info[0]), float(info[1]), model_path+fname, model_path+fname+'.txt', isDefault)
        elif course_name!=None and semester==None:
            s = "INSERT INTO models(gradeFile, studentFile, function, algorithm, accuracy, loss, path, paramPath, isDefault, course) \
                VALUES ('%s','%s','%s', '%s', '%f', '%f', '%s' ,'%s', '%s', '%s')" % (grade_file, student_file, prediction_function, algorithm_name, float(info[0]), float(info[1]), model_path+fname, model_path+fname+'.txt', isDefault, course_name)
        elif course_name==None and semester!=None:
            s = "INSERT INTO models(gradeFile, studentFile, function, algorithm, accuracy, loss, path, paramPath, isDefault, semester) \
                VALUES ('%s','%s','%s', '%s', '%f', '%f', '%s' ,'%s', '%s', '%d')" % (grade_file, student_file, prediction_function, algorithm_name, float(info[0]), float(info[1]), model_path+fname, model_path+fname+'.txt', isDefault, semester)
            
        try:
            cursor.execute(s)
            db.commit()
            joblib.dump(model, model_path+fname)
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            print("Save model error!(func: save_model)")
            db.rollback()

        ##write parameters of model to text file
        with open(model_path+fname+'.txt','w') as output:
            for i in range(len(parameters)):
                output.write(str(parameters[i])+'\n')
        
        #self.update_default_models()

        db.close()
