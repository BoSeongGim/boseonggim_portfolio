#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


mushrooms =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201203_day34/mushrooms.csv")
#mushrooms
# LabelEncoder - 열 단위로만 가능하므로 loop사용
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
for col in mushrooms.columns :
    mushrooms[col] = labelencoder.fit_transform(mushrooms[col]) #열단위로 기존값들을 숫자로 바꿔줌.(1열씩 1열씩 문자->숫자변경)
#mushrooms


# In[3]:


import matplotlib.pyplot as plt

y = mushrooms['class'].values        # class 열만을 취함.
x = mushrooms.drop(['class'],axis=1) # class 열을 제외한 나머지 모든열을 취함.
x = x.values


# In[4]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np


# In[5]:


seed=0
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=seed)
print("x_train.shape=",x_train.shape)
print("x_test.shape=",x_test.shape)
print("y_train.shape=",y_train.shape)
print("y_test.shape=",y_test.shape)
print(y_test[0:5])


# In[6]:


#Binary를 multi-class로
y_train = tf.keras.utils.to_categorical(y_train, num_classes=2)
y_test = tf.keras.utils.to_categorical(y_test,num_classes=2)


# In[7]:


###to_categorical로 이항->다항 변환후
print(x_train.shape)
print(y_train.shape)
print(y_test[0:5])


# In[8]:


model = Sequential()
model.add(Dense(48, input_dim=22, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(2, activation='softmax'))


# In[9]:


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history=model.fit(x_train, y_train, epochs=25, batch_size=32)


# In[10]:


model.summary()


# In[11]:


model.evaluate(x_test,y_test)

