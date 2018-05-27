
#Efnan Gülkanat, Meltem Daşdemir
import os
from flask import make_response
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
#from Grad_year import fin_grad_year
from flask import Markup
from flask_mail import Mail, Message

import smtplib
from email.mime.text import MIMEText
import csv
import pandas as pd
import time
from subprocess import Popen, PIPE




from VectorCourseYear import *
from DropoutYear import *
from AppController import *
from PassFailRate import *
from StudentSemester import *
from UniqueCourses import *
from DeparmentSuccessElective import *
from DepartmentSuccess import *
from GraduateMaleFemaleSuccess import *
from LeaveSuccessRate import *
from werkzeug.utils import secure_filename
from dbinfo import *

app = Flask(__name__)
colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
a=AppController()
model=None
parameters=None
info=None
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = mysl_user
app.config['MYSQL_PASSWORD'] = password
UPLOAD_FOLDER="data/"
UPLOAD_FOLDER_STUDENT ="datastudent/"
ALLOWED_EXTENSIONS = set(['csv'])
#app.config['MYSQL_DB'] = 'gpa_db_3'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_STUDENT'] = UPLOAD_FOLDER_STUDENT
db_name_deneme = "gpa_db_4"
#sql_filename = "C:/Users/DAŞDEMİR/Documents/dumps/Dump20180504.sql"
# init MYSQL
rector_mail = "gpapredict.123@gmail.com"
mysql = MySQL(app)


app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'gpapredict.123@gmail.com',
    MAIL_PASSWORD = 'gpapredict123'
)

mail = Mail(app)
#mail = Mail(app)


#Articles = Articles()

# Index
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    #if(session['logged_in'] == True):
        #data=session['data1']
        #return redirect_login(data)     




        

        #redirect_login(session['data1'])
    
    #process = Popen(['mysql.exe', db_name_deneme, '-u', "root", '-p', "abc123"],
                #stdout=PIPE, stdin=PIPE)
    #output = process.communicate('source ' + sql_filename)[0]

    cmd = "show databases" 
    #Execute query
    # #print(cmd)
    result = cur.execute(cmd)
    database_built = False
    if result > 0:
        data = cur.fetchall()
        for i in range(len(data)):
            row = data[i]
            if row["Database"] == db_name_deneme:#app.config['MYSQL_DB']:#app.config['MYSQL_DB']:
                database_built = True
                break
        #print(data)
        if database_built == False:
            cmd = "CREATE DATABASE %s" % db_name_deneme#(app.config['MYSQL_DB'])
            if run_cmd(cur, cmd, "Couldn't build database.") != -1:
                cmd =  """CREATE TABLE IF NOT EXISTS %s.`users` ( 
                            `name` VARCHAR(45) NOT NULL, 
                            `email` VARCHAR(45) NULL,
                            `username` VARCHAR(45) NULL,
                            `password` VARCHAR(255) NULL,
                            `user_type` INT NULL,
                            `user_id` INT NOT NULL AUTO_INCREMENT,
                            `is_approved` BOOL DEFAULT FALSE,
                            PRIMARY KEY (`user_id`),
                            UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC))""" % (db_name_deneme)
                run_cmd(cur, cmd, "Couldn't build table.")
                 #time.sleep(1)
                 #print("time.sleep called.")

                print("First table built.")
            #    cmd =  """CREATE TABLE IF NOT EXISTS %s.`gpas` ( 
            #                 `coursename` VARCHAR(45) NOT NULL, 
            #                 `grade` VARCHAR(45) NULL,
            #                 `user_id` INT,
            #                 `gpa_id` INT NOT NULL AUTO_INCREMENT,
            #                 PRIMARY KEY (`gpa_id`))
            #                 #FOREIGN KEY(`user_id`) REFERENCES users(`user_id`))
            #                 """ % (db_name_deneme)
            #     run_cmd(cur, cmd, "Couldn't build table.")
            #     cmd = """ALTER TABLE %s.`gpas` ADD FOREIGN KEY (`user_id`) REFERENCES users(`user_id`)
            #           """ % (db_name_deneme) 
            #     run_cmd(cur, cmd, "Couldn't alter table.")            

        app.config['MYSQL_DB'] = 'gpa_db_4'        
    return render_template('home.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree

path="data/"
pathsstudent="datastudent/"
#path = os.path.expanduser('C:/Users/DAŞDEMİR/Desktop/GPA/myflaskapp/data')
#pathsstudent = os.path.expanduser('C:/Users/DAŞDEMİR/Desktop/GPA/myflaskapp/datastudent')

@app.route('/MezunKizErkek', methods=['GET', 'POST'])
def MezunKizErkek():
    temp=[]
    file = session['file']
    #print(str(file))
    global filenew1
    filenew1=request.args.get('dropdown_list')
    if "dropdown" in str(filenew1):
        count=filenew1.count('?')
        a=filenew1.replace('?dropdown_list=', ',') 
        b=a.split(",")
        
        filenew1=b[count]

    if(file is None and filenew1 is None):
        file="student.csv"
        temp=file
        values,values1,labels=get_sex_file(file)
    elif not(filenew1 is None):
        values,values1,labels=get_sex_file(filenew1)
        temp=filenew1
    elif not(file is None):
        values,values1,labels=get_sex_file(file)
        temp=file
    return render_template('MezunKizErkek.html',courses=courses,values=values,labels=labels,values1=values1,file=temp)

filenew = None
@app.route('/BolumOnce', methods=['GET', 'POST'])
def BolumOnce():
    file=session['file']
    values=[]
    temp=[]
    labels=[]
    global filenew
    select = request.args.get('comp')
   
    file_curr  = request.args.get('dropdown_list')
    if  file_curr != None:
        filenew = file_curr        
    if "dropdown" in str(select):
        count=select.count('?')
        a=select.replace('?dropdown_list=', ',') 
        b=a.split(",")
        select=b[0]
        filenew=b[count]
       
    if(file is None or filenew is None):
        file='grade2.csv'
        temp=file
        courses=course_file_list(file)
    elif not(filenew is None):
        temp=filenew
        courses=course_file_list(file)
    elif not(file is None):
        temp=file
        courses=course_file_list(file)
    
    if not (select is None):
        if((file is None) and (filenew is None)):
            file='grade2.csv'
            temp=file
            labels,values=get_file(select,file)
            #return render_template('BolumOnce.html', set=zip(values, labels, colors), values=values, labels=labels, courses=courses,select=select,file=temp)
        elif not(filenew is None):
            labels,values=get_file(select,filenew)
            temp=filenew
            #return render_template('BolumOnce.html', set=zip(values, labels, colors), values=values, labels=labels, courses=courses,select=select,file=temp)
        elif not(file is None):
            labels,values=get_file(select,file)
            temp=file
            #return render_template('BolumOnce.html', set=zip(values, labels, colors), values=values, labels=labels, courses=courses,select=select,file=temp)
    return render_template('BolumOnce.html', set=zip(values, labels, colors), values=values, labels=labels, courses=courses,select=select,file=temp)
@app.route('/KursBırakma', methods=['GET', 'POST'])
def KursBırakma():
    values=[]
    labels=[]
    temp=[]
    file=session['file']
    global filenew1
    filenew1=request.args.get('dropdown_list')
    if(filenew1!='Seçiniz..'):
        if "dropdown" in str(filenew1):
            count=filenew1.count('?')
            a=filenew1.replace('?dropdown_list=', ',') 
            b=a.split(",")

            filenew1=b[count]
    if(file is None and filenew1 is None):
        file="student.csv"
        temp=file
        labels,values=get_drop_file(file)
    elif not(filenew1 is None):
        labels,values=get_drop_file(filenew1)
        temp=filenew1
    elif not(file is None):
        labels,values=get_drop_file(file)
        temp=file
    return render_template('KursBırakma.html', set=zip(values, labels, colors), values=values,labels=labels,file=temp)

@app.route('/BırakanlarBasarı', methods=['GET', 'POST'])
def BırakanlarBasarı():
    temp=[]
    values=[]
    labels=[]
    file=session['file']
    global filenew1
    filenew1=request.args.get('dropdown_list')
    #print(filenew1)
    if "dropdown" in str(filenew1):
        count=filenew1.count('?')
        a=filenew1.replace('?dropdown_list=', ',') 
        b=a.split(",")
        
        filenew1=b[count]   

    print(filenew1)
    
    if(file is None and filenew1 is None):
        file="student.csv"
        temp=file
        values,labels=get_leavg_file(file)
    elif not(filenew1 is None):
        values,labels=get_leavg_file(filenew1)
        temp=filenew1
    elif not(file is None):
        values,labels=get_leavg_file(file)
        temp=file
    return render_template('BırakanlarBasarı.html', set=zip(values, labels, colors), values=values,labels=labels,courses=courses,file=temp) 
@app.route('/KursRaporlamaOnce', methods=['GET', 'POST'])
def KursRaporlamaOnce():
    temp=[]
    values=[]
    labels=[]
    courses=[]
    file=session['file']
    global filenew
    
    if(file is None or filenew is None):
        file='grade2.csv'
        temp=file
        courses=course_list(file)
    elif not(filenew is None):
        temp=filenew
        values,labels=course_list(file)
    elif not(file is None):
        temp=file
        values,labels=course_list(file)
    select = request.args.get('comp_select')
    #print(select)
    if "dropdown" in str(select):
        count=select.count('?')
        a=select.replace('?dropdown_list=', ',') 
        b=a.split(",")
        select=b[0]
        filenew=b[count]
       
            

    if not (select is None):
        if(file is None and filenew is None):
            file="grade2.csv"
            temp=file
            values,labels=get_course_file(str(select),file)
        elif not(filenew is None):
            temp=filenew
            values,labels=get_course_file(str(select),filenew)
        elif not(file is None):
            temp=file
            values,labels=get_course_file(select,file)
    return render_template('KursRaporlamaOnce.html', set=zip(values, labels, colors), values=values,labels=labels,courses=courses,select=select,file=temp)

@app.route('/OgrencıKursOnce', methods=['GET', 'POST'])
def OgrencıKursOnce():
    file=session['file']
    temp=[]
    values=[]
    labels=[]
    global filenew
    ıd=request.args.get('text')
    select = request.args.get('comp')
    if "dropdown" in str(ıd): 
        count=ıd.count('?')
        a=ıd.replace('?dropdown_list=', ',') 
        b=a.split(",")
        ıd=b[0]
        filenew=b[count]  
    
    if(file is None or filenew is None):
        file='grade2.csv'
        temp=file
        courses=course_file_list(file)
    elif not(filenew is None):
        temp=filenew
        courses=course_file_list(filenew)
    elif not(file is None):
        temp=file
        courses=course_file_list(file)

    if not (select is None and ıd is None):
        if(file is None and filenew is None):
            print("1")
            file="grade2.csv"
            temp=file
            labels,values=get_semester_sucfile(int(ıd),str(select),file)
        elif not(filenew is None):
            print("2")
            temp=filenew
            labels,values=get_semester_sucfile(int(ıd),str(select),filenew)
        elif not(file is None):
            print("3")
            temp=file
            labels,values=get_semester_sucfile(int(ıd),str(select),file)
            print(labels,values)
    return render_template('OgrencıKursOnce.html', set=zip(values, labels, colors), values=values,labels=labels,courses=courses,select=select,ıds=ıd,file=temp) 

@app.route('/OgrencıDonemOnce', methods=['GET', 'POST'])
def OgrencıDonemOnce():
    temp=[]
    values=[]
    labels=[]
    global filenew
    select = request.args.get('text')
    if "dropdown" in str(select):
        count=select.count('?')
        a=select.replace('?dropdown_list=', ',') 
        b=a.split(",")
        select=b[0]
        filenew=b[count]  
    
    file=session['file']
    #print(select)
    if not (select is None):
        if(file is None and filenew is None):
            
            file="grade2.csv"
            temp=file
            labels,values=get_semester_file(int(select),file)
        elif not(filenew is None):
            
            temp=filenew
            labels,values=get_semester_file(int(select),filenew)
        elif not(file is None):
            
            temp=file
            labels,values=get_semester_file(int(select),file)
        
    return render_template('OgrencıDonemOnce.html', set=zip(values, labels, colors), values=values,labels=labels,select=select,file=temp)

@app.route('/KalmaGecmeOnce', methods=['GET', 'POST'])
def KalmaGecmeOnce():
    file=session['file']
    temp=[]
    values=[]
    values1=[]
    labels=[]
    global filenew
    if(file is None or filenew is None):
        file='grade2.csv'
        temp=file
        courses=course_list(file)
    elif not(filenew is None):
        temp=filenew
        courses=course_list(file)
    elif not(file is None):
        temp=file
        courses=course_list(file)
 
    select = request.args.get('comp_select')
    if "dropdown" in str(select):
        count=select.count('?')
        a=select.replace('?dropdown_list=', ',') 
        b=a.split(",")
        select=b[0]
        filenew=b[count]
       
    if not (select is None):
        if(file is None and filenew is None):
            file="grade2.csv"
            temp=file
            values,values1,labels=get_pass_file(str(select),file)
        elif not(filenew is None):
            temp=filenew
            values,values1,labels=get_pass_file(str(select),filenew)
        elif not(file is None):
            temp=file
            values,values1,labels=get_pass_file(str(select),file)
        
    return render_template('KalmaGecmeOnce.html',courses=courses,values=values,labels=labels,values1=values1,select=select,file=temp)
 
@app.route('/BolumSecmelıOnce', methods=['GET', 'POST'])
def BolumSecmelıOnce():
    values=[]
    labels=[]
    temp=[]
    file=session['file']
    global filenew
    if(file is None or filenew is None):
        file='grade2.csv'
        temp=file
        courses=course_file_list(file)
    elif not(filenew is None):
        temp=filenew
        courses=course_file_list(file)
    elif not(file is None):
        temp=file
        courses=course_file_list(file)
    ıd=request.args.get('elec')
    select = request.args.get('comp')
    print(select)
    print(ıd)
    if "dropdown" in str(ıd):
        count=ıd.count('?')
        a=ıd.replace('?dropdown_list=', ',') 
        b=a.split(",")
        ıd=b[0]
        filenew=b[count]

       
       

    if not (select is None and ıd is None):
        if(file is None and filenew is None):
            file='grade2.csv'
            temp=file
            labels,values=get_suc_file(select,ıd,file)
        elif not(filenew is None):
            temp=filenew
            labels,values=get_suc_file(select,ıd,filenew)
        elif not(file is None):
            temp=file
            labels,values=get_suc_file(select,ıd,file)
    return render_template('BolumSecmelıOnce.html', set=zip(values, labels, colors), courses=courses, values=values, labels=labels,select=select,ıds=ıd,file=temp)

@app.route('/AddStudentData',methods=['GET', 'POST'])
def AddStudentData(): 
    if request.method == 'POST':  
        files = request.files['file']
        if files and allowed_file(files.filename):
            global filename
            filename = secure_filename(files.filename)
            files.save(os.path.join(app.config['UPLOAD_FOLDER_STUDENT'], filename))
            return redirect(url_for('AddStudentData',
                                    filename=filename))
    
    return render_template('AddStudentData.html',tree=make_tree(pathsstudent))
 
@app.route('/AddData',methods=['GET', 'POST'])
def AddData(): 
    if request.method == 'POST':  
        files = request.files['file']
        if files and allowed_file(files.filename):
            global filename
            filename = secure_filename(files.filename)
            files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('AddData',
                                    filename=filename))
    
    return render_template('AddData.html',tree=make_tree(path))
 
