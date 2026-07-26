#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
diabetes_data = pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201124_day27/data-03-diabetes.csv",
                             names=["A","B","C","D","E","F","G","H","class"])


# In[2]:


#1)데이터의 일부분 찍어보기
diabetes_data


# In[3]:


#2)Seaborn을 활용하여 heatmap을 보며 데이터간의 상관관계를 분석하세요

import matplotlib.pyplot as mpl
import matplotlib as plt
import seaborn as sns #좀 더 정교하게 그림도와줌

#plt.figure(figsize=(12,12) )
#sns.heatmap(diabetes_data.corr(), linewidths=0.1, vmax=0.5, linecolor='white',annot=True)

#plt.show()

#상관관계 분석
# : 요소 D와 E가 가장 밀접한 관계(0.47)를 갖고 있으므로 
#   요소 D,E가 큰 영향을 미치는 요소로 판단.


# In[4]:


#3) 커널 밀도 추정(KDE: Kernel Density Estimator) 그려보기
diabetes_data.plot.kde()


# In[5]:


#4)Box plot 그려보고 의미 파악하기
diabetes_data.plot.box()


# In[6]:


#5)그외 실습에서 사용했던 여러가지 기능등을 사용해서 데이터 조사해보기
sns.pairplot(diabetes_data)


# In[7]:


sns.pairplot(diabetes_data,hue="class")


# In[ ]:




