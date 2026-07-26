#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy
import tensorflow as tf
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(seed)


# In[2]:


#준비된 수술 환자 데이터를 로딩
Data_set = numpy.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201127_day30/ThoraricSurgery.csv",delimiter=",")

#환자의 기록과 수술 결과를 X,Y로 구분하여 저장합니다.
X = Data_set[:,0:17]
Y = Data_set[:,[17]]


# In[3]:


#딥러닝 구조를 결정합니다(모델을 설정하고 실행하는 부분입니다.)
model = Sequential()
model.add(Dense(30,input_dim=17,activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))


# In[4]:


#딥러닝을 실행합니다.
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=30, batch_size=10)


# In[6]:


#결과를 출력합니다.
print("\n Accuracy: %.4f "%(model.evaluate(X,Y)[1]))


# 
