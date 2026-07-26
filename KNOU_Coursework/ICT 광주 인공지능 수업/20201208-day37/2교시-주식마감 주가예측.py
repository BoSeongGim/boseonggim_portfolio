#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint 
from tensorflow.keras.callbacks import EarlyStopping

import numpy as np
import pandas as pd
import tensorflow as tf
import os
import matplotlib.pyplot as plt


# In[2]:


#seed set
seed=0
np.random.seed(seed)
tf.random.set_seed(seed)


# In[3]:


df_pre = pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201208-day37/data-02-stock_daily.csv", header=1)#header:헤더로 설정할 행의 번호. 원본을 편집않도록 도와주는 고마운 존재!
df_pre


# In[4]:


df = df_pre.sample(frac=1) 
dataset= df_pre.values


#데이터 정규화
from sklearn.preprocessing import StandardScaler
xdata=dataset
xdata_ss = StandardScaler().fit_transform(xdata)
print(xdata_ss)


X = dataset[:,0:4]
Y = dataset[:,4]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=seed)


# In[8]:


model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1)) 


# In[9]:


model.compile(loss='mean_squared_error', optimizer='adam')


# In[10]:


#학습 자동 중단 설정
early_stopping_callback = EarlyStopping(monitor = 'val_loss', patience=50)
#monitor = 'val_loss' :val_loss의 값을 기준으로 해서 멈춤여부를 정하겠어.(횟수는 patience에서 설정)
# patience=100 : 100번까지는 오차가 줄지 않아도 봐줄게. 하지만 101번 째에도 오차가 안줄면 학습을 멈출거야!

#모델 저장 조건 설정.
MODEL_DIR = './model'
if not os.path.exists(MODEL_DIR) :
    os.mkdir(MODEL_DIR)

#모델 저장조건 설정
modelpath = "./model/{epoch:02d}-{val_loss:.4f}.hdf5" #파일저장경로 & 저장형식까지 설정.
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True) 

#모델 실행
history = model.fit(X_train, Y_train, validation_split=0.33, epochs=500, batch_size=10,
                    callbacks=[early_stopping_callback, checkpointer]) 


# In[11]:


hist = pd.DataFrame(history.history)
print(hist.tail() )


# In[14]:


#loss에 테스트셋으로 실험 결과의 오차값을 저장한다.
y_vloss = history.history['val_loss']

y_actual = history.history['loss']


#x값을 지정하고 정확도는 파란색 / 오차는 빨간색 으로 표현.
x_len = np.arange(len(y_actual)) #x축 길이를 설정하기 위해 실시.
plt.figure(figsize=(10,5) )

plt.plot(x_len, y_vloss, "o", c="violet", markersize=3, label='predicted')
plt.plot(x_len, y_actual, "o", c="springgreen", markersize=3, label='actual')

plt.legend() #범례표기하도록 실시.
plt.show()
    
#모델 실행 및 저장
#model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer]) 


# In[ ]:




