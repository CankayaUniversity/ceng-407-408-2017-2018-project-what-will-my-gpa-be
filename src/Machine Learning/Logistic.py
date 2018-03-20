from Data import data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
x = data[:,:-1] ## take all data expect graduation gpa column
y = x[:,-1] ## class label

## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
for i in range(y.size):
	index = c.index(y[i])
	y[i] = index

logistic = linear_model.LogisticRegression() ## create a logistic regression model

#define model parameters
error_rate = 0.001 ##this value defines tolerance for stopping criteria.
iteration = 1000 ## number of max iteration
solver = "lbfgs" ##optimization algorithm


