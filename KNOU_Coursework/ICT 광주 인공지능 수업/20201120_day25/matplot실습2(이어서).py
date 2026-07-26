#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

import matplotlib.font_manager as fm
#font_list = fm.findSystemFonts(fontpaths=None, fontext)
mpl.rc('font',family='MDSol')
mpl.rc('axes',unicode_minus=False)


# In[2]:


np.random.seed(2)

people =['남준', '정국', '태형', '호석']
y_pos = np.arange(len(people))

performance = 3+10 * np.random.rand(len(people))

error = np.random.rand(len(people))
print(performance)
print(error)

plt.title("Barh chart")
plt.barh(y_pos, performance, xerr=error, alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('x label')
plt.show()


# In[3]:


x = np.linspace(0.1, 2 * np.pi, 10)

plt.title("Stem Plot")
plt.stem(x,np.cos(x), '-.')
plt.show()


# In[4]:


labels = ['개구리', '돼지', '개', '통나무']
sizes=[20,30,45,10]
colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

explode = (0, 0.1, 0.2, 0)

plt.title("Pie chart")
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct='1.2f%%', shadow=True, startangle=90)

plt.show()


# In[5]:


np.random.seed(0)
x= np.random.randn(10000)

plt.title("histogram")
arrays, bins, patches = plt.hist(x, bins=20)
plt.show()


# In[6]:


np.random.seed(0)
X = np.random.normal(10,3,1000)
Y = np.random.normal(0,1,1000)
plt.title("Scatter plot")
plt.scatter(X,Y, color="purple", alpha=0.4)
plt.show()


# In[ ]:


#버블차트
N=30

X= np.random.rand(N)
Y= np.random.rand(N)
color = np.random.rand(N)

size =np.pi * (20 * np.random.rand(N) )**2
#아래 3줄정도 못침.. ㅜ.ㅜ


# In[9]:


get_ipython().system('pip install sklearn #여기서는 샘플로 써먹기 위한 데이터 용도로만 받음.')


# In[12]:


from sklearn.datasets import load_digits

digits = load_digits()

print(digits.images.shape)
digits


# In[13]:


X = digits.images[0]
print(type(X))
X


# In[16]:


plt.imshow(X, interplation='nearest',camp = plt.cm.bone_r)

plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.show()


# In[18]:


from mpl_toolkits.mplot3d import Axes3D
X= np.arange(-4,4,0.25)
Y= np.arange(-4,4,0.25)
XX, YY = np.meshgrid(X,Y)
RR = np.sqrt(XX**2 + YY**2)
ZZ = np.sin(RR)

fig = plt.figure()
ax=Axes3D(fig)
ax.set_title("3D Surface Plot")
ax.plot_surface(XX,YY,ZZ, rstride=1,cstride=1, cmap='hot')
plt.show()


# In[22]:


from mpl_toolkits.mplot3d import Axes3D

n=100
xmin,xmax, ymin,ymax, zmin,zmax = 0,20,0,20,0,50
cmin, cmax = 0,2

xs= np.array([(xmax-xmin) * np.random.random_sample() + xmin for i in range(n) ])
ys= np.array([(ymax-ymin) * np.random.random_sample() + ymin for i in range(n) ])
zs= np.array([(zmax-zmin) * np.random.random_sample() + zmin for i in range(n) ])
color= np.array([(cmax-cmin) * np.random.random_sample() + cmin for i in range(n) ])


fig = plt.figure(figsize=(6,6))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(xs,ys,zs,c=color,marker='*',s=100,cmap='Blues')
plt.show()


# In[26]:


# ax + by + cz = d 평면 그리기

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

a,b,c,d = 1,2,3,4

x = np.linspace(-1,1,10)
y = np.linspace(-1,1,10)

X,Y = np.meshgrid(x,y)
Z = (d - a*X - b*Y) / c

fig = plt.figure()
ax = fig.gca(projection="3d")

surf = ax.plot_surface(X, Y, Z)


# In[30]:


get_ipython().system('pip install seaborn')


# In[31]:


import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
type(iris)


# In[32]:


iris


# In[33]:


x = iris.petal_length.values
print(x)
sns.rugplot(x)
plt.show()


# In[34]:


sns.kdeplot(x)
plt.show()


# In[35]:


sns.pairplot(iris)
plt.show()


# In[37]:


sns.pairplot(iris,hue="species", markers=["o","s","D"])
plt.show()


# In[ ]:




