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

model.summary()
n=3

test_num = [[0]*n for _ in range(n)]

test_num1 = plt.imread('./model/minist_test/3.jpg')
test_num2 = plt.imread('./model/minist_test/5.jpg')
test_num3 = plt.imread('./model/minist_test/7.jpg')


# In[2]:


#!pip install opencv-python #없을 시 옆의 주석해제하여 설치실시.
import cv2
for i in range(3):
    test_num[i] = cv2.cvtColor(test_num1, cv2.COLOR_BGR2GRAY )

    plt.imshow(test_num[i], cmap='Greys');
    plt.show()

    test_num[i] = test_num[i].reshape(1,784).astype('float64') /255

    print('The Answer 3 is ', model.predict_classes(test_num[i]))


# In[ ]:





# In[ ]:




