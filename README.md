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
