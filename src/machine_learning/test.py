from AppController import *

dic={'course':'ceng241'}
cl=['ceng361','cec243','ceng464','cec301','ceng114','ceng466','ceng191','ceng407','ceng408','eng405']
p = ['AA','AA','AA','AA','AA','AA','AA','AA','AA','AA']
params=[None,None,None,None]

ac = AppController()
##model, info, p= ac.create_new_model('dropout','logistic',params,None)
##model, info, p=ac.create_new_model('dropout','svm',params,None)
##model, info, p=ac.create_new_model('dropout','mlp',params,None)
##model, info=ac.create_new_model('study_length','linear',None,None)
##model=ac.create_new_model('gpa','linear',None,None)
m,i,p=ac.create_new_model("course_grade","svm",params,'ceng241')
ac.save_model("course_grade","svm",p,i,m,1,'ceng241',None)
##m,i,p=ac.create_new_model("course_grade","svm",params,'cec243')
##m,i,p=ac.create_new_model("course_grade","mlp",params,'cec243')

##print(ac.predict_gpa(p,cl,'graduation'))
##print(ac.predict_dropout(p,cl))
##print(ac.predict_length(p,cl))
##print(ac.predict_course_grade(p,cl,'ceng241')
