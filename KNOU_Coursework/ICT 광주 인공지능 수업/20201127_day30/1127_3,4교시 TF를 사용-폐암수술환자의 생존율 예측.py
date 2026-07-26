#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[2]:


#step1. 데이터 로드& 변수에 할당.
Data_set = np.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201127_day30/ThoraricSurgery.csv",delimiter=",")

x_data = Data_set[:,0:17]
#Data_set
y_data = Data_set[:,[17]]
#y_data 


# In[3]:


X = tf.placeholder(tf.float32, [None, 17])
Y = tf.placeholder(tf.float32, [None, 1])


# In[4]:


#히든레이어는 1개이고 
#x값은 17개, 히든레이어의 노드는 30개이다.

#layer1 : 보내는쪽(입력층x1,x2)->은닉층1
W1 = tf.Variable(tf.random_normal([17,30], name='weight1'))#x값은 17개, 히든레이어의 노드는 30개이다.
b1 = tf.Variable(tf.random_normal([30]),name='bias1' )
#layer2 : 보내는쪽(은닉층3)->출력층y(y층은 1개 노드만 있는 것으로실시)
W2 = tf.Variable(tf.random_normal([30,1], name='weight2'))
b2 = tf.Variable(tf.random_normal([1]),name='bias2' )


# In[5]:


layer1 = tf.sigmoid(tf.matmul(X,W1) +b1)


# In[6]:


hypothesis = tf.sigmoid(tf.matmul(layer1, W2) +b2)


# In[7]:


cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis) )
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32 )
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32 ))


# In[8]:


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(10001):
        sess.run(train, feed_dict={X: x_data, Y:y_data})
        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y:y_data }) , sess.run(W2) )
            
    h,c,a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
    print("\n Hypothesis: \n", h, "\nCorrect : \n", c, "\nAccuracy : \n", a )


# In[ ]:





# In[9]:





# In[ ]:




