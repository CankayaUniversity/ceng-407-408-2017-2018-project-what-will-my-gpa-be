from sklearn import linear_model
from sklearn.metrics import log_loss

class LogisticRegression:
        
        def __init__(self):
                pass
                
        def train(self, tolerance, iteration, solver):
                self.logistic = linear_model.LogisticRegression(max_iter = iteration, solver = solver, tol=tolerance) ## create a logistic regression model
                self.logistic.fit(self.x,self.y)

        def getSummary(self):
                print("Accuracy: ", self.logistic.score(self.x,self.y))
                print("Loss:", log_loss(self.y, self.logistic.predict_proba(self.x)))

        def setData(self,x,y):
                self.x = x
                self.y = y
