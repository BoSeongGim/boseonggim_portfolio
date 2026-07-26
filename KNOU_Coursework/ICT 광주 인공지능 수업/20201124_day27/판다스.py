#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


s= pd.Series([9904312, 3448737, 2890451, 2466052],
            index=["서울","부산","인천","대구"]
            )
s


# In[4]:


s.ndim #몇 차원 배열이냐? 의 답변인것.


# In[6]:


s.shape


# In[7]:


pd.Series(range(10,14))


# In[8]:


s.index


# In[9]:


type(s.index)


# In[11]:


s.values


# In[13]:


type(s.values)


# In[15]:


s.name="인구"
s.index.name="도시"
s


# In[16]:


s/1000000


# In[17]:


s["부산"]


# In[18]:


s[[0,3,1]]


# In[19]:


s[1:3]


# In[21]:


s["부산":"대구"]


# In[24]:


s0 = pd.Series(range(3), index=["a","b","c"])
s0


# In[25]:


s0.a


# In[27]:


s0.c


# In[29]:


for a in s.items():
    print(a)


# In[31]:


data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}   # 딕셔너리
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"] # LIST
index = ["서울", "부산", "인천", "대구"] # LIST


# In[32]:


df = pd.DataFrame(data, index=index, columns=columns)
print(df)
df


# In[34]:


df["2005-2010 증가율"] = ((df["2010"] - df["2005"]))
df


# In[ ]:




