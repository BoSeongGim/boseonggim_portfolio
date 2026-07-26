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

#seed set
seed=0
np.random.seed(seed)
tf.random.set_seed(seed)

df = pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201207-day36/housing.csv",delim_whitespace=True, header=None)
#1행의 셀에 해당 정보를 모두 입력하기에  화이트 스페스로 구분할 수 있따.
#이번에는 속성에 대한 알려주는 정보가 없어 파악도 쉽지않지.(한 마디로 클래스로 별도 구분이 없어서 어느게 결과인지 아는게 쉽지않다)


# In[2]:


dataset = df.values
X = dataset[:,0:13]
Y = dataset[:,13]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=seed)


# In[3]:


model = Sequential()
model.add(Dense(30, input_dim=13, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1)) #소프트맥스 등을 활용 않는 이유는
#선형회귀 데이터는 참과 거짓을 구분할 필요가 없기에 활성화 함수를 지정할 필요가 없게 된 것이다.


# In[4]:


#학습 자동 중단 설정
#학습 자동 중단 설정
early_stopping_callback = EarlyStopping(monitor = 'val_loss', patience=100)
#monitor = 'val_loss' :val_loss의 값을 기준으로 해서 멈춤여부를 정하겠어.(횟수는 patience에서 설정)
# patience=100 : 100번까지는 오차가 줄지 않아도 봐줄게. 하지만 101번 째에도 오차가 안줄면 학습을 멈출거야!

#모델 저장 조건 설정.
MODEL_DIR = './model'
if not os.path.exists(MODEL_DIR) :
    os.mkdir(MODEL_DIR)

#모델 저장조건 설정
modelpath = "./model/{epoch:02d}-{val_loss:.4f}.hdf5" #파일저장경로 & 저장형식까지 설정.
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True) 

early_stopping_callback = EarlyStopping(monitor = 'val_loss', patience=100)


# In[5]:


model.compile(loss='mean_squared_error', optimizer='adam')

#모델 실행
history = model.fit(X, Y, validation_split=0.2, epochs=350, batch_size=50, callbacks=[early_stopping_callback, checkpointer]) 


# In[6]:


Y_prediction = model.predict(X_test).flatten()

for i in range(10) :
    label = Y_test[i]
    prediction = Y_prediction[i]
    print("실제가격 : {:.3f}, 예상가격: {:.3f}".format(label, prediction))


# In[7]:


hist = pd.DataFrame(history.history)
hist.tail()


# In[8]:


#1교시 그래프로 표현하기 사용 =============================
#y_vloss에 테스트셋으로 실험 결과의 오차값을 저장한다.
y_vloss = history.history['val_loss']

#y_acc에 학습셋으로 측정할 정확도의 값을 저장.
y_loss = history.history['loss']
#x값을 지정하고 정확도는 파란색 / 오차는 빨간색 으로 표현.
x_len = np.arange(len(y_loss)) #x축 길이를 설정하기 위해 실시.
plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
plt.plot(x_len, y_loss, "o", c="blue", markersize=3)

plt.show()
    
#모델 실행 및 저장
#model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer]) 


# In[ ]:




