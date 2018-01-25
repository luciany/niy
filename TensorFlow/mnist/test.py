import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import gzip, struct
import numpy as np
import matplotlib.pyplot as plt

def get_sample_in(filename):
	with gzip.open(filename , 'rb') as file:
		buf = file.read()
	 
	index = 0

	form = '>IIII'
	magic, numImages, numRows, numColumns = struct.unpack_from(form, buf, index)
	index += struct.calcsize(form)

	print("get_sample_in", filename)
	samples = []
	for i in range(numImages):
		form = '>784B'
		im_data = struct.unpack_from(form, buf, index)
		index += struct.calcsize(form)

		arr = np.array(im_data).astype("float32")
		arr = (arr - 128.0) / 128.0 
		samples.append(arr)

	return np.array(samples)

def get_sample_out(filename):
	with gzip.open(filename , 'rb') as file:
		buf = file.read()

	index = 0
	form = '>II'
	magic, numItems = struct.unpack_from(form, buf, index)
	index += struct.calcsize(form)

	print("get_sample_out", filename)
	samples = []
	for i in range(numItems):
		form = '>1B'
		label_data = struct.unpack_from(form, buf, index)
		index += struct.calcsize(form)

		arr = np.zeros((10,)).astype("float32")
		arr[label_data] = 1
		samples.append(arr)

	return np.array(samples)

train_in = get_sample_in('files/train-images-idx3-ubyte.gz')
test_in = get_sample_in('files/t10k-images-idx3-ubyte.gz')
train_out = get_sample_out('files/train-labels-idx1-ubyte.gz')
test_out = get_sample_out('files/t10k-labels-idx1-ubyte.gz')

print(train_in.shape, train_out.shape)
# os._exit(0)

sess = tf.Session()

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
# b = tf.Variable(tf.zeros([1,10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# test = tf.reduce_sum(tf.ones([2, 3, 4]), reduction_indices=[1])
# print(sess.run(test))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

sess.run(tf.global_variables_initializer())

i = 0
batch_size = 100
epoch = 0
while True:
	batch_xs, batch_ys = train_in[i:i+batch_size,:], train_out[i:i+batch_size,:]
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
	i += batch_size
	if i > len(train_in): 
		i = 0
		epoch += 1
		print("Epoch", epoch)
		correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		print("    test accuracy", sess.run(accuracy, feed_dict={x: test_in, y_: test_out}))

	if epoch >= 100: break

