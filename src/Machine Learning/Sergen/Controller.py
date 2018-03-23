from Tables import *
from Logistic import *

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


#define model parameters
tolerance = 0.0001 ##this value defines tolerance for stopping criteria.
iteration = 1000 ## number of max iteration
solv = "lbfgs" ##optimization algorithm

lr = LogisticRegression(x,y)
lr.train(tolerance,iteration,solv)
lr.getAccuracy()
