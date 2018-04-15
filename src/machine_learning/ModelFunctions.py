import ML
from Tables import *
from sklearn.externals import joblib

## save models

def dropout_logistic(x,y):
    model = ML.logistic_regression(x,y) ##train model
    joblib.dump(model, "models/default/dropout_logistic_model") ##save model

def dropout_svm(x,y):
    model = ML.svm(x,y) 
    joblib.dump(model, "dropout_svm_model") 

def dropout_mlp(x,y):
    model = ML.mlp(x,y)
    joblib.dump(model, "dropout_mlp_model") 

def dropout_rnn(x,y):
    model = ML.rnn(x,y)
    joblib.dump(model, "dropout_rnn_model")

def courseGrade_logistic(x,y):
    model = ML.logistic_regression(x,y)
    joblib.dump(model, "courseGrade_logistic_model")

def courseGrade_svm(x,y):
    model = ML.svm(x,y)
    joblib.dump(model, "courseGrade_svm_model")

def courseGrade_mlp(x,y):
    model = ML.mlp(x,y)
    joblib.dump(model, "courseGrade_mlp_model")

def courseGrade_rnn(x,y):
    model = ML.rnn(x,y)
    joblib.dump(model, "courseGrade_rnn_model")

def gpa2_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa2_linear_model")

def gpa3_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa3_linear_model")

def gpa4_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa4_linear_model")

def gpa5_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa5_linear_model")

def gpa6_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa6_linear_model")

def gpa7_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa7_linear_model")

def gpa8_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa8_linear_model")

##graduation gpa
def gpa0_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa_graudation_linear_model")

def studyLength_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "studyLength_linear_model")
