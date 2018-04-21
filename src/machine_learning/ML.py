from sklearn import linear_model, neural_network
from sklearn.svm import LinearSVC
from sklearn.metrics import log_loss, mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import numpy as np

## 10fold splitting
kf = KFold(n_splits=10, shuffle=True)

def logistic_regression(x,y,p):
    ##create model
    model = linear_model.LogisticRegression()
    
    ##Train and test
    accuracy = [model.fit(x[train], y[train]).score(x[test],y[test]) for train, test in kf.split(x)]
    res = np.array(accuracy)

    print("\nLogistic Regression\n-----------------\nAccuracy: %.2f" % res.mean())
    print("Loss: %.2f" % log_loss(y, model.predict_proba(x)))
    
    return model

def linear_regression(x,y,p):
    ##create model
    model = linear_model.LinearRegression()

    model.fit(x,y)

    print("\nLinear Regression\n-----------------\nAccuracy: %.2f" % model.score(x,y))
    print("Loss: %.2f" % mean_squared_error(y, model.predict(x)))
    
    return model

def svm(x,y,p):
    ##create model
    model = LinearSVC()
    
    ##Train and test
    accuracy = [model.fit(x[train], y[train]).score(x[test],y[test]) for train, test in kf.split(x)]
    res = np.array(accuracy)

    print("\nSupport Vector Machine\n----------------------\nAccuracy: %.2f" % res.mean())
    
    return model

def mlp(x,y,p):
    ##create model
    model = neural_network.MLPClassifier(max_iter=1000)
    
    ##Train and test
    accuracy = [model.fit(x[train], y[train]).score(x[test],y[test]) for train, test in kf.split(x)]
    res = np.array(accuracy)
    
    print("\nMultilayer Perceptron\n-----------------\nAccuracy: %.2f" % res.mean())
    print("Loss: %.2f" % model.loss_)
    return model

def rnn(x,y):
    x = np.reshape(x, (x.shape[0],1,x.shape[1]))
    
    model = Sequential()
    model.add(LSTM(5, input_shape=(1, 117)))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x, y, epochs=200, batch_size=1, verbose=2)
    return model
