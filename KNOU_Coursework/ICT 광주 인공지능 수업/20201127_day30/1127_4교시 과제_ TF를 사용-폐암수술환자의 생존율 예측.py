#!/usr/bin/env python
# coding: utf-8

# In[1]:



#진행단계 설명
#스텝1 : 필요한 텐서플로 넘파이 import
#스텝2 : 변수설정[ 데이터 로드& 변수할당, 이외변수 설정(스페이스 홀더,학습율)]
#스텝3 : 기울기(W1,W2) 바이어스(b1,b2) 설정.
#스텝4 : 딥러닝 입력층,은닉층,출력층 설정(총 3개 레이어)
#스텝5 : hypothesis, cost 등 설정.
#스텝6 : 실제학습실시.


# In[2]:


#스텝1: 필요한 텐서플로 넘파이 import
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np


# In[3]:


#스텝2: 변수설정[ 데이터 로드& 변수할당, 이외변수 설정(스페이스 홀더,학습율)]
data = np.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201127_day30/ThoraricSurgery.csv",delimiter=",")

x_data=data[:,0:17] #0~17열(엑셀A~N)
y_data=data[:,[17]] #마지막열 생사여부결과

X = tf.placeholder(tf.float32, [None, 17] )#x에 None을 하여 다양한 값들이 입력받는것에 제한을 두지 않도록 함.(플레이스 홀더의 규칙중 하나!)
Y = tf.placeholder(tf.float32, [None, 1])
#x,y데이터들을 읽을 때 궁극적으로 마지막에 세션에 런시키려고 넣을 때 플레이스 홀더가 필요하다

learning_rate=0.1


# In[4]:


#스텝3 : 기울기(W1,W2) 바이어스(b1,b2) 설정.
#은닉층의 노드는 30개로 실시.

W1 = tf.Variable(tf.random_normal([17,30], name="weight1"))#x는 17열의 입력, 노드개수30개. 텍스트 예제가 텍스트를 한줄씩읽는 것과 같다.
b1 = tf.Variable(tf.random_normal([30]),name="bias1" )

W2 = tf.Variable(tf.random_normal([30,1], name="weight2"))
b2 = tf.Variable(tf.random_normal([1]),name="bias2" )


# In[5]:


#스텝4 : 딥러닝레이어 설정(총3개레이어 -입력,출력레이어 = 은닉층 총 1개)
#정확한 표현은 히든레이어를 설정한다가 맞지요
layer1= tf.sigmoid(tf.matmul(X,W1)+b1)


# In[6]:


#스텝5 : hypothesis, cost,train,predicted,accuracy 등 설정.
hypothesis = tf.sigmoid(tf.matmul(layer1, W2)+b2)

#코스트 트레인은 hypothesis에 사용된다.
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis) ) 
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)


#정확도 계싼을 담당하는 2개의 함수들,
#predicted = tf.cast(hypothesis> 0.5, dtpye=tf.float32 )
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32 )
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32 ))                          


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
    
    

