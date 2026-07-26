#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint #모델을 저장하기 위해 케라스의 콜백함수 중 ModelCheckpoint함수를 불러옴.

#콜백함수
# : 메인프로그램이 돌아가면서 또 다른 프로세스를 가동시키는 것.(스레드라고 표현하기도 함.)
#   Non Block방식 
#   Non Block방식 : 호출이 있기 전까지 자신이 맡은 일을 계속한다는 것.


#from sklearn.preprocessing import LabelEncoder
#from sklearn.model_selection import StratifiedKFold

import pandas as pd
import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt


# In[2]:


#시드값 설정
seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)


# In[3]:


#데ㅣ터
df_pre =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201204_day35/wine.csv",header=None)
df = df_pre.sample(frac=0.15)#frac=1 과는 그렇게 큰 차이가 없다 그래도 전체에서 15%만 활용하는 셈.

#데이터 셋을 구성. 학습셋 검증셋 않음.
dataset = df.values
X = dataset[:,0:12]
Y = dataset[:,12]


# In[4]:


model = Sequential()

#조건1 : 4개의 은닉층 생성 30,12,8,1(선생님이 정한 임의의 값들임.)
model.add(Dense(30, input_dim=12,activation='relu' ))#히든레이어, 인풋(input_dim), 
model.add(Dense(12,  activation='relu' ) ) #Dense를 이용하여 각 모델을 설정.
model.add(Dense(8,  activation='relu' ) )
model.add(Dense(1,  activation='sigmoid' ) )


# In[5]:


#조건2 : binary_crossentropy, adam 사용
model.compile(loss='binary_crossentropy',
              optimizer='adam',metrics=['accuracy'])


# In[6]:


#이 부분부터 12월 4일과는 달라진다.(01의 모델업데이트와 동일하다) =============================

#모델 실행 및 저장
#validation_split을 위해 훈련 데이터의 일부를 자동으로 예약할 데이터의 비율을 나타내므로
#0보다 크고 1보다 작은 숫자로 설정해야 한다.
history = model.fit(X, Y, validation_split=0.33, epochs = 3500, batch_size= 500) #일부러 긴 학습을 보기위해 에포크를 3500으로 함.
# 검증량(validation_split)을 33%로 설정.(여담인데 33%라고 입력하면 걍 에러라고만 한다... 0.33식으로 입력해주자.)
    
#y_vloss에 테스트셋으로 실험 결과의 오차값을 저장한다.
y_vloss = history.history['val_loss']

#y_acc에 학습셋으로 측정할 정확도의 값을 저장.
y_acc = history.history['accuracy']

#x값을 지정하고 정확도는 파란색 / 오차는 빨간색 으로 표현.
x_len = np.arange(len(y_acc)) #x축 길이를 설정하기 위해 실시.
plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
plt.plot(x_len, y_acc, "o", c="blue", markersize=3)

plt.show()
    
#모델 실행 및 저장
#model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer]) 


# In[7]:


#결과를 출력합니다.
print("\n Accuracy : %.4f" %(model.evaluate(X,Y)[1]))

