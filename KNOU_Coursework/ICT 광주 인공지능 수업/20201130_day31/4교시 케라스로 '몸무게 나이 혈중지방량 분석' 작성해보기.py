#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import RMSprop
from mpl_toolkits.mplot3d import Axes3D

#1.0 경우 아래와 같이 쓴다고 한다.
#import keras
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.optimizers import RMSprop


# In[2]:


#step1. 데이터 로드& 변수에 할당.
raw_data = np.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201119_day24/Blood_fat.csv",delimiter=",")

#실제 데이터들
xs = np.array(raw_data[:,0], dtype=np.float32)
ys = np.array(raw_data[:,1], dtype=np.float32)
zs = np.array(raw_data[:,2], dtype=np.float32)


# In[3]:


#그래프를 그릴려고 맞춰 만드는 과정.
x_data = np.array(raw_data[:,0:2], dtype=np.float32)
y_data = np.array(raw_data[:,2], dtype=np.float32)
y_data = y_data.reshape((25,1)) #쉐이프 맞춰줄려고


# In[4]:


#선형회귀&케라스에서는 RMSprop를 많이 사용한다. 
#케라스에서는 모델이 핵심이다!(모델생성,predict,그래프그리기)

rmsprop = RMSprop(lr=0.01)
model = Sequential()
model.add(Dense(1,input_shape=(2,)))
model.compile(loss='mse',optimizer=rmsprop)
model.summary()


# In[5]:


hist = model.fit(x_data,y_data, epochs=1000)
print(hist.history.keys())


# In[6]:


print("100kg 40세 혈중지방함량치:",model.predict(np.array([100,40]).reshape(1,2)) ) #1차원적 요소인 나이와 몸무게를 2차원적(1행2열)로 만듬
print("60kg 25세 혈중지방함량치:",model.predict(np.array([60,25]).reshape(1,2)) )


# In[7]:


W_, b_ = model.get_weights()#웨이트랑 바이어스를 구하려고 하는 것.설정한대로 웨이트와 바이어스를 갖고오도록 하는것.

#x=np.linspace(start, stop, num). start배열의 시작값, stop은 배열의 끝값
#num은 start와 stop 사이를 몇 개의 일정한 간격으로 요소를 만들지
#num을 생략하면 디폴트(Default)로 50개의 수열, 즉 1차원 배열을 만들어줍니다.

x = np.linspace(20,100,50).reshape(50,1)#x:몸무게 / 20~100까지 50개를 만든다.
y = np.linspace(10,70,50).reshape(50,1)#y:나이 / 0~70까지 50개를 만든다.
print("x=",x.reshape)
print("y=",y.reshape)

#기존의 코드에서는 위의 x,y,2개의 reshape 출력을 아래의 for문을 활용하여 만들었다.
#
#calc_y=[]
#for i in range(25):
#    new_y = (da1*x[i])+(da2*x2[i]+db)
#    calc_y.append(new_y)
#    print(new_y)


# In[8]:


#Numpy 배열들을 하나로 합치는데 이용.
#나이와 몸무게를 하나의 2차원 배열로 만든다.
X = np.concatenate((x,y), axis=1)
print("X=",X.shape)

#예측치
Z=np.matmul(X,W_)+b_ #ax+b  


# In[9]:


fig = plt.figure(figsize=(12,12))
ax=fig.add_subplot(111,projection='3d')


ax.scatter(x,y,Z)#예측 데이터

#아래는 실제 데이터들
ax.scatter(xs,ys,zs)
ax.set_xlabel('Weight')
ax.set_ylabel('Age')
ax.set_zlabel('Blood fat')
ax.view_init(15,15)
plt.show()



# In[ ]:




