#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import tensorflow.compat.v1 as tf
#tf.disable_v2_behavior()

#본 예제에서는 텐서플로우를 사용하지 않습니다.(#의외중의 의외)
import numpy as np


# In[2]:


#가중치와 바이어스 설정
w11 = np.array([-2,-2])
w12= np.array([2,2])
w2 = np.array([1,1])
b1=3
b2=-1
b3=-1


# In[9]:


print(w11)
print(w12)
print(w2)


# In[3]:


#퍼셉트론
def MLP(x,w,b) :
    y = np.sum(w*x) +b
    if y<=0:
        return 0
    else:
        return 1


# In[4]:


#NAND게이트
def NAND(x1,x2):
    return MLP(np.array([x1,x2]), w11,b1)


# In[5]:


#OR게이트
def OR(x1,x2):
    return MLP(np.array([x1,x2]),w12,b2 )


# In[6]:


#AND 게이트
def AND(x1,x2):
    return MLP(np.array([x1,x2]),w2,b3)


# In[7]:


#XOR게이트
def XOR(x1,x2):
    return AND( NAND(x1,x2), OR(x1,x2) )


# In[8]:


# 값을 번갈아 대입해가며 최종값을 출력
if __name__ == '__main__':#메인모듈이면 아래의 내용을 실행하시오! 라는 의미로 간단히 생각하자.
    for x in [(0,0), (1,0), (0,1), (1,1)]:
        print("x[0]:",x[0], "x[1] :",x[1])
        y=XOR(x[0], x[1])
        print("입력 값 :"+str(x)+"출력 값:"+str(y))


# In[ ]:





# In[ ]:




