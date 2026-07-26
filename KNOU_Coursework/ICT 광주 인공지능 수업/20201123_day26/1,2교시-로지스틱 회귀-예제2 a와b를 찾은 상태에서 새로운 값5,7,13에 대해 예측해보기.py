#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[2]:


#x,y의 데이터 값
data=[[2,0], [4,0], [6,0], [8,1], [10,1], [12,1], [14,1]] # [[공부시간1,합격여부(합격=1) ],[공부시간2,합격여부(합격=1) ]...]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]


# In[3]:


#,a와 b의 값을 임의로 정한다.
a = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))


# In[4]:


#y 시그모이드 함수의 방정식을 세운다.
y = 1/(1 + np.e** -(a * x_data + b) )#넘파이 라이브러리를 이용하여 작성한 것이다.


# In[5]:


#loss를 구하는 함수
loss = -tf.reduce_mean( np.array(y_data) * tf.log(y) + (1 - np.array(y_data)) * tf.log(1-y) )


# In[6]:


#학습률 값
leaning_rate = 0.5


# In[7]:


#loss를 최소로 하는 값 구하기
gradient_decent = tf.train.GradientDescentOptimizer(leaning_rate).minimize(loss)


# In[27]:


#학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for i in range(60001) :
        sess.run(gradient_decent)
        if i % 6000 ==0 :
            print("Epoch : %.f, loss=%.4f, 기울기a = %.4f, y절편=%.4f"
                 % (i,sess.run(loss), sess.run(a), sess.run(b) ))

        #새로운값 5,7,13에 대한 분석결과를 출력하도록 한다.
        if i % 60000 ==0 and i != 0 :
            new_x_data=5              
            y_test = 1/(1 + np.e** -(a * new_x_data + b) ) 
            print("y_test : ", sess.run(y_test) )             #y_test :  [3.88235153e-05] 의 의미는 합격률=0.0003, 거의 불합격이란애기.              
            print("y_test[0] : ", sess.run(y_test[0]) )

            new_x_data=7
            y_test = 1/(1 + np.e** -(a * new_x_data + b) ) # 합격률 0.53537986
            print("y_test : ", sess.run(y_test) )
            print("y_test[0] : ", sess.run(y_test[0]) )

            new_x_data=13
            y_test = 1/(1 + np.e** -(a * new_x_data + b) )  #합격률 1.
            print("y_test : ", sess.run(y_test) )
            print("y_test[0] : ", sess.run(y_test[0]) )
            print("")
            print("y_test :",y_test)
            
sess.close()


# In[ ]:




