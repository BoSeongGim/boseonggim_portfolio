#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import sys
import os
from tensorflow.keras.models import load_model

import matplotlib.pyplot as plt
import numpy as np

model = load_model('./model/my_model_cnn.h5')
#model.summary()
test_num1 = plt.imread('./model/minist_test/3.jpg')
test_num2 = plt.imread('./model/minist_test/5.jpg')
test_num3 = plt.imread('./model/minist_test/7.jpg')


# In[6]:


#!pip install opencv-python #없을 시 옆의 주석해제하여 설치실시.
import cv2

#test_num1 = cv2.cvtColor(test_num1, cv2.COLOR_BGR2GRAY)
#test_num2 = cv2.cvtColor(test_num2, cv2.COLOR_BGR2GRAY)
#test_num3 = cv2.cvtColor(test_num3, cv2.COLOR_BGR2GRAY)

plt.imshow(test_num1, cmap='Greys');
plt.show()
plt.imshow(test_num2, cmap='Greys');
plt.show()
plt.imshow(test_num3, cmap='Greys');
plt.show()

test_num1 = test_num1.reshape(1, 784).astype('float64')/255
test_num2 = test_num2.reshape(1, 784).astype('float64')/255
test_num3 = test_num3.reshape(1, 784).astype('float64')/255

print('The Answer 3 is ', model.predict_classes(test_num1))
print('The Answer 5 is ', model.predict_classes(test_num2))
print('The Answer 7 is ', model.predict_classes(test_num3))


# In[ ]:





# In[ ]:




