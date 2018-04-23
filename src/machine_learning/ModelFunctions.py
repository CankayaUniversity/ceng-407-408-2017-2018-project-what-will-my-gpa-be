import ML
from Tables import *
from sklearn.externals import joblib

## save models

def dropout_logistic(x,y,p):
    model, info = ML.logistic_regression(x,y,p) ##train model
    joblib.dump(model, "models/dropout_logistic_model") ##save model
    return info

def dropout_svm(x,y,p):
    model, info  = ML.svm(x,y,p) 
    joblib.dump(model, "models/dropout_svm_model")
    return info

def dropout_mlp(x,y,p):
    model, info  = ML.mlp(x,y,p)
    joblib.dump(model, "models/dropout_mlp_model")
    return info

def dropout_rnn(x,y,p):
    model, info  = ML.rnn(x,y,p)
    joblib.dump(model, "models/dropout_rnn_model")
    return info

def courseGrade_logistic(x,y,p):
    model, info  = ML.logistic_regression(x,y,p)
    joblib.dump(model, "models/course_"+p['course']+"_model")
    return info

def courseGrade_svm(x,y,p):
    model, info  = ML.svm(x,y,p)
    joblib.dump(model, "models/courseGrade_svm_model")
    return info

def courseGrade_mlp(x,y,p):
    model, info  = ML.mlp(x,y,p)
    joblib.dump(model, "models/courseGrade_mlp_model")
    return info

def courseGrade_rnn(x,y,p):
    model, info  = ML.rnn(x,y,p)
    joblib.dump(model, "models/courseGrade_rnn_model")
    return info

def gpa2_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa2_linear_model")
    return info

def gpa3_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa3_linear_model")
    return info

def gpa4_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa4_linear_model")
    return info

def gpa5_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa5_linear_model")
    return info

def gpa6_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa6_linear_model")
    return info

def gpa7_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa7_linear_model")
    return info

def gpa8_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa8_linear_model")
    return info

##graduation gpa
def graduationgpa_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/gpa7_model")
    return info

def studyLength_linear(x,y,p):
    model, info  = ML.linear_regression(x,y,p)
    joblib.dump(model, "models/studyLength_linear_model")
    return info
