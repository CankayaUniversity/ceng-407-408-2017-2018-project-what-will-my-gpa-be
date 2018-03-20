from Data import data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
x = data[:,:-1] ## take all data expect graduation gpa column
y = x[:,-1] ## class label
x = np.delete(x,-1,1) ## remove class column from input data

## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
for i in range(y.size):
	index = c.index(y[i])
	y[i] = index

##parameters
activ = 'logistic'
solv = 'lbfgs' ##optimizer
alph = 0.003 ## for regularization
batch = 100
l_rate_init = 0.001
m_iter = 1000 ## maximum iteration
shuffl = True ##shuffle data?


##create model
mlp = MLPClassifier(activation=activ, solver=solv, alpha = alph, batch_size = batch,
                    learning_rate_init=l_rate_init, max_iter=1000, shuffle=shuffl)
mlp.fit(x,y)

