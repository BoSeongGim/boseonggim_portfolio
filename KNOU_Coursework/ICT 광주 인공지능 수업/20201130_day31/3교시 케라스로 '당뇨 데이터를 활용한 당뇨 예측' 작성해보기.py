#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense#Activation,
#from tensorflow.keras import optimizers


# In[2]:


seed =0
numpy.random.seed(seed)
tf.random.set_seed(seed)


# In[3]:


#step1. 데이터 로드& 변수에 할당.
data = numpy.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201124_day27/data-03-diabetes.csv",delimiter=",")

training_data = data[:,0:-1]
target_data = data[:,[-1]]


# In[4]:


#딥러닝 구조를 결정합니다(모델을 설정하고 실행하는 부분입니다.)
model = Sequential()
model.add(Dense(30,input_dim=8,activation='relu')) 
model.add(Dense(30,activation='relu')) 
model.add(Dense(1,activation='sigmoid'))


# In[5]:


#딥러닝을 실행합니다.
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
model.fit(training_data,target_data, epochs=3000, batch_size=1000)
print(model.evaluate(training_data, target_data) )


# In[7]:


#결과를 출력합니다.
print("\n Accuracy: %.4f "%(model.evaluate(training_data,target_data)[1]))


#만약 epochs=3000, batch_size=1000를 하였고 결과가 아래와 같이 나왔다.
#24/24 [==============================] - 0s 896us/step - loss: 0.0280 - accuracy: 0.9763
#Accuracy: 0.9763 
#그러면 이것을 무조건 신뢰할 수 있느냐는 별개의 문제이다. 왜냐면 과적합이 우려되기 때문.


# In[ ]:





# In[ ]:




