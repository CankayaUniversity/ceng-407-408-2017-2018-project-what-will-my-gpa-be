import ML
from Tables import *
from sklearn.externals import joblib

## save models

def dropout_logistic(x,y,p):
    model = ML.logistic_regression(x,y,p) ##train model
    joblib.dump(model, "models/dropout_logistic_model") ##save model

def dropout_svm(x,y,p):
    model = ML.svm(x,y,p) 
    joblib.dump(model, "models/dropout_svm_model") 

def dropout_mlp(x,y,p):
    model = ML.mlp(x,y,p)
    joblib.dump(model, "models/dropout_mlp_model") 

def dropout_rnn(x,y,p):
    model = ML.rnn(x,y,p)
    joblib.dump(model, "models/dropout_rnn_model")

def courseGrade_logistic(x,y,p):
    model = ML.logistic_regression(x,y,p)
    joblib.dump(model, "models/courseGrade_logistic_model")

def courseGrade_svm(x,y,p):
    model = ML.svm(x,y,p)
    joblib.dump(model, "models/courseGrade_svm_model")

def courseGrade_mlp(x,y,p):
    model = ML.mlp(x,y,p)
    joblib.dump(model, "models/courseGrade_mlp_model")

def courseGrade_rnn(x,y,p):
    model = ML.rnn(x,y,p)
    joblib.dump(model, "models/courseGrade_rnn_model")

def gpa2_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa2_linear_model")

def gpa3_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa3_linear_model")

def gpa4_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa4_linear_model")

def gpa5_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa5_linear_model")

def gpa6_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa6_linear_model")

def gpa7_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa7_linear_model")

def gpa8_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa8_linear_model")

##graduation gpa
def gpa0_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa_graudation_linear_model")

def studyLength_linear(x,y,p):
    model = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/studyLength_linear_model")
