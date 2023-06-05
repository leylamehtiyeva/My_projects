import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.layers import Dense


"""
Celsius to Fahrenheit conversion
"""

# Training set

celsius = np.array([-40, -10, 0, 8, 15, 22, 38])
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100])

#  creates a multilayer neural network model
model = keras.Sequential()

#  first layers with 1 neuron (units), with one entrance (input_shape) and with linear activation function
model.add(Dense(units=1, input_shape=(1,), activation='linear'))

#  0.1 - gradient descent convergence step
#  when we compile we create a network with random initial weights
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

#  network training
history = model.fit(celsius, fahrenheit, epochs=500, verbose=False)

plt.plot(history.history['loss'])
plt.grid(True)
plt.show()

print(model.predict([100]))
print(model.get_weights())