def delete_table():
    cur = mysql.connection.cursor()
    user_id=session['user_id']
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s", [user_id])
    if result1>0:
        cur.execute("TRUNCATE TABLE gpas")

@app.route("/EditCourses", methods=['GET', 'POST'])
def EditCourses():
    db = MySQLdb.connect("localhost","root","123456","gpa_db_4" )
    cursor = db.cursor() 
    cur = mysql.connection.cursor()
    
    user_id=session['user_id']
    rows=[]
    isDel=0
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s AND isDeleted = %s ", ([user_id], 0))
    if result1>0:
        data1=cur.fetchall()
        index=0
        for i in range(len(data1)):
            row = dict(semesters=data1[index]["semester"],grades=data1[index]["grade"],courses=data1[index]["coursename"])
            rows.append(row)
            index += 1
    if request.method=='POST':
        gra = request.form.getlist('educationDate')
        course = request.form.getlist('CourseName')
        semes= request.form.getlist('Semester')
        check_box=request.form.getlist('check_box')
        for i in range(len(semes)):
            semes[i]=int(semes[i])
        result1=0
        if(gra and course and semes):
           
            for i in range(len(course)):
                if((rows[i]['courses']!=course[i]) or (rows[i]['semesters']!=semes[i]) or (rows[i]['grades']!=gra[i])):
                    if(check_box[i]=='Select..'):
                        print(gra,course,semes,check_box)
                        print(course[i])
                        couna=rows[i]['courses']
                        result1 = cur.execute("SELECT * FROM gpas WHERE coursename=%s ", [couna] )
                        if result1>0:
                            data1=cur.fetchone()
                            gpaid = data1['gpa_id']
                            cmd="UPDATE gpas \
                                    SET coursename= '%s', grade= '%s', semester= '%s', isDeleted='%s' \
                                    WHERE gpa_id='%s'" % (course[i],gra[i],semes[i],0,gpaid)
                            cursor.execute(cmd)
                            db.commit()   
                    elif(check_box[i]=='Delete'):
                        couna=course[i]
                        result2 = cur.execute("SELECT * FROM gpas WHERE coursename=%s ", [couna] )
                        if result2>0:
                            data1=cur.fetchone()
                            gpaid = data1['gpa_id']
                            cmd="UPDATE gpas \
                                    SET coursename= '%s', grade= '%s', semester= '%s', isDeleted='%s' \
                                    WHERE gpa_id='%s'" % (course[i],gra[i],semes[i],1,gpaid)
                            cursor.execute(cmd)
                            db.commit() 
        return redirect(url_for('EditCourses'))        

    return render_template('EditCourses.html',rows=rows) 

@app.route("/SeeCourses", methods=['GET', 'POST'])
def SeeCourses():
    user_id=session['user_id']
    cur = mysql.connection.cursor()
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s AND isDeleted = %s ", ([user_id], 0))
    rows=[]
    if result1 > 0:
     
        data1=cur.fetchall()
        index=0
        rows=[]
        for i in range(len(data1)):
            row = dict(semesters=data1[index]["semester"],grades=data1[index]["grade"],courses=data1[index]["coursename"])
            rows.append(row)
            index += 1
    return render_template('SeeCourses.html',rows=rows)



@app.route("/OgrencıGPA", methods=['GET', 'POST'])
def OgrencıGPA():
    user_id=session['user_id']
    cur = mysql.connection.cursor()
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s AND isDeleted = %s ", ([user_id], 0))
    rows=[]
    grades=[]
    courses=[]
    num=[]
    if result1 > 0:
        data1=cur.fetchall()
        index=0
        rows=[]
        for i in range(len(data1)):
            row = dict(semesters=data1[index]["semester"],grades=data1[index]["grade"],courses=data1[index]["coursename"])
            rows.append(row)
            grades.append(data1[index]["grade"])
            courses.append(data1[index]["coursename"])
            index += 1

    num=a.predict_gpa(grades,courses)
    #print(num)
    return render_template('OgrencıGPA.html',num=num,rows=rows)

@app.route("/OgrencıKurs", methods=['GET', 'POST'])
def OgrencıKurs():
    user_id=session['user_id']
    cur = mysql.connection.cursor()
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s AND isDeleted = %s ", ([user_id], 0))
    rows=[]
    num="Result: "
    grades=[]
    courses=[]
    if result1 > 0:
     
        data1=cur.fetchall()
        index=0
        rows=[]
        for i in range(len(data1)):
            row = dict(semesters=data1[index]["semester"],grades=data1[index]["grade"],courses=data1[index]["coursename"])
            rows.append(row)
            grades.append(data1[index]["grade"])
            courses.append(data1[index]["coursename"])
            index += 1
    as_dict2= request.args.get('Predict_name')
    name=request.args.get('clicked')
    if(name=='Predict'):
        num=num+a.predict_course_grade(grades,courses,as_dict2)
    print(as_dict2)
    return render_template('OgrencıKurs.html',num=num,rows=rows)

@app.route("/CoursesPage", methods=['GET', 'POST'])
def CoursesPage():
    cur = mysql.connection.cursor()
    username=session['username']
    courses=[]
    grades=[]
    semesters=[]
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
    if result > 0:
        data = cur.fetchone()
        user_id = data['user_id']
    string=[]  
    #print(user_id,isDel)
    #cmd = "SELECT * \
            #FROM gpas \
            #WHERE user_id='%s' " % ([user_id])
    
    #result1 = cur.execute(cmd)
    #print(result1)
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s AND isDeleted = %s ", ([user_id], 0))
    rows=[]
    if result1 > 0:
        data1=cur.fetchall()
        #print(data1)
        index=0
        rows=[]
        for i in range(len(data1)):
            row = dict(semesters=data1[index]["semester"],grades=data1[index]["grade"],courses=data1[index]["coursename"],deleted=data1[index]["isDeleted"])
            rows.append(row)
            index += 1
    temp=1
    grade = request.args.getlist('educationDate')
    coursename = request.args.getlist('CourseName')
    semester= request.args.getlist('Semester')    
    if(grade!="" and coursename!="" and semester!=""):
        for i in range(len(semester)):
            if(bool(rows)):
                for j in range(len(rows)):
                    if(rows[j]['courses']==coursename[i] and rows[j]['deleted']==0):
                        print("not added user")
                        temp=0
                        break
                    elif(rows[j]['courses']==coursename[i] and rows[j]['deleted']==1):
                        temp=1
                        break
                if(temp!=0):
                    cmd = "INSERT INTO gpas (coursename, grade,semester,user_id,isDeleted) VALUES(\"%s\", \"%s\", %d, %d, %d)" % (coursename[i], grade[i],int(semester[i]), user_id,0)
                    if run_cmd(cur, cmd, "Couldn't add user.") != -1:
                        print("Added user")    
            else:
                cmd = "INSERT INTO gpas (coursename, grade,semester,user_id,isDeleted) VALUES(\"%s\", \"%s\", %d, %d, %d)" % (coursename[i], grade[i],int(semester[i]), user_id,0)
                if run_cmd(cur, cmd, "Couldn't add user.") != -1:
                    print("Added user")  
    #print(rows)
    
    
    mysql.connection.commit()
   
    return render_template('CoursesPage.html')

        

@app.route('/CreateModel')
def CreateModel():
    return render_template('CreateModel.html')


@app.route('/LogıstıcRegressıon')
def LogıstıcRegressıon():
    name=[]
    name=request.args.get('clicked')
    
    file_curr=[]
    file_curr  = request.args.get('dropdown_list')
    file_curr_student= request.args.get('dropdown_list1')
    file=session['file']
    
    courses=[]
    if ((file_curr_student==None  or file_curr_student=='Seçiniz..') and (file_curr==None or file_curr=='Seçiniz..') ):
        file_curr_student="student.csv"
        file_curr="grade2.csv"
        courses=course_list(file_curr)
    elif  file_curr != None:
        filenew = file_curr        
        courses=course_list(filenew) 

    algorithm="logistic"
    
    global model,info,parameters,predict_f
    temp1=[]
    temp2=[]
    select=None
    predict_function=request.args.get('prediction_function')
    if(predict_function!='Select..'):
        if(predict_function=='Course Grade Prediction'):
            temp1="course"
            predict_f="course_grade"
        elif(predict_function=='Dropout for a Student'):
            temp1="c"
            predict_f="dropout"
    coursename=request.args.get('course')
    select = request.args.getlist('ıteratıon')
    check_box=request.args.get('check_box')
    if(name=='CreateModel'):
        temp2="button"
        if(select[0]!= ""):
            select[0]=float(select[0])
        if(select[2] != ""):
            select[2]=int(select[2])
        if(predict_f=="course_grade"):
            session['coursename']=coursename
            model,info,parameters=a.create_new_model(file_curr,file_curr_student,predict_f, algorithm, select, coursename.lower(), None)        
        else:
            model,info,parameters=a.create_new_model(file_curr,file_curr_student,predict_f, algorithm, select, None, None)
        return render_template('LogıstıcRegressıon.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=parameters,info=info,temp=coursename,temp1=temp1,temp2=temp2)
    
    elif(name=='SaveModel'):
        temp2="s"
        isdef=1
        if check_box==None:
            isdef=0
        if(predict_f=="course_grade"):
            coursename=session['coursename']
            a.save_model(file_curr,file_curr_student,predict_f, algorithm, parameters,info,model,isdef,coursename.lower(),None)    
        else:
            a.save_model(file_curr,file_curr_student,predict_f, algorithm, parameters,info,model,isdef,None,None)
  
    
    return render_template('LogıstıcRegressıon.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=[],info=[],temp=coursename,temp1=temp1,temp2=temp2)


@app.route('/MultılayerPerceptıon')
def MultılayerPerceptıon():
    file_curr=[]
    temp1=[]
    file_curr  = request.args.get('dropdown_list')
    file_curr_student= request.args.get('dropdown_list1')
    file=session['file']
    courses=[]
    check_box=request.args.get('check_box')
    if ((file_curr_student==None  or file_curr_student=='Seçiniz..') and(file_curr==None or file_curr=='Seçiniz..') ):
        file_curr_student="student.csv"
        file_curr="grade2.csv"
        courses=course_list(file_curr)
    elif  file_curr != None:
        filenew = file_curr        
        courses=course_list(filenew) 
   
    algorithm="mlp"
    global model,info,parameters,predict_f
    select=None
    temp2=[]
    predict_function=request.args.get('predict_function')
    if(predict_function!='Select..'):
        if(predict_function=='Course Grade Prediction'):
            temp1="course"
            predict_f="course_grade"
        elif(predict_function=='Dropout for a Student'):
            temp1="c"
            predict_f="dropout"
    coursename=request.args.get('course')
    select = request.args.getlist('ıteratıon')
    name=[]
    name=request.args.get('clicked')
    if(name=='CreateModel'): 
        temp2="button" 
        if(select[0]!= ""):
            tup=(0,0);
            tup=list(tup)                                                                                                                
            tup[0]=int(select[0])
            tup[1]=int(select[1])
            tup=tuple(tup)
            del select[0]
            del select[0]
            select=[tup]+select
            print(select)
        if(select[3] != ""):
            select[3]=float(select[3])  
        if(select[4] != ""):
            select[4]=int(select[4])
        if(select[6] != ""):
            select[6]=int(select[6])  
        if(select[5] != ""):
            select[5]=float(select[5]) 
        if(select[7] != ""):
            select[7]=float(select[7]) 
        if(predict_f=="course_grade"):
            session['coursename']=coursename
            model,info,parameters=a.create_new_model(file_curr,file_curr_student,predict_f, algorithm, select, coursename.lower(), None)       
        else:  
            model,info,parameters=a.create_new_model(file_curr,file_curr_student,predict_f, algorithm, select, None, None)
        return render_template('MultılayerPerceptıon.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=parameters,info=info,temp=coursename,temp1=temp1,temp2=temp2)
    elif(name=='SaveModel'):
        temp2="s"
        isdef=1
        if check_box==None:
            isdef=0
        if(predict_f=="course_grade"):
            coursename=session['coursename']
            a.save_model(file_curr,file_curr_student,predict_f, algorithm, parameters,info,model,isdef,coursename.lower(),None)    
        else:
            a.save_model(file_curr,file_curr_student,predict_f, algorithm, parameters,info,model,isdef,None,None)          
    return render_template('MultılayerPerceptıon.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=[],info=[],temp=coursename,temp1=temp1,temp2=temp2)
 

@app.route('/SupportVectorMachıne')
def SupportVectorMachıne():
    
    check_box=request.args.get('check_box')
    file_curr  = request.args.get('dropdown_list') 
    file_curr_student= request.args.get('dropdown_list1')
    file=session['file']
    courses=[]
    if ((file_curr_student==None  or file_curr_student=='Seçiniz..') and(file_curr==None or file_curr=='Seçiniz..') ):
        file_curr_student="student.csv"
        file_curr="grade2.csv"
        courses=course_list(file_curr)
    elif  file_curr != None:
        filenew = file_curr        
        courses=course_list(filenew) 

    name=request.args.get('clicked')
    algorithm="svm"
    predict_function=request.args.get('prediction_function')
    temp1=[]
    temp2=[]
    global model,info,parameters,predict_f
    coursename=request.args.get('course')
    if(predict_function!='Select..'):
        if(predict_function=='Course Grade Prediction'):
            temp1="course"
            predict_f="course_grade"
        elif(predict_function=='Dropout for a Student'):
            temp1="c"
            predict_f="dropout" 
    select = request.args.getlist('ıteratıon')
    if(name=='CreateModel'):
        temp2="button"
        if(select[0]!= ""):
            select[0]=float(select[0])
        if(select[1] != ""):
            select[1]=int(select[1])
        if(predict_f=="course_grade"):
            session['coursename']=coursename
            model,info,parameters=a.create_new_model(file_curr,file_curr_student,predict_f, algorithm, select, coursename.lower(), None)       
        else:  
            model,info,parameters=a.create_new_model(file_curr,file_curr_student,predict_f, algorithm, select, None, None)
        return render_template('SupportVectorMachıne.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=parameters,info=info,temp=coursename,temp1=temp1,temp2=temp2) 

    elif(name=='SaveModel'):
        temp2="s"
        isdef=1
        if check_box==None:
            isdef=0
        if(predict_f=="course_grade"):
            coursename=session['coursename']
            a.save_model(file_curr,file_curr_student,predict_f, algorithm, parameters,info,model,isdef,coursename.lower(),None)    
        else:
            a.save_model(file_curr,file_curr_student,predict_f, algorithm, parameters,info,model,isdef,None,None)
    

    return render_template('SupportVectorMachıne.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=[],info=[],temp=coursename,temp1=temp1,temp2=temp2)


@app.route('/LınearRegressıon')
def LınearRegressıon():
    check_box=request.args.get('check_box')
    algorithm="linear"
    file_curr=[]
    temp1="course"
    file_curr  = request.args.get('dropdown_list') 
    file_curr_student= request.args.get('dropdown_list1')
    file=session['file']
    courses=[]
    temp2=[]
    global model,info,parameters,predict_f
    if ((file_curr_student==None  or file_curr_student=='Seçiniz..') and(file_curr==None or file_curr=='Seçiniz..') ):
        file_curr_student="student.csv"
        file_curr="grade2.csv"
        courses=course_list(file_curr)
    elif  file_curr != None:
        filenew = file_curr        
        courses=course_list(filenew)
    predict_function=request.args.get('prediction_function')
    if(predict_function!='Select..'):
        if(predict_function=='GPA Prediction'):
            predict_f="gpa"
        elif(predict_function=='Length of Study Prediction'):
            predict_f="study_length"
    coursename=request.args.get('course')
    if(coursename=='Select..'):
        temp1="c"
        select = request.args.getlist('ıteratıon')
    else:
        select = request.args.getlist('ıteratıon')
    name=request.args.get('clicked')
    if(name=='CreateModel'):
        temp2="button"
        model,info,parameters=a.create_new_model(file_curr,file_curr_student,predict_f, algorithm, select, None, None)
        return render_template('LınearRegressıon.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=parameters,info=info,temp=coursename,temp1=temp1,temp2=temp2) 

    elif(name=='SaveModel'):
        temp2="s"
        isdef=0
        if check_box=='Default':
            isdef=1
        if model!=None:
            print(info)
            a.save_model(file_curr,file_curr_student,predict_f, algorithm, parameters, info, model ,isdef, None, None)
    return render_template('LınearRegressıon.html',courses=courses,tree=make_tree(path),tree1=make_tree(pathsstudent),parameters=[],info=[],temp=coursename,temp1=temp1,temp2=temp2)
     

# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])

    user_type = SelectField('User Type', choices = [("Rector", "Rector"),("Department Head", "Department Head"), ("Faculty Head", "Faculty Head"),
                                                        ("Student", "Student"), ("Teacher", "Teacher")])#choices=[('Student', 'Student'), ('Teacher', 'Python'),  ('University Head', 'Plain Text'), ('Department Head', 'Plain Text'), ('Faculty Head', 'Plain Text')])
    #user_type = SelectField('User Type', [validators.Length(min=6, max=50)])
    confirm = PasswordField('Confirm Password')



# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        user_type = (str(form.user_type.data))
        user_kinds = ["Rector", "Department Head", "Faculty Head", "Student", "Teacher"]
        idx = user_kinds.index(user_type)
        #print (idx)
        #print (type(idx))
        # Create cursor
        
        cur = mysql.connection.cursor()
        cur.execute("use %s" % (db_name_deneme))
        cmd = "INSERT INTO users (name, email, username, password,user_type, is_approved) VALUES(\"%s\", \"%s\", \"%s\",\"%s\", %d, 0)" % (name, email, username, password, idx)
        if run_cmd(cur, cmd, "Couldn't add user.") != -1:
            print ("Added user.")
            # cmd = "SELECT * FROM users WHERE username = \"%s\"" % (username)
            # if run_cmd(cur, cmd, "Couldn't get user id.") != -1:
            #     data = cur.fetchone()            
            #     user_id = data[0]["user_id"]
            #     print ("User id is: %s" % user_id)
            #     hash = sha256_crypt.encrypt(user_id)
            #     link = "http://localhost:5000/approve?hash_val=%s" % (hash)
            #     approve_sent = "Hello. User %s with name %s and email %s is registered to the system. Please click on the following link to confirm:\n %s"  % (username, name, email, link)   
            #     msg = Message(approve_sent,
            #         sender="gpapredict.123@gmail.com",
            #         recipients=[rector_mail])

            
            #     mail.send(msg)




            # msg = MIMEText("Mail deneme".)
            # # me == the sender's email address
            # # you == the recipient's email address
            # msg['Subject'] = 'The contents of %s' % textfile
            # msg['From'] = "gpapredict.123@gmail.com"
            # msg['To'] = "meltemdasdemir94@gmail.com"
            # # Send the message via our own SMTP server, but don't include the
            # # envelope header.
            # s = smtplib.SMTP('localhost')
            # s.sendmail(me, [you], msg.as_string())
            # s.quit()
            # recipients=["talhakaradeniz@gmail.com"]
            # msg = Message("Hi.",
            #      sender="talhakaradeniz@localhost",
            #      recipients=recipients)
            # mail.send(msg)


        # Execute query
        #print(cmd)
        #cur.execute(cmd)



        # Commit to DB
        mysql.connection.commit()

        # Close connection
        #cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']
        
      

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        cur.execute("use %s" % (db_name_deneme))     
        cmd = "SELECT * FROM users WHERE username = '%s'" % (username)
        result = cur.execute(cmd)

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            
            password = data['password']
            #print (password)
            #print(password_candidate)
            # Compare Passwords
            hash = sha256_crypt.encrypt(password_candidate)
            #print(hash)
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['username'] = username
                #session['data1']=data
                session['user_id']=data['user_id']
                return redirect_login(data)                



            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            #cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout



@app.route('/PredıctıonsHomePage')
def PredıctıonsHomePage():
    return render_template('PredıctıonsHomePage.html')

@app.route('/DepartmentHomePage', methods=['GET', 'POST'])
def DepartmentHomePage():
    
    return render_template('DepartmentHomePage.html') 
@app.route('/KursRaporlamaHome', methods=['GET', 'POST'])
def KursRaporlamaHome():
    
    return render_template('KursRaporlamaHome.html')   
@app.route('/OgrencıRaporHome', methods=['GET', 'POST'])
def OgrencıRaporHome():

    return render_template('OgrencıRaporHome.html')
@app.route('/OgrencıHomePage', methods=['GET', 'POST'])
def OgrencıHomePage():
    
    return render_template('OgrencıHomePage.html')  



@app.route('/RaporHomepage', methods=['GET', 'POST'])
def RaporHomepage():
    
    return render_template('RaporHomepage.html')  


@app.route('/HeadHomepage', methods=['GET', 'POST'])
def HeadHomepage():
    session['file'] = request.args.get('dropdown_list')
    session['filenew']=session['file']
    return render_template('HeadHomepage.html')  

@app.route('/ProfessorHomepage', methods=['GET', 'POST'])
def ProfessorHomepage():
    
    return render_template('ProfessorHomepage.html')  


@app.route('/HeadPrediction', methods=['GET', 'POST'])
def HeadPrediction():
    
    return render_template('HeadPrediction.html')  

@app.route('/LengthPrediction', methods=['GET', 'POST'])
def LengthPrediction():
    as_dict = request.args.getlist('educationDate')
    as_dict1 = request.args.getlist('CourseName')
    print(as_dict)
    print(as_dict1)
    num=a.predict_length(as_dict,as_dict1)
    return render_template('LengthPrediction.html',num=num) 

@app.route('/CriticalDropout', methods=['GET', 'POST'])
def CriticalDropout():
    user_id=session['user_id']
    cur = mysql.connection.cursor()
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s AND isDeleted = %s ", ([user_id], 0))
    rows=[]
    num=[]
    grades=[]
    courses=[]
    if result1 > 0:
        data1=cur.fetchall()
        index=0
        rows=[]
        for i in range(len(data1)):
            row = dict(semesters=data1[index]["semester"],grades=data1[index]["grade"],courses=data1[index]["coursename"])
            rows.append(row)
            grades.append(data1[index]["grade"])
            courses.append(data1[index]["coursename"])
            index += 1

    num=a.predict_dropout(grades,courses)
    #print(num)
    if(num==False):
        num="You will not leave."
    else:
        num="Yes, probably you will leave."
    return render_template('CriticalDropout.html',num=num,rows=rows) 


@app.route('/OgrencıPredıctıons', methods=['GET', 'POST'])
def OgrencıPredıctıons():
    
    return render_template('OgrencıPredıctıons.html')  



@app.route("/OgrencıLength", methods=['GET', 'POST'])
def OgrencıLength():
    user_id=session['user_id']
    cur = mysql.connection.cursor()
    result1 = cur.execute("SELECT * FROM gpas WHERE user_id = %s AND isDeleted = %s ", ([user_id], 0))
    rows=[]
    num=[]
    grades=[]
    courses=[]
    if result1 > 0:
     
        data1=cur.fetchall()
        index=0
        rows=[]
        for i in range(len(data1)):
            row = dict(semesters=data1[index]["semester"],grades=data1[index]["grade"],courses=data1[index]["coursename"])
            rows.append(row)
            grades.append(data1[index]["grade"])
            courses.append(data1[index]["coursename"])
            index += 1


    num=a.predict_length(grades,courses)
    #print(num)
    return render_template('OgrencıLength.html',num=int(num),rows=rows)



@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

def redirect_login(data):
    session['logged_in'] = True

 
    if(data['user_type']==3):
        session['ogrencı_logged']=True
        flash('You are now logged in', 'success')
        return redirect(url_for('OgrencıHomePage'))
        #return render_template('OgrencıHomePage.html')
    elif(data['user_type']==0 or data['user_type']== 1 or data['user_type']==2 or data['user_type']==4):
        session['ogrencı_logged']=False
        flash('You are now logged in', 'success')

        return redirect(url_for('HeadHomepage'))


def run_cmd(cur, cmd, err_msg):
    try:
        result = cur.execute(cmd)
    except:
        print(err_msg)
        result = -1
    return result    
            
@app.route('/approve', methods=['GET', 'POST'])
def approve():
    id_hash = request.form['hash_val']
    cur = mysql.connection.cursor()
    cmd = "SELECT * FROM users"
    result =  run_cmd(cur, cmd, "Couldn't obtain users list.") 
    if result != -1:
        data = cur.fetchall()        
        for i in range(len(users)):
            user_id =  data[i]["user_id"] 
            hash_user_id = sha256_crypt.encrypt(password_candidate)
            #print(hash)
            if sha256_crypt.verify(id_hash, hash_user_id):
                print ("User id: %d" % user_id)
                break


    #    password_candidate = request.form['password']    

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)


