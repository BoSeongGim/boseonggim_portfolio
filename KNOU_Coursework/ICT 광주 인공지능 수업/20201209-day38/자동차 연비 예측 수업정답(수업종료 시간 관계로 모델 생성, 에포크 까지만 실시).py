#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pathlib #

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# In[2]:


#데이터 셋 
dataset_path = keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
print(dataset_path)


# In[3]:


column_names=["MPG","Cylinders","Displacement","Horsepower","Weight","Acceleration","Model Year","Origin"]


# In[4]:


raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=" ", skipinitialspace=True)

dataset = raw_dataset.copy()
dataset.tail()


# In[5]:


print(dataset.isnull().sum())
dataset = dataset.dropna()


# In[6]:


origin = dataset.pop('Origin')
dataset['USA'] = (origin == 1) *1.0
dataset['Europe'] = (origin == 2) *1.0
dataset['Japan'] = (origin == 3) *1.0
dataset.tail


# In[7]:


train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)


# In[8]:


sns.pairplot(train_dataset[["MPG","Cylinders","Displacement","Weight"]], diag_kind="kde")


# In[9]:


train_stats = train_dataset.describe()
train_stats.pop("MPG")


# In[10]:


train_stats = train_stats.transpose()
train_stats


# In[11]:


train_labels = train_dataset.pop('MPG')
test_labels=test_dataset.pop('MPG')


# In[12]:


def norm(x):
    return (x-train_stats['mean']) /train_stats['std']


# In[13]:


normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)


# In[14]:


model = tf.keras.Sequential()

model.add(keras.layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys()) ]))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(1))
optimizer = tf.keras.optimizers.RMSprop(0.001)


# In[15]:


model.compile(loss='mse',
                optimizer=optimizer,
              metrics=['mae','mse'])


# In[16]:


example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
print(example_result)


# In[17]:


class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0 : print('')
        print('.',end='')
EPOCHS = 1000   


# In[18]:


history = model.fit(
    normed_train_data, train_labels,
    epochs=EPOCHS, validation_split=0.2, verbose=0, 
    callbacks=[PrintDot()])#100번에 한번씪 점을 찍는 셈이다.


# In[19]:


import matplotlib.pyplot as plt

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure(figsize=(8,12))

  plt.subplot(2,1,1)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [MPG]')
  plt.plot(hist['epoch'], hist['mae'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mae'],
           label = 'Val Error')
  plt.ylim([0,5])
  plt.legend()

  plt.subplot(2,1,2)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$MPG^2$]')
  plt.plot(hist['epoch'], hist['mse'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mse'],
           label = 'Val Error')
  plt.ylim([0,20])
  plt.legend()
  plt.show()

plot_history(history)


# In[20]:


# patience 매개변수는 성능 향상을 체크할 에포크 횟수입니다
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(normed_train_data, train_labels, epochs=EPOCHS,
                    validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])

plot_history(history)


# In[ ]:





# In[ ]:




