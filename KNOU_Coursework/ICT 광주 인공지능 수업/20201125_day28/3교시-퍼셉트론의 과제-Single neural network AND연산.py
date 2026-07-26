#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[2]:


#실행할 때마다 같은 결과를 출력하기 위한 시드 값 설정
seed=0
np.random.seed(seed)
tf.set_random_seed(seed)


# In[9]:


#x,y 데이터 값
x_data = np.array([[0,0], [0,1], [1,0], [1,1] ], dtype=np.float32) 
y_data = np.array([[0],[0],[0],[1] ], dtype=np.float32)


# In[13]:


#입력값을 플레이스홀더에 실시.
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_uniform([2,1], dtype=tf.float32) )
b = tf.Variable(tf.random_uniform([1], dtype=tf.float32) )


# In[5]:


#y 시그모이드 함수의 방정식을 세움.
hypothesis = tf.sigmoid(-(tf.matmul(X, W) +b ))


# In[6]:


cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis) )
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
predicted = tf.cast(hypothesis>0.5, dtype=tf.float32 ) #결과값 나오는 small Y이다.
accuracy =tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32 )) #계산하기 좋게 0,1으로 변경한다


# In[7]:


#학습
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())

    for step in range(10001) :
        sess.run(train,feed_dict={X:x_data, Y:y_data} ) 
        if(step) % 1000 == 0 :
            print("step:",step,"cost:",sess.run(cost, feed_dict={X:x_data, Y:y_data}),
                  "W:",sess.run(W),"b:",sess.run(b) )
    #정확도 측정
    h,c,a = sess.run( [hypothesis , predicted, accuracy], feed_dict= {X:x_data, Y:y_data} )
    print("\n Hypothesis :", h ,"\n Correct (Y) :", c, "\n Accuracy:",a)

