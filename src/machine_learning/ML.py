
from sklearn import linear_model, svm, neural_network
from sklearn.metrics import log_loss, mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

def logistic_regression(x,y):
    model = linear_model.LogisticRegression()
    model.fit(x,y)
    print("Accuracy: %.2f" % model.score(x,y))
    print("Loss: %.2f" % log_loss(y, model.predict_proba(x)))
    return model

def linear_regression(x,y):
    model = linear_model.LinearRegression()
    model.fit(x,y)
    print("Accuracy: %.2f" % model.score(x,y))
    print("Loss: %.2f" % mean_squared_error(y, model.predict(x)))
    return model

def svm(x,y):
    model = svm.SVC()
    model.fit(x,y)
    print("Accuracy: %.2f" % model.score(x,y))
    return model

def mlp(x,y):
    model = neural_network.MLPClassifier()
    model.fit(x,y)
    print("Accuracy: %.2f", model.score(x,y))
    print("Loss: %.2f", model.loss_)
    return model

def rnn(x,y):
    model = Sequential()
    model.add(LSTM(4, input_shape=(1, 119)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x, y, epochs=100, batch_size=1, verbose=2)
    return model
