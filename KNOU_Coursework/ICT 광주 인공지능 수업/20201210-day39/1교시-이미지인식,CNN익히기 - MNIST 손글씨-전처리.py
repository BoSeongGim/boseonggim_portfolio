#!/usr/bin/env python
# coding: utf-8

# In[1]:


#데이터 전처리
from tensorflow.keras.datasets import mnist

import numpy as np
import sys
import tensorflow as tf

seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)


# In[2]:


#MNIST 데이터셋 불러오기
(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()

print("학습셋 이미지 수 : %d 개" % (X_train.shape[0]) )
print("테스트셋 이미지수 : %d 개"% (X_test.shape[0]) )


# In[3]:


import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap='Greys')
plt.show()


# In[4]:


for x in X_train[0]:
    for i in x :
        sys.stdout.write('%d\t' % i ) 
    sys.stdout.write('\n')


# In[7]:


#차원 변환 과정
X_train = X_train.reshape(X_train.shape[0], 784)
X_train = X_train.astype('float64')
X_train = X_train /255

X_test = X_test.reshape(X_test.shape[0], 784).astype('float64' )/ 255

print("class :%d" % (Y_class_train[0] ))

Y_train = tf.keras.utils.to_categorical(Y_class_train,10)
Y_test = tf.keras.utils.to_categorical(Y_class_test,10)

print(Y_train[0])


# In[ ]:




