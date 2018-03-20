from Data import data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
x = data[:,:-1] ## take all data expect graduation gpa column
y = x[:,-1] ## class label
x = np.delete(x,-1,1) ## remove class column from input data

## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
for i in range(y.size):
	index = c.index(y[i])
	y[i] = index

#define model parameters
tolerance = 0.0001 ##this value defines tolerance for stopping criteria.
iteration = 1000 ## number of max iteration
solv = "lbfgs" ##optimization algorithm

logistic = linear_model.LogisticRegression(max_iter = iteration, solver = solv, tol=tolerance) ## create a logistic regression model

logistic.fit(x,y)

print(logistic.get_params())
print("Accuracy: ", logistic.score(x,y))      
