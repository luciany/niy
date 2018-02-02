import os
import numpy as np
import struct
import matplotlib.pyplot as plt

X_SIZE = 5
Y_SIZE = 1
N = 50000

np.random.seed(2018)

sample_in_bytes = bytearray()
sample_out_bytes = bytearray()
sample_in_head = np.zeros(8).astype("int32")
sample_out_head = np.zeros(8).astype("int32")

sample_in_head[1:4] = [1, 1, X_SIZE]
sample_out_head[1:4] = [1, 1, Y_SIZE]

sample_in_bytes += sample_in_head.tobytes()
sample_out_bytes += sample_out_head.tobytes()

X = np.random.rand(N, X_SIZE).astype("float32")

Y = 50*(X[:,0]**3) + 20*(X[:,1]**2) + 2*X[:,2] + 1*X[:,3] + 0*X[:,4]
Y = (Y - Y.min()) / (Y.max() - Y.min()) - 0.5
print(X.max(), X.min(), X.shape, Y.shape)

sample_in_bytes += X.tobytes()
sample_out_bytes += Y.tobytes()

with open("train_in.smpl", "wb") as file:
	file.write(sample_in_bytes)

with open("train_out.smpl", "wb") as file:
	file.write(sample_out_bytes)