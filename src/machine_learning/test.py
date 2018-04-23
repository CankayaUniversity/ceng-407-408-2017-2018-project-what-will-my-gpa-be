from AppController import *

dic={'course':'ceng241'}
cl=['ceng361','cec243','ceng464','ceng466']
p = ['AA','CB','BB','BB']

ac = AppController()
##m= ac.create_new_model('dropout','logistic',None)
##ac.create_new_model('dropout','svm',None)
##ac.create_new_model('dropout','mlp',None)
##ac.create_new_model('study_length','linear',None)
##ac.create_new_model('gpa','linear',None)
##ac.create_new_model("course_grade","logistic",dic)
##ac.create_new_model("course_grade","svm",dic)
##ac.create_new_model("course_grade","mlp",dic)

##res=ac.predict_gpa(p,cl,'graduation')
##res = ac.predict_dropout(p,cl)
##res = ac.predict_length(p,cl)
res = ac.predict_course_grade(p,cl,'ceng241')

##print(res)
