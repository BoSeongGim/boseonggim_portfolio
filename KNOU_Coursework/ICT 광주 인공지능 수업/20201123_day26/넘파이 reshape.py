#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.arange(12)
a


# In[4]:


b = a.reshape(3,4)
b


# In[5]:


#-1을 넣으면 갯수를 맞추기 위해 컴이 알아서 계산해서 넣는다.
a.reshape(3,-1)


# In[10]:


#-1을 넣으면 갯수를 맞추기 위해 컴이 알아서 계산해서 넣는다.
a.reshape(2,2,-1)
print(a.reshape(2,2,-1))


# In[11]:


#-1을 넣으면 갯수를 맞추기 위해 컴이 알아서 계산해서 넣는다.
a.reshape(2,-1,2)


# In[ ]:




