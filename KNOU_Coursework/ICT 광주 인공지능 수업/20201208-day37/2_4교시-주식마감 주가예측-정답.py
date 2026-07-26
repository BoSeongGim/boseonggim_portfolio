#!/usr/bin/env python
# coding: utf-8

# In[1]:


#tensorflow
import tensorflow as tf

#keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201208-day37/data-02-stock_daily.csv", header=1)#header:헤더로 설정할 행의 번호. 원본을 편집않도록 도와주는 고마운 존재!
data


# In[3]:


#데이터 시각화
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(30,20) )

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.plot(data['Open'])
ax1.plot(data['High'])
ax1.plot(data['Low'])
ax1.plot(data['Close'])

ax2.plot(data['Volume'])

ax3.plot(data['Open'][0:7], linewidth=3.0, label="Open" )
ax3.plot(data['High'][0:7], linewidth=3.0, label="High" )
ax3.plot(data['Low'][0:7], linewidth=3.0, label="Low" )
ax3.plot(data['Close'][0:7], linewidth=3.0, label="Close" )

ax3.legend(prop={'size':30})


# In[4]:


#"Open","High","Low","Volume"으로 Close 가격 예측하기
xdata = data[["Open","High","Low","Volume"]]
ydata = pd.DataFrame(data["Close"])

#데이터 정규화
from sklearn.preprocessing import StandardScaler

xdata_ss = StandardScaler().fit_transform(xdata)
ydata_ss = StandardScaler().fit_transform(ydata)

print(xdata_ss.shape, ydata_ss.shape )


# In[5]:


xtrain = xdata_ss[220: , :]
xtest  = xdata_ss[:220 , :]
ytrain = ydata_ss[220: , :]
ytest  = ydata_ss[:220 , :]

print(xtrain.shape, xtest.shape, ytrain.shape, ytest.shape)
#220행 이후의 데이터들을 트레이닝으로 사용하여 


# In[6]:


model = Sequential()
model.add(Dense(1024, input_dim=4, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1)) 


# In[7]:


model.compile(loss='mse', optimizer='adam', metrics=['mae']) #metrics=['mae'] 평균제곱오차


# In[8]:


#학습 자동 중단 설정
from tensorflow.keras.callbacks import EarlyStopping
es= EarlyStopping(monitor="mae", patience=10)

seed=123
np.random.seed(seed)
tf.random.set_seed(seed)
hist = model.fit(xtrain, ytrain, epochs=100, batch_size=16, callbacks=[es])


print("loss:"+str(hist.history['loss']) )
print("MAE:"+str(hist.history['mae']) )


# In[9]:


res = model.evaluate(xtest,ytest,batch_size=32)
print("loss:",res[0],"mae",res[1])


# In[10]:


xhat=xtest
yhat=model.predict(xhat)
plt.figure()
plt.plot(yhat, label="predicted")
plt.plot(ytest, label="actual")
plt.legend(prop={'size':20})
print("Evaluate : {}".format(np.average((yhat-ytest)**2)))# format(np.average((yhat-ytest)**2) : 평균제곱오차


# In[ ]:




