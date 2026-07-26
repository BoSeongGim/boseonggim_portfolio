#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[2]:


learning_rate=0.1
tf.set_random_seed(0)
np.random.seed(0)


# In[3]:


x_data=[[0,0], [0,1], [1,0], [1,1] ]
y_data=[[0], [1], [1], [0] ]


# In[4]:


X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 1])


# In[5]:


W1 = tf.Variable(tf.random_normal([2,5], name='weight1'))
b1 = tf.Variable(tf.random_normal([5]),name='bias1' )


# In[6]:


layer1 = tf.sigmoid(tf.matmul(X,W1) +b1)


# In[7]:


W2 = tf.Variable(tf.random_normal([5,1], name='weight2'))
b2 = tf.Variable(tf.random_normal([1]),name='bias2' )


# In[8]:


hypothesis = tf.sigmoid(tf.matmul(layer1, W2) +b2)


# In[9]:


cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis) )
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32 )
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32 ))


# In[10]:


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(10001):
        sess.run(train, feed_dict={X: x_data, Y:y_data})
        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y:y_data }) , sess.run(W2) )
            
    h,c,a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
    print("\n Hypothesis: \n", h, "\nCorrect : \n", c, "\nAccuracy : \n", a )


# In[ ]:





# In[ ]:




