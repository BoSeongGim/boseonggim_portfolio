#!/usr/bin/env python
# coding: utf-8

# In[1]:


#노이즈나 
# 좋은 데이터 저장소
# UCI 머신 러닝 저장소 -> https://archive.ics.uci.edu/ml/index.php


# In[2]:


#0.사용할 패키지 불러오기
#import tensorflow as tf
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[3]:


#1.랜덤시드 고정
np.random.seed(5)
#책 설명 : "seed값을 설정한다"="랜덤 테이블중에서 몇 번째 테이블을 불러와 쓸지를 정하는 것" 
#          "seed값이 같다" = "똑같은 랜덤값을 출력한다."
#          "넘파이 라이브러리를 사용하면서 텐서플로 기반으로 딥러닝을 구현할 때에는 일정한 결과값을 얻기 위해
#           넘파이의 seed값과 텐서플로 seed값을 모두 설정해야 한다.
#
# 책 설명 출처 : 모두의 딥러닝(개정2판)-11장 6절-'피마 인디언의 당뇨병 예측 실행' 중에서


# In[4]:


#2.데이터 준비
dataset = np.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201201_day32/pima-indians-diabetes.csv",delimiter=",",dtype=np.float32)
#768명(768행)의 데이터를 

#3.데이터셋 생성
x_train = dataset[:700,0:8]
y_train = dataset[:700,8]
x_test = dataset[700:,0:8]
y_test = dataset[700:, 8]


# In[5]:


#4.모델 구성하기
model = Sequential()
model.add(Dense(12, input_dim=8,activation='relu' ))
model.add(Dense(8,  activation='relu' ) )
model.add(Dense(1,  activation='sigmoid' ) )


# In[6]:


#5.딥러닝을 실행합니다.
#모델 학습과정 설정
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
#모델 학습 실시
model.fit(x_train,y_train,epochs=1500, batch_size=64)


# In[ ]:





# In[7]:


scores = model.evaluate(x_test,y_test)
#결과를 출력합니다.
print("%s:%.2f%%" %(model.metrics_names[1],scores[1]*100 ))


# In[ ]:





# In[ ]:





# In[ ]:




