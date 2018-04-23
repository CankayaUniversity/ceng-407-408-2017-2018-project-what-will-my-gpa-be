from sklearn.externals import joblib
from Tables import *
import ModelFunctions as mf

class AppController:
    def __init__(self):
        ## load default models
        try:
            self.dropout = joblib.load("models/dropout_logistic_model")
            self.graduation = joblib.load("models/gpa7_model")
            self.study_length = joblib.load("models/studyLength_linear_model")
            self.course_grade = joblib.load("models/course_logistic_model")
##            for i in range(8):
##                m = "models/gpa"+str(i)+"_model"
##                self.gpa.append(joblib.load(m))
        except IOError as e:
            print("One of the model file doesn't exist.")

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
        result = model[0].predict(lst)
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
        elif semester=='graduation': ##graduation gpa
            result = self.graduation[0].predict(lst)
            if result<0: result=result*-1
            return "%.2f"%result
         
    def predict_length(self,vector,course_list):
        vector=self.courses_to_numeric(vector,True)
        lst = np.empty(studyTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = study_imp.transform(lst)
        result = self.study_length[0].predict(lst)
        return np.round(result[0])


    ## new models
    def create_new_model(self, predict_function, algorithm_name, parameters):
        if predict_function=='gpa':
            
             if algorithm_name=='linear':
                return mf.graduationgpa_linear(graduationTable,graduationLabel,parameters)
            
        elif predict_function=='dropout':
            
            if algorithm_name=='logistic':
                return mf.dropout_logistic(dropoutTable, dropoutLabel, parameters)
            elif algorithm_name=='svm':
                return mf.dropout_svm(dropoutTable, dropoutLabel, parameters)
            elif algorithm_name=='mlp':
                return mf.dropout_mlp(dropoutTable, dropoutLabel, parameters)
##            elif algorithm_name=='rnn':
##                mf.dropout_rnn(dropoutTable, dropoutLabel, parameters)
            
        elif predict_function=='course_grade':
            c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
            x = courseTable[:]
            course_name = parameters['course'].lower()
            class_index = courseList.index(course_name)
            y = x[:,class_index] ## class label
            x = np.delete(x,class_index,1) ## remove class column from input data
            ## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
            for i in range(y.size):
                    index = c.index(y[i])
                    y[i] = index
            
            if algorithm_name=='logistic':
                return mf.courseGrade_logistic(x,y,parameters)
            elif algorithm_name=='svm':
                return mf.courseGrade_svm(x,y,parameters)
            elif algorithm_name=='mlp':
                return mf.courseGrade_mlp(x,y,parameters)
##            elif algorithm_name=='rnn':
##                mf.courseGrade_rnn(courseTable,courseLabel,parameters)

        elif predict_function=='study_length':
            
            if algorithm_name=='linear':
                return mf.studyLength_linear(studyTable, studyLabel, parameters)
