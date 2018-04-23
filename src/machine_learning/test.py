from AppController import *

dic={'course':'ceng241'}
cl=['ceng361','cec243','ceng464','cec301','ceng114','ceng466','ceng191','ceng407','ceng408','eng405']
p = ['AA','AA','AA','AA','AA','AA','AA','AA','AA','AA']

ac = AppController()
##m= ac.create_new_model('dropout','logistic',None)
##m=ac.create_new_model('dropout','svm',None)
##m=ac.create_new_model('dropout','mlp',None)
##m=ac.create_new_model('study_length','linear',None)
##m=ac.create_new_model('gpa','linear',None)
##m=ac.create_new_model("course_grade","logistic",dic)
##m=ac.create_new_model("course_grade","svm",dic)
##m=ac.create_new_model("course_grade","mlp",dic)

##print(m)

res=ac.predict_gpa(p,cl,'graduation')
##res = ac.predict_dropout(p,cl)
##res = ac.predict_length(p,cl)
##res = ac.predict_course_grade(p,cl,'ceng241')
print(res)

##a = ['AA'] *118
##b=courseList
##b = [x for x in b if x != 'ceng241']

##x=courseTable.copy()
##class_index = courseList.index('ceng241')
##x = np.delete(x,class_index,1) ## remove class column from input data
##y=courseList.copy()
##y = [i for i in y if i != 'ceng241']
##
##res = ac.predict_course_grade(x[0],y,'ceng241')
##print(res)
