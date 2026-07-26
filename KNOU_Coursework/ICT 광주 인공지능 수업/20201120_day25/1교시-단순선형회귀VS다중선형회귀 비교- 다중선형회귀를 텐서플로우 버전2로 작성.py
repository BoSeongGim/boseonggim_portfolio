#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


#x1,x2,y의 데이터 값.
data = [[2, 0 ,81], [4, 4, 93], [6,2,91], [8,3,97]] # 공부한시간,과외횟수,시험점수

x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data] #새로추가되는 값. 다중선형회귀 위해 x2가 추가됨.
y_data = [y_row[2] for y_row in data]

a1     = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed=0 ))#기울기 
a2     = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed=0 ))#기울기 
b      = tf.Variable(tf.random.uniform([1], 0, 100,dtype=tf.float64, seed=0 ))#절편


# In[3]:


#기울기와 절편을 통하여 계산되는 예상 y값

def hypothesis(a1,a2,b):
    return x1 * a1 + x2 * a2 +b    #가설 a1*x1 + a2*x2 +b

def cost(a1,a2,b):
    #손실을 계산하는 함수.
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,a2,b) - y_data )))

def costFunc():
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,a2,b) - y_data ))) #minimize에서 사용 손실(비용)함수

#경사하강법 실시.
opt = tf.keras.optimizers.SGD(learning_rate=0.1)
#텐서플로 버전1의 gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)가 
#텐서플로 버전2로 오면서 사용이 불가하게 되었다.
#대신 tf.keras.optimizers.SGD에서 대신 할 수 있도록 대체되었다.(#기존 버전1과 딴사람처럼 달라졌다고 하는 대표적이유)

for i in range(5000):
    opt.minimize(costFunc, var_list=[a1,a2,b])
    #opt.minimize()도 함수의 형태로 값을 받는 것으로 바뀌었기에 기존 버전1의 방식대로 할수가 없다
    #버전2는 프로그래머들의 요청인 함수개념등 프로그래머들의 제안들이 도입되고,
    #텐서플로 버전1의 그래프와 세션 개념을 숨기면서 방식이 바뀌어져 버렸다.
    
    if i % 100 == 0 :
        print(i, f'{cost(a1,a2,b)},{a1.numpy()}, {a2.numpy()}, {b.numpy()}' )
                 # cost(RMSE)값,     기울기1,     기울기2,      y절편값


# In[ ]:




