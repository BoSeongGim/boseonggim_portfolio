#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np


# In[2]:


#실행할 때마다 같은 결과를 출력하기 위한 시드 값 설정
seed=0
np.random.seed(seed)
tf.random.set_seed(seed)


# In[3]:


#x,y 데이터 값
x_data = np.array([[2,3], [4,3], [6,4], [8,6], [10,7], [12,8], [14,9]], dtype=np.float32) #[[공부시간1,과외수1],[공부시간2,과외수2] ... ]
y_data = np.array([0,0,0,1,1,1,1], dtype=np.float32).reshape(7,1) #합격여부


# In[4]:


W = tf.Variable(tf.random.uniform([2,1], dtype=tf.float32) )
b = tf.Variable(tf.random.uniform([1], dtype=tf.float32) )


# In[5]:


def hypothesis(W,b) :
    return tf.sigmoid(-(tf.matmul(x_data, W) +b) )

def costFunc() :
    return - tf.reduce_mean(y_data * tf.math.log(hypothesis(W,b)) 
                            + (1-y_data) * tf.math.log(1-hypothesis(W,b)) )

def cost(W,b) :
    return - tf.reduce_mean(y_data *tf.math.log(hypothesis(W,b))
                           + (1-y_data) * tf.math.log(1-hypothesis(W,b)) )


# In[6]:


opt = tf.keras.optimizers.SGD(learning_rate=0.1)


# In[7]:


for i in range(3001) : 
    opt.minimize(costFunc, var_list=[W,b])
    if i % 100 == 0 :
        print(f'epochs={i}, cost={cost(W,b)}, W1={W.numpy()[0,0]}, W2={W.numpy()[1,0]},b={b.numpy()}' )


# In[9]:


print("============================")
print("W=",W.numpy())
print("b=",b.numpy())
print("sigmoid=",hypothesis(W,b).numpy() )
print()
print("Accturacy=%.4f"%(sum((y_data == (hypothesis(W,b).numpy()>0.5)).flatten()/ len(y_data) )))


# In[ ]:





# In[ ]:




