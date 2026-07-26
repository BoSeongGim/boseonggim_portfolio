#!/usr/bin/env python
# coding: utf-8

# In[5]:



#ppt-1
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)


# In[6]:


#ppt-2
df =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201203_day34/iris.csv",
               names=["sepal_length","sepal_width","petal_length","petal_width","species"])


sns.pairplot(df, hue='species')
plt.show()

dataset = df.values 
X = dataset[:,0:4].astype(float) #넘파이에서 활용하려면 자료형을 명시해야 한다.
Y_obj = dataset[:,4]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
Y_encoded = tf.keras.utils.to_categorical(Y)


# In[8]:



model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(3,activation='softmax'))



#5.딥러닝을 실행합니다.
#모델 학습과정 설정
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
#모델 학습 실시
model.fit(X, Y_encoded, epochs=50, batch_size=1)


# In[9]:


#결과를 출력합니다.
print("\n Accuracy:%.4f" % (model.evaluate(X, Y_encoded)[1]) )


# In[ ]:




