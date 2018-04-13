
import ML
from sklearn.externals import joblib

## save models

def dropout_logistic(x,y):
    model = ML.logistic_regression(x,y) ##get model
    joblib.dump(model, "dropout_logistic_model") ##save model

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

def gpa_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "gpa_linear_model")

def studyLength_linear(x,y):
    model = ML.linear_regression(x,y)
    joblib.dump(model, "studyLength_linear_model")
