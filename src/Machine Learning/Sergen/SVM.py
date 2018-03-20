from Data import data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
x = data[:,:-1] ## take all data expect graduation gpa column
y = x[:,-1] ## class label
x = np.delete(x,-1,1) ## remove class column from input data

## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
for i in range(y.size):
	index = c.index(y[i])
	y[i] = index

model = svm.SVC(decision_function_shape='ovo') ## create SVM model
model.fit(x,y) ##train data
