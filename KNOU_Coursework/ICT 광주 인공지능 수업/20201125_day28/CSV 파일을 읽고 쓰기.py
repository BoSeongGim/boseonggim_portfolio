#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import pandas as pd
import numpy as np
tf.__version__


# In[2]:


### 파이썬 파일 read / write

inFp = open("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/test.csv")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")


inFp.close()


# In[ ]:


### 모든 행을 읽기 위해서는 loop를 써라.

inFp =None;

open("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/test.csv")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")


inFp.close()


# In[ ]:


### 모든 행을 읽기 위해서는 loop를 써라.

inFp =None;

open("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/test.csv")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")


inFp.close()


# In[ ]:


outFp  =
open("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/testTxt.txt","w",encoding='utf-8')

while True :
    outStr = input("내용입력 : ")
    if ourStr != "":
        outFp.wirtelines(outstr+"\n")


# In[ ]:


inFp = 
outPf = open(

inList =- )


# In[9]:


np_blood_fat = np.loadtxt("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/Blood_fat.csv", delimeter=',')


# In[10]:


import csv

f = open("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/test.csv")
csv_data = csv.reader(f)

print(csv_data)
for row in csv_data:
    print(row)
print(type(row))
f.close()


# In[12]:


file_gwangju= open("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/광주기온.csv","r")

inList = file_gwangju.readlines()
for inStr in inList:
    print(inStr,end="")
file_gwangju.close()


# In[13]:


df_gw = pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/광주기온.csv",encoding='CP949')
df_gw


# In[16]:


df_gw = pd.read_csv("C:/sourceTree/DataScience/ICT/Py_Project/20201125_day28/광주기온.csv",index_col='날짜', encoding='CP949')
df_gw


# In[17]:


df_titanic = pd.read_csv("https://raw.githubusercontent.com/datascienceschool/docker_rpython/master/data/titanic.csv")


# In[18]:


df_titanic


# In[ ]:





# In[ ]:





# In[ ]:




