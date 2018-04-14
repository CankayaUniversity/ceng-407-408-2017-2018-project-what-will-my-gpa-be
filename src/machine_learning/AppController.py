
from sklearn.externals import joblib
import ModelFunctions

class AppController:

    def __init__(self):

        ## load default models
        try:
            self.logistic = joblib.load("models/default/logistic_model")
            self.linear = joblib.load("models/default/linear_model")
            self.mlp = joblib.load("models/default/mlp_model")
            self.svm = joblib.load("models/default/svm_model")
            self.rnn = joblib.load("models/default/rnn_model")
        except IOError as e:
            print("One of the model file doesn't exist.")


    ## prediction functions
            
    def predict_course_grade(self,vector):
        return self.logistic.predict(vector)

    def predict_dropout(self,vector):
        return self.logistic.predict(vector)

    def predict_gpa(self,vector):
        return self.linear.predict(vector) 

    def predict_length(self,vector):
        return self.linear.predict(vector)


    ## new models
    def create_new_model(self, predict_function, algorithm_name, parameters):
        if predict_function=='gpa':
            
            pass
        elif predict_function=='dropout':
            
            pass
        elif predict_function=='course_grade':
            
            pass    
        elif predict_function=='study_length':
            
            pass
