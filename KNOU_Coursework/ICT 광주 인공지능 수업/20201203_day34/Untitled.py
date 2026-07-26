#!/usr/bin/env python
# coding: utf-8

# In[6]:


#판다스를 통해 로드
import pandas as pd
df =pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201203_day34/iris.csv",
               names=["sepal_length","sepal_width","petal_length","petal_width","species"])
print(df.head())


# In[19]:


df.describe()


# In[8]:


#판다스의 seaborn 기능등을 활용하여 그래프로 먼저 데이터의 분류 파악해보기
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df,hue='species');
plt.show()


# In[9]:


#케라스를 이용하여 아이리스의 품종을 예측해보자.
dataset = df.values
X = dataset[:,0:4].astype(float)
Y_obj = dataset[:,4]


# In[11]:


#y의 값을 문자열->숫자로 변경
from sklearn.preprocessing import LabelEncoder

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
# Y #Y를 실시하면 값이 0,1,2로 바뀜을 확인.
    #딥러닝 용도에 맞추기위해 0,1,2로 바꾼 것


# In[14]:


#원-핫 인코딩(원-핫 인코딩:여러개의 Y값을 0과1만으로 구성된 형태로 바꿔주는 기법)
import tensorflow as tf
Y_encoded = tf.keras.utils.to_categorical(Y)

#Y_encoded # 출력값이 아래와 같이 바뀌게 된다.
#첫번째 모델의 경우 -> [1., 0., 0.],
#두번째 모델의 경우 -> [0., 1., 0.],
#세번째 모델의 경우 -> [0., 0., 1.],


# In[17]:


#모델 만들어보기
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(3,activation='softmax'))


# In[36]:


#3.데이터셋 생성
#x_train = dataset[:100,0:4]
#y_train = Y_encoded[:100,:]
#x_test = dataset[50:,0:8]
#y_test = Y_encoded[:50,:]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
x_train.shape, x_test.shape, y_train.shape, y_test.shape



#5.딥러닝을 실행합니다.
#모델 학습과정 설정
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
#모델 학습 실시
model.fit(x_train,y_train,epochs=1500, batch_size=64)


# In[35]:


scores = model.evaluate(x_test,y_test)
#결과를 출력합니다.
print("%s:%.2f%%" %(model.metrics_names[1],scores[1]*100 ))


# In[ ]:




