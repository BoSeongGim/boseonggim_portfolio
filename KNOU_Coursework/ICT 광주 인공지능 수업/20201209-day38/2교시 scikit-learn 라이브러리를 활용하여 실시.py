#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from sklearn import datasets

from sklearn.cluster import KMeans#

iris = datasets.load_iris()

samples = iris.data

model = KMeans(n_clusters=3)

model.fit(samples)

labels = model.predict(samples)

x= samples[:, 0 ]
y= samples[:, 1 ]

plt.scatter(x,y,c=labels, alpha=0.5)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width(cm)')
plt.show()


# In[4]:


#비지도 학습 - 검증

import numpy as np
import pandas as pd

target = iris.target

species = np.chararray(target.shape, itemsize=150)


for i in range(len(samples)) : 
    if target[i] == 0:
        species[i] = 'setosa'
    elif target[i] == 1:
        species[i] = 'versicolor'
    elif target[i] == 2:
        species[i] = 'virginica'
        
df = pd.DataFrame({'labels':labels, 'species':species})
ct = pd.crosstab(df['labels'], df['species'])
print(ct)


# In[6]:


num_clusters = list(range(1,9))
inertias=[]
for i in num_clusters : 
    model = KMeans(n_clusters=i)
    model.fit(samples)
    inertias.append(model.inertia_)
    
plt.plot(num_clusters, inertias, '-o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()


# In[ ]:




