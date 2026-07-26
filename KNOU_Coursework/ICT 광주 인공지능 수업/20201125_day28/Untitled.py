#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index=["a", "b", "c"],
                  columns=["A", "B", "C", "D"])
df


# In[3]:


df.loc["b":"c"]


# In[6]:


df["b":"c"]


# In[8]:


df[["b","c"]] #이런경우는 키보드 애러임


# In[9]:


df.A


# In[10]:


def select_rows(df):
    return df.A > 15


# In[13]:


select_rows(df)


# In[14]:


df.loc[select_rows(df)]


# In[15]:


df.iloc[0,1]


# In[16]:


df.iloc[0,-2:]


# In[17]:


df.iloc[2:3,1:3]


# In[18]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(0)
df1 = pd.DataFrame(np.random.randn(100, 3),
                   index=pd.date_range('1/1/2020', periods=100),   ## 기간 100일(하루간격)
                   columns=['A', 'B', 'C']).cumsum()                ## cumsum()은 누적합
df1


# In[20]:


df1.plot()
plt.title("title")
plt.xlabel("time")
plt.ylabel("data")


# In[22]:


iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터

iris.sepal_length[:20].plot(kind='bar', rot=0)   # kind='line'... rot=0도 회전(x축눈금)
plt.title("꽃받침의 길이 시각화")
plt.xlabel("Data")
plt.ylabel("꽃받침의 길이")
plt.show()


# In[23]:


iris[:5].plot.bar(rot=0)
plt.title("Iris 데이터의 Bar Plot")
plt.xlabel("Data")
plt.ylabel("각 Feature의 값")
plt.ylim(0, 7)     # y축 범위
plt.show()


# In[24]:


df3 = titanic.pclass.value_counts()
df3.plot.pie(autopct='%.2f%%')
plt.title("선실별 승객 수 비율")
plt.axis('equal')
plt.show()


# In[25]:


iris.plot.box()


# In[26]:


iris.boxplot(by='species')


# In[ ]:




