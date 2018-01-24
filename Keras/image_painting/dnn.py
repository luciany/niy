# Image painting using Keras
# https://cs.stanford.edu/people/karpathy/convnetjs/demo/image_regression.html

import os, time, sys, random
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import keras
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import RMSprop,SGD,Adam
from keras.layers.advanced_activations import PReLU
from keras.layers import MaxoutDense
from keras.layers.normalization import BatchNormalization
print(keras.__version__)

# filename = r"files/chess.png"
# filename = r"files/rhombus.png"
# filename = r"files/word.png"
# filename = r"files/line.png"
# filename = r"files/noise.png"
filename = r"files/man.png"

img = Image.open(filename)
img_array = np.array(img)

XSIZE = img_array.shape[0]
YSIZE = img_array.shape[1]

X = np.zeros((XSIZE * YSIZE, 2)).astype('float32')
Y = np.zeros((XSIZE * YSIZE, 3)).astype('float32')
n = 0
for i in range(0, XSIZE):
	for j in range(0, YSIZE):
		X[n][0] = (i - XSIZE // 2) / (XSIZE // 2)
		X[n][1] = (j - YSIZE // 2) / (YSIZE // 2)
		Y[n][0] = img_array[i][j][0]
		Y[n][1] = img_array[i][j][1]
		Y[n][2] = img_array[i][j][2]
		n += 1

if (Y.max() - Y.min()) <= 2:
	Y *= 255.0
Y = Y / 255.0 - 0.5
# Y = Y / 255.0

# activation = Activation('relu')
activation = PReLU()
model = Sequential()
model.add(Dense(8, input_dim=2))
model.add(activation)
model.add(Dense(8))
model.add(activation)
model.add(Dense(8))
model.add(activation)
model.add(Dense(8))
model.add(activation)
model.add(Dense(8))
model.add(activation)
model.add(Dense(3))

# model.add(BatchNormalization())

# optimizer = SGD(lr=0.01, momentum=0.9)
# optimizer = RMSprop()
optimizer = Adam()
model.compile(optimizer=optimizer,
	          loss='mse',
	          metrics=['mae'])

def adj(c):
	c += 0.5
	c *= 255.0
	c = round(c)
	if c < 0: c = 0
	if c > 255: c = 255
	return np.uint8(c)

for i in range(0, 20):
	model.fit(X, Y, 
		epochs=2, 
		batch_size=32,
		verbose=2)
	
	Z = model.predict(X)
	n = 0
	for i in range(0, XSIZE):
		for j in range(0, YSIZE):
			img_array[i][j][0] = adj(Z[n][0])
			img_array[i][j][1] = adj(Z[n][1])
			img_array[i][j][2] = adj(Z[n][2])
			n += 1

	img_new = Image.fromarray(img_array)
	img_new.save("_img.bmp")
