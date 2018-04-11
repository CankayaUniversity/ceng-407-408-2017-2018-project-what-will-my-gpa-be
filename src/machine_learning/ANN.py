
## Sergen ISPIR

from sklearn.neural_network import MLPClassifier

class MultilayerPerceptron:
        def __init__(self, x, y):
                self.x = x
                self.y = y                
        def train(self, activ, solv, alph, batch, l_rate_init, m_iter):
                self.mlp = MLPClassifier(activation=activ, solver=solv, alpha = alph, batch_size = batch,
                    learning_rate_init=l_rate_init, max_iter=m_iter)
                self.mlp.fit(self.x,self.y)
        def getSummary(self):
                print("Accuracy: ", self.mlp.score(self.x,self.y))
                print("Loss:", self.mlp.loss_)
