from AppController import *

cl=['ceng361','cec243','ceng464','cec301','ceng114','ceng466','ceng191','ceng407','ceng408','eng405']
p = ['DD','CC','CC','CC','DD','DD','AA','BA','CC','CC',2.45]
params=[None,None,None,None]

ac = AppController()
##tb=Tables()
##tb.read_data("default_grade.csv","default_student.csv")
##x = tb.studyTable
##y = tb.studyLabel

##model, info, p = ac.create_new_model("default_grade.csv","default_student.csv",'dropout','logistic',params,None,None)
##model, info, p = ac.create_new_model("default_grade.csv","default_student.csv",'dropout','svm',     params,None,None)
##model, info, p = ac.create_new_model("default_grade.csv","default_student.csv",'dropout','mlp',     params,None,None)
##model, info, p = ac.create_new_model("default_grade.csv","default_student.csv","course_grade","logistic",params,'ceng241',None)
##model, info, p = ac.create_new_model("default_grade.csv","default_student.csv","course_grade","svm",params,'ceng241',None)
##model, info, p = ac.create_new_model("default_grade.csv","default_student.csv","course_grade","mlp",params,'ceng241',None)
##model, info, p = ac.create_new_model("default_grade.csv","default_student.csv","course_grade","mlp",params,'cec243',None)
##model, info = ac.create_new_model("default_grade.csv","default_student.csv",'study_length','linear',params,None,None)
model, info = ac.create_new_model("default_grade.csv","default_student.csv",'study_length','mlp_regressor',params,None,None)


##ac.save_model("default_grade.csv","default_student.csv",'dropout','logistic',params,info,model,0,None,None)
##ac.save_model("default_grade.csv","default_student.csv",'dropout','mlp',params,info,model,1,None,None)
##ac.save_model("default_grade.csv","default_student.csv",'course_grade','svm',params,info,model,1,'ceng241',None)
##ac.save_model("default_grade.csv","default_student.csv",'course_grade','mlp',params,info,model,1,'cec243',None)
##ac.save_model("default_grade.csv","default_student.csv",'study_length','linear',params,info,model,1,None,None)

##print(ac.predict_length(p,cl))
##print(ac.predict_dropout(p,cl))

##tb=Tables()
##tb.read_data("default_grade.csv","default_student.csv")
##x=tb.studyTable
##print(ac.study_length.predict(x))


