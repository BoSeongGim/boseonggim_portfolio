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


# In[3]:


#x,y 데이터 값
x_data = np.array([[2,3], [4,3], [6,4], [8,6], [10,7], [12,8], [14,9]]) #7행2열의 데이터 
y_data = np.array([0,0,0,1,1,1,1]).reshape(7,1)


# In[4]:


#입력값을 플레이스홀더에 실시.
X = tf.placeholder(tf.float64, shape=[None, 2])
Y = tf.placeholder(tf.float64, shape=[None, 1])


# In[5]:


#기울기 a와 바이어스 b의 값을 임의로 정함. a는 [2,1] 형태를 가지며 a1,a2이다.
a = tf.Variable(tf.random_uniform([2,1], dtype=tf.float64) )
#[2,1] 의미 : 들어오는 값은 2개, 나가는 값은 1개(tf.random_uniform([2,1])
b = tf.Variable(tf.random_uniform([1], dtype=tf.float64) )


# In[6]:


#y 시그모이드 함수의 방정식을 세움.
y = tf.sigmoid(-(tf.matmul(X,a) +b ))


# In[7]:


#오차를 구하는 함수
loss = -tf.reduce_mean(Y * tf.log(y) + (1-y) *tf.log(1-y) )
#tf.reduce_mean() : 배열의 평균


# In[8]:


#학습률
learning_rate=0.1


# In[9]:


#오차를 최소로 하는 값 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)


# In[10]:


predicted = tf.cast(y>0.5, dtype=tf.float64 ) #결과값 나오는 small Y이다.

accuracy =tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float64 )) #계산하기 좋게 0,1으로 변경한다
#accuracy : 정밀도 구하기
#tf.cast(tf.equal(predicted, Y) : 예측값(predicted과 실제값(Y)이 같은지(tf.equal() )를 확인후 boolean값으로 리턴하시오.
#(예) 예측을 11110으로 했는데 결과가 11111으로 나왔다? =>정확도(accuracy)는 80%=0.8

#학습
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())

    for i in range(3001) :
        a_, b_, loss_, _ = sess.run([a,b,loss,gradient_decent], feed_dict={X:x_data, Y: y_data} ) 
        if(i+1) % 300 == 0 :
            print("step=%d, a1=%.4f, a2=%.4f, b=%.4f, loss=%.4f" % (i+1, a_[0], a_[1], b_, loss_))
    
    print("predicted=",sess.run(predicted, feed_dict={X:x_data} ))
            
    #다른 값 테스트
    p_val, h_val = sess.run([predicted, y], feed_dict= {X:[ [1,5], [10,5], [4,5] ]} )
    print("check predicted=",p_val) #연산된 값을 bool로 변환한 값.
    print("cechkhypothesis=",h_val) #계산값

    #정확도 측정
    h,c,a = sess.run( [y, predicted, accuracy], feed_dict= {X:x_data, Y:y_data} )
    print("\n Hypothesis :", h ,"\n Correct (Y) :", c, "\n Accuracy:",a)


# In[ ]:




