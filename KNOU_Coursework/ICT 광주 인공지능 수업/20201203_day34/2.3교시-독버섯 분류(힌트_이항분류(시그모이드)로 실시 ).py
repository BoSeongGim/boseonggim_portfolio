#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# In[4]:


mushrooms =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201203_day34/mushrooms.csv")

labelencoder = LabelEncoder()

for col in mushrooms.columns :
    mushrooms[col] = labelencoder.fit_transform(mushrooms[col])
    
mushrooms


# In[16]:



dataset = mushrooms.values 
X = dataset[:,1:22].astype(float) #넘파이에서 활용하려면 자료형을 명시해야 한다.
Y_obj = dataset[:,0]


#3.데이터셋 생성
x_train = dataset[:7000,1:22]
y_train = dataset[:7000,0]
x_test = dataset[1124:,1:22]
y_test = dataset[1124:, 0]

#4.모델 구성하기
model = Sequential()
model.add(Dense(12, input_dim=22,activation='relu' ))
model.add(Dense(1,  activation='sigmoid' ) )



#5.딥러닝을 실행합니다.
#모델 학습과정 설정
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
#모델 학습 실시
model.fit(x_train,y_train,epochs=1500, batch_size=64)


# In[8]:





# In[9]:





# In[ ]:




