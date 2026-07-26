#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.preprocessing import LabelEncoder


import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)


# In[2]:


df_pre =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201203_day34/iris.csv", header=None)

df = df_pre.sample(frac=1) #미선언 오류로 일단 지정.

dataset = df.values


X = dataset[:,0:4].astype(float) #넘파이에서 활용하려면 자료형을 명시해야 한다.
Y_obj = dataset[:,4]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
Y = tf.keras.utils.to_categorical(Y)


# In[3]:


model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu' ))
model.add(Dense(3,activation='softmax'))


# In[4]:


model.compile(loss='categorical_crossentropy',
                optimizer='adam',metrics=['accuracy'])


# In[7]:


#이 부분부터 12월 4일과는 달라진다.(01의 모델업데이트와 동일하다) =============================

#모델 실행 및 저장
history = model.fit(X, Y, validation_split=0.33, epochs = 5000, batch_size= 10) 
    

y_vacc = history.history['val_accuracy']   #y_acc에 학습셋으로 측정할 정확도의 값을 저장.
y_vloss = history.history['val_loss'] #y_vloss에 테스트셋으로 실험 결과의 오차값을 저장한다.
y_acc = history.history['accuracy']
y_loss = history.history['loss']


x_len = np.arange(len(y_acc))
plt.figure(figsize=(10,10))
plt.plot(x_len, y_vacc, "o", c="red", markersize=3, label='val_accuracy')
plt.plot(x_len, y_acc, "o", c="blue", markersize=3, label='accuracy')
plt.plot(x_len, y_vloss, "o", c="violet", markersize=3, label='val_loss')
plt.plot(x_len, y_loss, "o", c="springgreen", markersize=3, label='loss')


plt.legend()
plt.show()
    
#모델 실행 및 저장
#model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer]) 


# In[6]:


#===========================================================================


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




