#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold

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


# In[6]:


#10개의 파일로 쪼갬
n_fold = 10
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)


# In[7]:


#빈 accuracy 배열
accuracy=[]


# In[10]:


#모델의 설정 컴파일 실행
for train, test in skf.split(X,Y):
    model = Sequential()
    model.add(Dense(24, input_dim=60, activation='relu') )
    model.add(Dense(10, activation='relu') )
    model.add(Dense(1,  activation='sigmoid') )
    
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    model.fit(X[train], Y[train], epochs =100 , batch_size=5 )
    k_accuracy = "%.4f" % (model.evaluate(X[test],Y[test])[1] )
    accuracy.append(k_accuracy)    
print("\n %.f fold accuracy" % n_fold, accuracy)          


# In[ ]:



              


# In[ ]:





# In[ ]:




