#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[2]:


data = np.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201127_day30/ThoraricSurgery.csv",delimiter=",")

x_data = data[:,0:17]
y_data = data[:,[-1]]


# In[3]:


X = tf.placeholder(tf.float32, [None, 17])
Y = tf.placeholder(tf.float32, [None, 1])
learning_rate=0.1


# In[4]:


W1 = tf.Variable(tf.random_normal([17,30], name="weight1") )
b1 = tf.Variable(tf.random_normal([30]), name="bias1")

W2 = tf.Variable(tf.random_normal([30,1], name="weight2"))
b2 = tf.Variable(tf.random_normal([1]), name="bias2" )


# In[5]:


layer1 = tf.sigmoid(tf.matmul(X,W1)+b1)


# In[6]:


hypothesis = tf.sigmoid(tf.matmul(layer1, W2)+b2)

#cost = -tf.reduce_mean(Y*tf.log(hypothesis + (1-Y) * tf.log(1-hypothesis) ) )
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis) ) 
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#predicted = tf.cost(hypoehsis > 0.5, dtype = tf.float32)
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32 )
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))


# In[7]:


#스텝6 : 실제학습실시.
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer() )

    for step in range(10001) :
        sess.run(train, feed_dict= {X: x_data, Y: y_data})
        if step % 100 == 0 :
            print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data }), sess.run(W2) )
    
    h,c,a = sess.run([hypothesis, predicted,accuracy], feed_dict={X:x_data, Y:y_data} )
    print("\n Hypothesus : \n",h , "\n Correct : \n",c, "\n Accuracy : \n",a)
    
    


# In[8]:


with tf.Session as sess:
    sess.run(tf.global_variables_initializer() )
    
    for step in range(10001):
        sess.run(train, feed_dict = {X:x_data, Y:y_data})
        
        if step % 100 == 0:
           #print(step, sess.run(cost, feed_dict={X:x_data,Y:y_data}, sess.run(W2)))
            print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data }), sess.run(W2) )
            
    h,c,a = sess.run([hypothesis, predicted, accuracy], feed_dict= {X:x_data, Y:y_data})
    print("\n Hypothesus : \n",h , "\n Correct : \n",c, "\n Accuracy : \n",a)
    

