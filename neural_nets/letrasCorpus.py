import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras import optimizers
from keras import metrics
from keras.optimizers import SGD


#formula from 
# https://datascience.stackexchange.com/questions/14415/how-does-keras-calculate-accuracy
import keras.backend as K

def get_categorical_accuracy_keras(y_true, y_pred):
    return K.mean(K.equal(K.argmax(y_true, axis=1), K.argmax(y_pred, axis=1)))

letraI = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
letraT = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
letraN = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
letraO = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
letraZ = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
letraL = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
letraJ = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
letraE = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
letraP = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
letraQ = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

Inputs = [
			letraI,
			letraT,
			letraN,
			letraO,
			letraZ,
			letraL,
			letraJ,
			letraE,
			letraP,
			letraQ,
			]

Targets = [
			[0,0,0,0,0,0,0,0,0,1],
			[0,0,0,0,0,0,0,0,1,0],
			[0,0,0,0,0,0,0,1,0,0],
			[0,0,0,0,0,0,1,0,0,0],
			[0,0,0,0,0,1,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
			[0,0,0,1,0,0,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0],
			[1,0,0,0,0,0,0,0,0,0],
			]



Inputs = np.asarray(Inputs)


Targets = np.asarray(Targets)

model = Sequential([
    keras.layers.Dense(81, activation=tf.nn.sigmoid, input_dim=81),
    keras.layers.Dense(64, activation=tf.nn.sigmoid),
    keras.layers.Dense(32, activation=tf.nn.sigmoid),
    keras.layers.Dense(10, activation=tf.nn.sigmoid) ])

sgd = optimizers.SGD(lr=0.4, decay=1e-6, momentum=0.7, nesterov=True)
model.compile(optimizer=sgd, 
              loss='mean_squared_error',
              metrics=[get_categorical_accuracy_keras])

history = model.fit(Inputs, Targets, epochs=5000)


test = np.asarray(Inputs)
predictions = model.predict(test)


print("Estimaciones = ")
print(predictions)
print(np.round(predictions, 2))

