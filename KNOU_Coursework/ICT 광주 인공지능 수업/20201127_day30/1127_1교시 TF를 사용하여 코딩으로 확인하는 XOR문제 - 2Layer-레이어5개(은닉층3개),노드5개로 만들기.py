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


#layer1 : 보내는쪽(입력층x1,x2)->은닉층1
W1 = tf.Variable(tf.random_normal([2,5], name='weight1'))
b1 = tf.Variable(tf.random_normal([5]),name='bias1' )


# In[6]:


layer1 = tf.sigmoid(tf.matmul(X,W1) +b1)


# In[7]:


#layer2 : 보내는쪽(은닉층1)->은닉층2
W2 = tf.Variable(tf.random_normal([5,5], name='weight2'))
b2 = tf.Variable(tf.random_normal([5]),name='bias2' )


# In[8]:


layer2 = tf.sigmoid(tf.matmul(X,W1) +b2)


# In[9]:


#layer3 : 보내는쪽(은닉층2)->은닉층3
W3 = tf.Variable(tf.random_normal([5,5], name='weight3'))
b3 = tf.Variable(tf.random_normal([5]),name='bias3' )


# In[10]:


layer3 = tf.sigmoid(tf.matmul(X,W1) +b3)


# In[11]:


#layer4 : 보내는쪽(은닉층2)->은닉층3
W4 = tf.Variable(tf.random_normal([5,5], name='weight4'))
b4 = tf.Variable(tf.random_normal([5]),name='bias4' )


# In[12]:


layer4 = tf.sigmoid(tf.matmul(X,W1) +b4)


# In[13]:


#layer5 : 보내는쪽(은닉층3)->출력층y(y층은 1개 노드만 있는 것으로실시)
W5 = tf.Variable(tf.random_normal([5,1], name='weight3'))
b5 = tf.Variable(tf.random_normal([1]),name='bias3' )


# In[14]:


layer3 = tf.sigmoid(tf.matmul(X,W1) +b5)


# In[15]:


hypothesis = tf.sigmoid(tf.matmul(layer1, W2) +b2)


# In[16]:


cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis) )
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32 )
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32 ))


# In[17]:


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




