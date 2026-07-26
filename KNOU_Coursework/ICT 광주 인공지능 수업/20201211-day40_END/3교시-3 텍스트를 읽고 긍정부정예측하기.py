#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import array


# In[2]:


docs=["너무 재밌네요", "최고예요", "참 잘만든 영화예요","추천하고 싶은 영화입니다", "한 번 더 보고 싶네요",
     "글쎄요","별로예요","생각보다 지루하네요","연기가 어색해요","재미없어요"]


# In[3]:


classes= array([1,1,1,1,1,0,0,0,0,0])


# In[4]:


from tensorflow.keras.preprocessing.text import Tokenizer


# In[5]:


token = Tokenizer()


# In[6]:


token.fit_on_texts(docs)


# In[7]:


print(token.word_index)


# In[8]:


x = token.texts_to_sequences(docs)
print("\n 리뷰텍스트 토근화 결과 :\n",x)


# In[9]:


from tensorflow.keras.preprocessing.sequence import pad_sequences
#패딩, 서로 다른 길이의 데이터를 4로 맞추어 줍니다.


# In[10]:


padded_x = pad_sequences(x,4)


# In[11]:


print("\n패딩 결과 :\n",padded_x)


# In[12]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten,Embedding

print("\n 딥러닝 모델 시작:\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


word_size = len(token.word_index)+1


# In[15]:


model = Sequential()
model.add(Embedding(word_size, 8, input_length=4))
model.add(Flatten())
model.add(Dense(1,activation='sigmoid') )
model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padded_x,classes,epochs=20)
print("\n Accuracy : %.4f" % (model.evaluate(padded_x, classes)[1]))


# In[ ]:




