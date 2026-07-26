#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


#시드값 설정
seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)


# In[4]:


#데ㅣ터
df_pre =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201204_day35/wine.csv",header=None)
df = df_pre.sample(frac=1)#frac=1 : frac=1 원본데이터 100%를 불러온다, 

#데이터 셋을 구성. 학습셋 검증셋 않음.
dataset = df.values
X = dataset[:,0:12]
Y = dataset[:,12]


# In[5]:


model = Sequential()

#조건1 : 4개의 은닉층 생성 30,12,8,1(선생님이 정한 임의의 값들임.)
model.add(Dense(30, input_dim=12,activation='relu' ))#히든레이어, 인풋(input_dim), 
model.add(Dense(12,  activation='relu' ) ) #Dense를 이용하여 각 모델을 설정.
model.add(Dense(8,  activation='relu' ) )
model.add(Dense(1,  activation='sigmoid' ) )


# In[6]:


#조건2 : binary_crossentropy, adam 사용
model.compile(loss='binary_crossentropy',
              optimizer='adam',metrics=['accuracy'])


# In[8]:


#이 부분부터 12월 4일과는 달라진다.=============================

#모델 저장 폴더 설정
MODEL_DIR = './model'
if not os.path.exists(MODEL_DIR) :
    os.mkdir(MODEL_DIR)

    
#모델 저장조건 설정
modelpath = "./model/{epoch:02d}-{val_loss:.4f}.hdf5" #파일저장경로 & 저장형식까지 설정.
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True) 
# checkpointer변수 : 모니터할 값을 지정하는 변수.
#ModelCheckpoint는 계속 감독자처럼 계속 체크 및 기록만 하고 있다.
#  save_best_only=True 옵션 : epochs 수만큼 저장하는게 아니라, 개선점이 보인 순간의 값들을 저장하는 식으로 의미 있는 값들만 저장하는 식으.

#모델 실행 및 저장
model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer]) 


# In[12]:


#결과를 출력합니다.
print("\n Accuracy : %.4f" %(model.evaluate(X,Y)[1]))

