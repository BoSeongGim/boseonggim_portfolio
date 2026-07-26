#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.preprocessing.text import text_to_word_sequence
#text_to_word_sequence메소드 : 케라스의 텍스트 전처리와 관련된함수.


# In[2]:


#
text = '해보지 않으면 해낼 수 없다'


# In[3]:


result = text_to_word_sequence(text)
print("\n원문:\n",text)
print("\n토큰화:\n", result)


# In[4]:


from tensorflow.keras.preprocessing.text import Tokenizer


# In[5]:


docs = [ '먼저 텍스트의 각 단어를 나누어 토큰화 합니다.',
         '텍스트의 단어로 토큰화 해야 딥러닝에서 인식됩니다.',
         '토큰화 한 결과는 딥러닝에서 사용할 수 있습니다.',
        ]


# In[6]:


token = Tokenizer()
token.fit_on_texts(docs)


# In[7]:


print("\n단어 카운트 : \n", token.word_counts)


# In[8]:


print("\n문장 카운트 :\n",token.document_count)


# In[9]:


print("\n각 단어가 몇 개의 문장에 포함되어 있는가? :\n",token.word_docs)


# In[10]:


print("\n각 단어에 매겨진 인덱스 값 :\n",token.word_index)

