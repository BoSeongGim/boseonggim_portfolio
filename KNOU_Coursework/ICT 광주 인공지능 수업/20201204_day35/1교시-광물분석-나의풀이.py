#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201204_day35/sonar.csv",header=None)
print(df.info)
#행->샘플 208개(행)/ 열-> 속성 60 클래스 1 
#결론 : 우리가 따로 전처리할 필요 없ㅇ르 정도로 잘 갈무리된 자료이다!


# In[3]:


print(df.head)


# In[4]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# In[5]:


labelencoder = LabelEncoder()
df[60] = labelencoder.fit_transform(df[60])
df


# In[10]:



dataset = df.values 
X = dataset[:,0:59].astype(float) #넘파이에서 활용하려면 자료형을 명시해야 한다.
Y_obj = dataset[:,60]


#3.데이터셋 생성
x_train = dataset[:160,0:59]
y_train = dataset[:160,60]
x_test = dataset[48:,0:59]
y_test = dataset[48:, 60]

#4.모델 구성하기
model = Sequential()
model.add(Dense(28, input_dim=59,activation='relu' ))
model.add(Dense(14, input_dim=59,activation='relu' ))
model.add(Dense(1,  activation='sigmoid' ) )


#5.딥러닝을 실행합니다.
#모델 학습과정 설정
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
#모델 학습 실시
model.fit(x_train,y_train,epochs=3000, batch_size=30)


# In[11]:


scores = model.evaluate(x_test,y_test)
#결과를 출력합니다.
print("%s:%.2f%%" %(model.metrics_names[1],scores[1]*100 ))


# In[ ]:




