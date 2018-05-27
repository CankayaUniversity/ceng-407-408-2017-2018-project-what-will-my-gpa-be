# ceng-407-408-project-what-will-my-gpa-be

# Student Performance Evaluation System

* Efnan Gülkanat c1311021@student.cankaya.edu.tr

* Sergen İspir c1311026@student.cankaya.edu.tr

* Meltem Daşdemir c1311014@student.cankaya.edu.tr

Advisor: Prof. Dr. Erdoğan Doğdu

# **Installation and Compilation Guide**
We will describe how to install and compile the Student Performance Evaluation System project.

## **Prerequisites**

* Anaconda for Windows/ IOS should be installed.
* MySql should be installed and import to our dump file to your MySql;
	* mysql -u mysql_user -p DATABASE < Dump20180513.sql
	
* After dumping mysql, you should change mysql username and password in dbinfo.py. This file is in the [GPA.rar](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/releases) file.

* After installing Anaconda, you should install new Python libraries to your device.(These codes should be written in a Anaconda Prompt. All of these libraries are required, if they are not installed then you get some compilation errors.)
	* pip install numpy
	* pip install sklearn
	* pip install pandas
  * pip install flask
  * pip install os 
  * pip install WTForms
  * pip install functools
  * pip install flask_mysqldb
  * pip install passlib.hash


## **Compiling and Running**
* For running;
	* cd (path)/Desktop
  * cd GPA/myflaskapp
  * python app.py
 
After running project, you can access to program via [localhost](http://localhost/5000) or just type localhost/5000.


# USER MANUAL

We are going to show how to use system properly in this section. To get more information about Student Performance Evaluation System please click the link below before use the system.
* [Software Requirements Specification](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/wiki/Software-Requirements-Specification)
* [Software Design Document](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/wiki/Software-Design-Document)

## User Interface

We are going to start with show registration to use system.

### Register
You have to register before use and system provide for five type of user. Therefore, you have to choose which type you in during registration step.

![]()
*Figure 1 Register Page*

-------

### Login
After registration, you can login to system. Please be careful, each type of user provide different functionalities.

![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/login.png)
*Figure 2 Login Page*

-------

### Student Homepage
Homepage for students.

![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/student.PNG)
*Figure 3 Student Homepage*

-------

### Prediction Page
This page provide students to make prediction to learn predicted gpa, certain course grade, dropout or length of study. After click predict button in pages, predicted values will be displayed on below of the screen.

![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/gpa.PNG)
![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/kurs.PNG)
*Figure 4 Prediction pages*

-------

### Add Course Page
You can add any course and edit it whenever you want.

![]()
*Figure 5 Add course page*

-------

### Mutual Homepage
Homepage for professors, head of department, faculty and university.

![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/head.PNG)
*Figure 6 Mutual Homepage*

-------

### Add New Data File Page

![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/AddData.PNG)
*Figure 7 Add new data file page*

-------

### Create Model Page
This page includes four machine learning algorithm. After create a model and save it, students use that models for predictions.

![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/Createana.PNG)
*Figure 8 Create model page*

* #### Logistic regression
We are going to show how to create model with logistic regression. Other three algorithms use same steps.

There are two option here. Create model and save model. Save model button unclickable until you create a model. Every algorithm needs parameters. It doesn't matter whether you filled any parameter in textboxes. When they are empty, system use default parameters. After filling parameters, you should click the create model button. You will see successfuly created message top of the screen. Then save model button will become clickable. If you save model as default, students will use that model for predictions.

![](https://github.com/CankayaUniversity/ceng-407-408-project-what-will-my-gpa-be/blob/master/src/images/CREATE.PNG)
*Figure 9 Logistic regression page*

-------

### Report Page

![]()
*Figure 10 Report page*
