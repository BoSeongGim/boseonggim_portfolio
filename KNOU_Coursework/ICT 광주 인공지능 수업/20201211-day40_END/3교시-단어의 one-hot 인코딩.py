#!/usr/bin/env python
# coding: utf-8

# In[1]:


#토큰화(Tokenizer())->원핫인코딩( to_categorical(x,num_classes = word_size) )

from tensorflow.keras.preprocessing.text import Tokenizer
text="오랫동안 꿈꾸는 이는 그 꿈을 닮아간다"

token=Tokenizer()
token.fit_on_texts([text])
print(token.word_index)


# In[5]:


#원핫인코딩 방식으로 표현.
x =token.texts_to_sequences([text])#원핫인코딩 방식으로 표현 위해 사용.

print("\n텍스트 토큰화 결과:\n",x)


# In[7]:


#인덱스 수어 하나를 추가하여 원핫 인코딩 배열을 만들었다.

from tensorflow.keras.utils import to_categorical

word_size = len(token.word_index) +1
x = to_categorical(x,num_classes = word_size)
print(x)


# In[8]:





# In[9]:





# In[10]:





# In[ ]:




