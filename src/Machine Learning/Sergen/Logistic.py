from Tables import courseTable
import numpy as np
from sklearn import linear_model


class LogisticRegression:
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def train(self, tolerance, iteration, solver):
                self.logistic = linear_model.LogisticRegression(max_iter = iteration, solver = solver, tol=tolerance) ## create a logistic regression model
                self.logistic.fit(self.x,self.y)
        def getAccuracy(self):
                print("Accuracy: ", self.logistic.score(self.x,self.y))
        def getLoss(self):
                pass



