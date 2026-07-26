#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np


# In[2]:


#x,y의 데이터 값
data=[[2,0], [4,0], [6,0], [8,1], [10,1], [12,1], [14,1]] # [[공부시간1,합격여부(합격=1) ],[공부시간2,합격여부(합격=1) ]...]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]


# In[3]:


a      = tf.Variable(tf.random.normal([1], dtype=tf.float64, seed=0 ))
b      = tf.Variable(tf.random.normal([1], dtype=tf.float64, seed=0 ))


# In[4]:


def hypothesis(a,b):
    #가설
    return 1/(1 + np.e** -(a * x_data + b) )

def cost(w,b):
    #손실을 계산하는 함수.
    return -tf.reduce_mean(np.array(y_data) * tf.math.log(hypothesis(a,b))
            +(1 -np.array(y_data)) * tf.math.log(1- hypothesis(a,b)) )


def costFunc():#minimize에서 사용 손실(비용)함수
    return -tf.reduce_mean(np.array(y_data) * tf.math.log(hypothesis(a,b))
            +(1 -np.array(y_data)) * tf.math.log(1- hypothesis(a,b)) )


#loss를 최소로 하는 값 구하기 & #학습률 값
opt = tf.keras.optimizers.SGD(learning_rate=0.5)


# In[5]:


#학습
for i in range(60001) :
    opt.minimize(costFunc, var_list=[a,b])
    if i % 6000 == 0 :
        print(i, f'{cost(a,b)}, {a.numpy()}, {b.numpy()}' )
        
#새로운값 5,7,13에 대한 분석결과를 출력하도록 한다.
#즉시실행의 개념에 따라 작동한다.
new_x_data=5              
y_test = 1/(1 + np.e** -(a * new_x_data + b) )             
print(y_test.numpy() )             #y_test :  [3.88235153e-05] 의 의미는 합격률=0.0003, 거의 불합격이란애기.              
print("%.40f"%float(y_test.numpy()) )

new_x_data=7
y_test = 1/(1 + np.e** -(a * new_x_data + b) ) 
print(y_test.numpy() )             #y_test :  [3.88235153e-05] 의 의미는 합격률=0.0003, 거의 불합격이란애기.              
print("%.40f"%float(y_test.numpy()) )

new_x_data=13
y_test = 1/(1 + np.e** -(a * new_x_data + b) ) 
print(y_test.numpy() )             #y_test :  [3.88235153e-05] 의 의미는 합격률=0.0003, 거의 불합격이란애기.              
print("%.40f"%float(y_test.numpy()) )
   


# In[ ]:




