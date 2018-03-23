from keras.models import Sequential
from keras.layers import Dense, Activation
from Data import data
import numpy as np

c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
x = data[:,:-1] ## take all data expect graduation gpa column
y = x[:,-1] ## class label
x = np.delete(x,-1,1) ## remove class column from input data

## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
for i in range(y.size):
	index = c.index(y[i])
	y[i] = index


##Simple 2 layers Neural network
model = Sequential()
model.add(Dense(32, activision='relu'), input_dim=109)
model.add(Dense(1, activision='sigmoid'), input_dim=109)
model.compile(optimizer = 'rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=100, batch_size=32)
