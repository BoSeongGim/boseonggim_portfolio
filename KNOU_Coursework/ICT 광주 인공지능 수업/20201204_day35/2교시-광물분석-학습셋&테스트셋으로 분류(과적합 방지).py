#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


import pandas as pd
import numpy as np
import tensorflow as tf


# In[2]:


#시드값 설정
seed = 0
tf.random.set_seed(seed)


# In[3]:


#데ㅣ터
df =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201204_day35/sonar.csv",header=None)
#print(df.info)


# In[4]:


dataset = df.values
X = dataset[:,0:60].astype(float)
Y_obj = dataset[:,60]


# In[5]:


#문자열 변환
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

#from sklearn.model_selection import train_test_split
#학습셋과 테스트셋의 구분
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=seed)


# In[6]:


#모델 변환
model = Sequential()
model.add(Dense(24, input_dim=60, activation='relu') )
model.add(Dense(12, activation='relu') )
model.add(Dense(1,  activation='sigmoid') )


# In[7]:


model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
              
#model.fit(X_train, Y_train, epochs =200 ,validation_data=(X_test, Y_test) ) #NG

model.fit(X_train, Y_train, epochs =200 ,batch_size=5) 


# In[8]:



#학습셋으로 모델 검증
print("\n Accuracy : %.4f" % (model.evaluate(X_train,Y_train)[1] ))          

#테스트셋에 모델 적용
print("\n Accuracy : %.4f" % (model.evaluate(X_test,Y_test)[1] ))              


# In[ ]:




