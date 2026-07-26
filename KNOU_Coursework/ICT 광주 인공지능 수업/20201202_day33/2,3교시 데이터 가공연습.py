#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#csv파일에 헤더가 없기에 헷갈리기 쉽다.
#그래서 names라는 판다스의 함수를 활용하여 각 속성별 키워드를 정해주어보자
df = pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201201_day32/pima-indians-diabetes.csv",
                 names=["pregnant","plasma","pressure","thickness",
                       "insulin","BMI","predigree","age","class"])
df
#전체보기는 아래코드 주석해제.
#print(df)


# In[2]:


print(df)


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


print( df.info() )


# In[6]:


df.describe()


# In[7]:


#일부칼럼만 보기 - 임신횟수('pregnant')와 당뇨병 발병여부('class')만 확인해보기
df[['pregnant','class']]


# In[8]:


print(df[['pregnant','class']].groupby(['pregnant'], as_index=False).
     mean().sort_values(by='pregnant',ascending=True))


# In[9]:


#아무리 잘 정리된 테이블이라고 하여도 그래프로 표현하는 것이 빠른 파악에 도움이 된다.
import matplotlib.pyplot as plt
import seaborn as sns #좀 더 정교하게 그림도와줌


# In[10]:


plt.figure(figsize=(12,12))


# In[14]:


sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white',annot=True)

#df.corr() #df : 데이터 / .corr() : 각 변수간의(열 간의) 상관관계를 보려면
#linewidths=0.1
#vmax=0.5 #vmax :최대값 설정
#map=plt.cm.gist_heat, cmap:맵의 색깔 설정, plt.cm.gist_heat:
#linecolor='white'
#annot=True annot:각 셀의 값을 표기여부 결정.(true시 표기)
plt.show()


# In[12]:


print(df.corr())


# In[15]:


grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma',bins=10)
plt.show()


# In[ ]:




