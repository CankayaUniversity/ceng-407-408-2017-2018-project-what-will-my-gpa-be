from flask import Markup
from flask import Flask, request, url_for, redirect, flash
import csv
import pandas as pd
from flask import render_template
from Grad_year import fin_grad_year
from VectorCourseYear import *
from DropoutYear import *
from PassFailRate import *
from StudentSemester import *
from UniqueCourses import *
from DeparmentSuccessElective import *
from DepartmentSuccess import *


app = Flask(__name__) 
colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
@app.route("/")
def Homepage():
    return render_template('Homepage.html')

@app.route('/KursRaporlama', methods=['GET', 'POST'])
def KursRaporlama():
    #if request.method == 'POST':
    #select = request.form.get('comp_select')
    #print(select)
    select = request.args.get('comp_select')
    #print(request.args)
    values,labels=get_course_avg(str(select))
    courses=course_list()
    #return str(select)
    return render_template('KursRaporlama.html', set=zip(values, labels, colors), courses=courses, values=values,labels=labels )





@app.route('/OgrencıKurs', methods=['GET', 'POST'])
def OgrencıKurs():
	ıd=request.args.get('text')
	select = request.args.get('comp')
	labels,values=get_semester_success(int(ıd),select)
	return render_template('/OgrencıKurs.html', set=zip(values, labels, colors), values=values, labels=labels )




@app.route('/BolumSecmelı', methods=['GET', 'POST'])
def BolumSecmelı():
	ıd=request.args.get('elec')
	select = request.args.get('comp')
	labels,values=getsuccess(str(select),str(ıd))
	
	return render_template('/BolumSecmelı.html', set=zip(values, labels, colors), values=values, labels=labels )

 
@app.route('/Bolum', methods=['GET', 'POST'])
def Bolum():
	
	select = request.args.get('comp')
	labels,values=get_dep_success(select)
	return render_template('/Bolum.html', set=zip(values, labels, colors), values=values, labels=labels ) 	


@app.route('/KursRaporlamaOnce', methods=['GET', 'POST'])
def KursRaporlamaOnce():
    courses=course_list()

    return render_template('KursRaporlamaOnce.html',courses=courses)


@app.route('/OgrencıDonemOnce', methods=['GET', 'POST'])
def OgrencıDonemOnce():

   	return render_template('OgrencıDonemOnce.html')

def empty(value):
   try:
       value = float(value)
   except ValueError:
       pass
   return bool(value)

@app.route('/OgrencıDonem', methods=['GET', 'POST'])

def OgrencıDonem():
	#dosyaad=request.args.get['file']		
	ıd=request.args.get('text')
	labels,values=get_semester_ıd(int(ıd))
	##if labels!=0:
	return render_template('OgrencıDonem.html', set=zip(values, labels, colors), values=values,labels=labels)
	#else:
		#{"error": "parameter age: positive integer required"}		
		#return render_template('OgrencıDonemOnce.html')


@app.route('/KalmaGecmeOnce', methods=['GET', 'POST'])
def KalmaGecmeOnce():
    #if request.method == 'POST':
    #session['table_id'] = request.args.get('comp_select')
    #print(session['table_id'])
    #values,labels=get_course_avg(select)
    courses=course_list()
    

    return render_template('KalmaGecmeOnce.html',courses=courses)

@app.route('/KalmaGecme', methods=['GET', 'POST'])
def KalmaGecme():

    select = request.args.get('comp_select')
    values,values1,labels=get_pass_val(str(select))
    courses=course_list()
    return render_template('KalmaGecme.html',courses=courses,values=values,labels=labels,values1=values1)


@app.route('/OgrencıRaporHome', methods=['GET', 'POST'])
def OgrencıRaporHome():

    return render_template('OgrencıRaporHome.html')




@app.route('/OgrencıKursOnce', methods=['GET', 'POST'])
def OgrencıKursOnce():
 
    courses=course_listt()
    return render_template('OgrencıKursOnce.html',courses=courses)

@app.route('/BolumOnce', methods=['GET', 'POST'])
def BolumOnce():

    courses=course_listt()
    return render_template('BolumOnce.html',courses=courses)


@app.route('/BolumSecmelıOnce', methods=['GET', 'POST'])
def BolumSecmelıOnce():

    courses=course_listt()
    return render_template('BolumSecmelıOnce.html',courses=courses)



@app.route('/foo', methods=['GET', 'POST'])
def foo():
    #if request.method == 'POST':
    #select = request.form.get('comp_select')
    #print(select)
    select = request.args.get('a')
    print (request.args)
    print (select)
    return str(select)

@app.route('/KursBırakma', methods=['GET', 'POST'])
def KursBırakma():
    
    labels,values=fin_drop_year()
    return render_template('KursBırakma.html', set=zip(values, labels, colors), values=values,labels=labels )


@app.route('/YeniRaporlama', methods=['GET', 'POST'])
def YeniRaporlama():
    
    labels,values=fin_drop_year()
    return render_template('YeniRaporlama.html', set=zip(values, labels, colors), values=values,labels=labels )

@app.route('/Raporlama', methods=['GET', 'POST'])
def Raporlama():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Homepage'))

    # show the form, it wasn't submitted
    
    labels,values=fin_grad_year()
    return render_template('Raporlama.html', set=zip(values, labels, colors), values=values,labels=labels )







 
if __name__ == "__main__":
    app.run()