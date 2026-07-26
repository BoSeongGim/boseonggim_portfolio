#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[2]:


#step1. 데이터 로드& 변수에 할당.
data = np.loadtxt("C:/Users/GimBoSeong/OneDrive/문서/DataScience/ICT/Py_Project/20201124_day27/data-03-diabetes.csv",delimiter=",")

x_data = data[:,0:-1]
y_data = data[:,[-1]]


# In[3]:


X = tf.placeholder(tf.float32, shape=[None, 8])
Y = tf.placeholder(tf.float32, shape=[None, 1])


# In[4]:


#기울기 a와 바이어스 b의 값을 임의로 정함. a는 [2,1] 형태를 가지며 a1,a2이다.
W = tf.Variable(tf.random_uniform([8,1]) )
#[2,1] 의미 : 들어오는 값은 2개, 나가는 값은 1개(tf.random_uniform([2,1])
b = tf.Variable(tf.random_uniform([1]) )


# In[5]:


#y 시그모이드 함수의 방정식을 세움.
hypthesis = tf.sigmoid(-(tf.matmul(X,W) +b ))


# In[6]:


cost = -tf.reduce_mean(Y * tf.log(hypthesis) + (1-Y) * tf.log(1-hypthesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


# In[7]:


predicted = tf.cast(hypthesis>0.5, dtype=tf.float32 ) #결과값 나오는 small Y이다#
accuracy  = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32 )) #계산하기 좋게 0,1으로 변경한다

#학습
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())

    for step in range(10000) :
        cost_val, _ = sess.run([cost,train], feed_dict={X:x_data, Y: y_data} ) 
        if step % 1000 == 0 :
            print("step=%d, cost_val=%.4f" % (step, cost_val))
   #정확도 측정
    _, _, a = sess.run( [ hypthesis, predicted, accuracy], feed_dict= {X:x_data, Y:y_data} )
    print( "\n Accuracy:",a)


# In[8]:



#   print("predicted=",sess.run(predicted, feed_dict={X:x_data} ))
        
#    #다른 값 테스트
#    p_val, h_val = sess.run([predicted, y], feed_dict= {X:[ [1,5], [10,5], [4,5] ]} )
#    print("check predicted=",p_val) #연산된 값을 bool로 변환한 값.
#    print("cechkhypothesis=",h_val) #계산값

#    #정확도 측정
#    h,c,a = sess.run( [y, predicted, accuracy], feed_dict= {X:x_data, Y:y_data} )
#    print("\n Hypothesis :", h ,"\n Correct (Y) :", c, "\n Accuracy:",a)


# In[ ]:




