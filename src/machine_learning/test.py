from AppController import *

ac = AppController()
ac.create_new_model('dropout','logistic',None)
ac.create_new_model('dropout','svm',None)
ac.create_new_model('dropout','mlp',None)
ac.create_new_model('study_length','linear',None)
ac.create_new_model('gpa','linear',None)

##cl=['ceng361','cec243','ceng464','ceng466']
##p = [3,2.5,3.5,2]
##res = ac.predict_dropout(p,cl)
