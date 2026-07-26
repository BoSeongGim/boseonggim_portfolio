#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

import numpy
import pandas as pd
import tensorflow as tf

#seed set
seed=0
numpy.random.seed(seed)
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


# In[6]:


model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(X_train, Y_train, epochs=200, batch_size=10 )


# In[5]:


Y_prediction = model.predict(X_test).flatten()

for i in range(10) :
    label = Y_test[i]
    prediction = Y_prediction[i]
    print("실제가격 : {:.3f}, 예상가격: {:.3f}".format(label, prediction))


# In[ ]:




