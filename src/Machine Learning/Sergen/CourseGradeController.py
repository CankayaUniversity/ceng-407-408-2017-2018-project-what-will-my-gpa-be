
## Sergen ISPIR

from Tables import *
from Logistic import *
from ANN import *
from sklearn.model_selection import KFold



## data preparation
c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
x = courseTable[:]
course_name = 'ceng241'
courseList = [i.lower() for i in courseList]
class_index = courseList.index('ceng241')
y = x[:,class_index] ## class label
x = np.delete(x,class_index,1) ## remove class column from input data

## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
for i in range(y.size):
        index = c.index(y[i])
        y[i] = index
        
## parameters
tolerance = 0.001 ##this value defines tolerance for stopping criteria.
iteration = 10000 ## number of max iteration
solv = "lbfgs" ##optimization algorithm

## kfold for testing and validation
kf = KFold(n_splits=10, shuffle=True)
for train_index, test_index in kf.split(x):
##        print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
lr = LogisticRegression(x, y)
lr.train(tolerance,iteration,solv)
lr.getAccuracy()
lr.getLoss()

######################################
## parameters
activ = 'logistic'
solv = 'lbfgs' ##optimizer
alph = 0.003 ## for regularization
batch = 100
l_rate_init = 0.001
m_iter = 1000 ## maximum iteration

## MLP model
mlp = MultilayerPerceptron(x, y)
mlp.train(activ,solv,alph,batch,l_rate_init,m_iter)
mlp.getSummary()
########################################
