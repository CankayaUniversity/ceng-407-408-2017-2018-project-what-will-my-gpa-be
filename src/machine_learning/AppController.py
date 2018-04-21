from sklearn.externals import joblib
from Tables import *
import ModelFunctions as mf

class AppController:
    def __init__(self):
        
        ## load default models
        try:
            self.dropout = joblib.load("models/default/dropout_model")
            self.gpa2 = joblib.load("models/default/gpa2_model")
            self.gpa3 = joblib.load("models/default/gpa3_model")
            self.gpa4 = joblib.load("models/default/gpa4_model")
            self.gpa5 = joblib.load("models/default/gpa5_model")
            self.gpa6 = joblib.load("models/default/gpa6_model")
            self.gpa7 = joblib.load("models/default/gpa7_model")
            self.gpa8 = joblib.load("models/default/gpa8_model")
            self.graduation = joblib.load("models/default/graduation_gpa_model")
            self.study_length = joblib.load("models/default/study_length_model")
            self.course_grade = joblib.load("models/default/course_grade_model")
        except IOError as e:
            print("One of the model file doesn't exist.")


    ## prediction functions
    def predict_course_grade(self,vector,course_list,pcourse_name):
        lst = np.empty(courseTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = course_imp.transform(lst)
        result = self.course_grade.predict(vector)
        print(result)
##        return 

    def predict_dropout(self,vector,course_list):
        lst = np.empty(dropoutTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = dropout_imp.transform(lst)
        result = self.dropout.predict(lst)
        if result[0] == 1: return True
        else:   return False

    def predict_gpa(self,vector,semester,course_list):
        if semester=='2':
            return self.gpa2.predict(vector)
        elif semester=='3':
            return self.gpa3.predict(vector)
        elif semester=='4':
            return self.gpa4.predict(vector)
        elif semester=='5':
            return self.gpa5.predict(vector)
        elif semester=='6':
            return self.gpa6.predict(vector)
        elif semester=='7':
            return self.gpa7.predict(vector)
        elif semester=='8':
            return self.gpa8.predict(vector)
        elif semester=='0': ##graduation gpa
            return self.graduation.predict(vector)
         
    def predict_length(self,vector,course_list):
        lst = np.empty(studyTable.shape[1])
        lst[:] = np.nan
        for i in range(len(course_list)):
            lst[courseList.index(course_list[i])] = vector[i]
        lst = lst.reshape(1,-1)
        lst = study_imp.transform(lst)
        result = self.study_length.predict(lst)
        print(result)
##        return self.study_length.predict(lst)


    ## new models
    def create_new_model(self, predict_function, algorithm_name, parameters):
        if predict_function=='gpa':
            
             if algorithm_name=='linear':
                pass
            
        elif predict_function=='dropout':
            
            if algorithm_name=='logistic':
                mf.dropout_logistic(dropoutTable, dropoutLabel, parameters)
            elif algorithm_name=='svm':
                mf.dropout_svm(dropoutTable, dropoutLabel, parameters)
            elif algorithm_name=='mlp':
                mf.dropout_mlp(dropoutTable, dropoutLabel, parameters)
            elif algorithm_name=='rnn':
                mf.dropout_rnn(dropoutTable, dropoutLabel, parameters)
            
        elif predict_function=='course_grade':
            
            if algorithm_name=='logistic':
                pass
            elif algorithm_name=='svm':
                pass
            elif algorithm_name=='mlp':
                pass
            elif algorithm_name=='rnn':
                pass

        elif predict_function=='study_length':
            
            if algorithm_name=='linear':
                mf.studyLength_linear(studyTable, studyLabel, parameters)
