# example code from page: 
pyhton
import tensorflow as tf

# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
  sess.run(train, {x: x_train, y: y_train})

# evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

### output should look as below, except every line is preceeded with
# '#' so that one can run this entire file as a script.

#Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
#[GCC 5.4.0 20160609] on linux2
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import tensorflow as tf
#>>> 
#>>> # Model parameters
#... W = tf.Variable([.3], dtype=tf.float32)
#>>> b = tf.Variable([-.3], dtype=tf.float32)
#>>> # Model input and output
#... x = tf.placeholder(tf.float32)
#>>> linear_model = W * x + b
#>>> y = tf.placeholder(tf.float32)
#>>> 
#>>> # loss
#... loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
#>>> # optimizer
#... optimizer = tf.train.GradientDescentOptimizer(0.01)
#>>> train = optimizer.minimize(loss)
#>>> 
#>>> # training data
#... x_train = [1, 2, 3, 4]
#>>> y_train = [0, -1, -2, -3]
#>>> # training loop
#... init = tf.global_variables_initializer()
#>>> sess = tf.Session()
#2017-09-12 16:04:15.335370: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
#2017-09-12 16:04:15.335409: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
#2017-09-12 16:04:15.335421: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
#2017-09-12 16:04:15.669806: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:893] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
#2017-09-12 16:04:15.670034: I tensorflow/core/common_runtime/gpu/gpu_device.cc:955] Found device 0 with properties: 
#name: GRID K520
#major: 3 minor: 0 memoryClockRate (GHz) 0.797
#pciBusID 0000:00:03.0
#Total memory: 3.94GiB
#Free memory: 3.90GiB
#2017-09-12 16:04:15.670064: I tensorflow/core/common_runtime/gpu/gpu_device.cc:976] DMA: 0 
#2017-09-12 16:04:15.670080: I tensorflow/core/common_runtime/gpu/gpu_device.cc:986] 0:   Y 
#2017-09-12 16:04:15.670099: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GRID K520, pci bus id: 0000:00:03.0)
#>>> sess.run(init) # reset values to wrong
#>>> for i in range(1000):
#...   sess.run(train, {x: x_train, y: y_train})
#... 
#>>> # evaluate training accuracy
#... curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
#>>> print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
#W: [-0.9999969] b: [ 0.99999082] loss: 5.69997e-11
#>>> 
