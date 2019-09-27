#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np

points = np.random.randint(0, 10, (100,2))


# In[10]:


print(points.shape)
import matplotlib.pyplot as plt

plt.scatter(points[:,0], points[:,1])

plt.show()


# In[12]:


import matplotlib.pyplot as plt

plt.plot(points[:,0])
# plt.plot(points[:,1])

plt.show()


# In[20]:


import matplotlib.pyplot as plt

plt.plot([x*0.1 for x in range(30)], [x**2 for x in range(30)])
# plt.scatter(range(30), [x**2 for x in range(30)])

plt.show()


# In[55]:


print(points.shape)
import matplotlib.pyplot as plt

# points2 = np.random.randint(10, 20, (100,2))
points = 8 * np.random.randn(200,2) + np.array([10,10])
points2 = 6 * np.random.randn(200,2) + np.array([30,42])

plt.scatter(points[:,0], points[:,1], c='r')
plt.scatter(points2[:,0], points2[:,1], c='b')

plt.show()


# In[28]:


points2 = np.random.randint(10, 20, (100,2))

all_points = np.concatenate([points, points2], axis=0)
all_labels = np.array([0] * 100 + [1] * 100)
print(all_points.shape)
print(all_labels.shape)


# In[30]:


import matplotlib.pyplot as plt

plt.scatter(all_points[:,0], all_points[:,1], c=all_labels, cmap='Set1')

plt.show()


# In[56]:


from sklearn.mixture import GaussianMixture

# points2 = np.random.randint(8, 20, (200,2))
points = 8 * np.random.randn(200,2) + np.array([10,10])
points2 = 6 * np.random.randn(200,2) + np.array([30,42])

all_points = np.concatenate([points, points2], axis=0)
print(all_points.shape)
print(all_labels.shape)

gmm = GaussianMixture(n_components=2)
res = gmm.fit(all_points)

print(res.means_)
print(res.covariances_)
print(res.weights_)
print(gmm.predict(all_points))

plt.scatter(
    all_points[:,0],
    all_points[:,1],
    c=gmm.predict(all_points),
    cmap='Set1')

plt.show()


# In[48]:


from sklearn.cluster import DBSCAN
from itertools import product

for eps, min_s in product([0.5, 1, 1.5, 3, 5], [2, 4, 7, 12]):
    db = DBSCAN(eps=eps, min_samples=min_s)
    res = db.fit(all_points)
    nb_class = len(set(res.labels_))
    print(f"eps={eps} , min_s={min_s}, classes= {nb_class}")

db = DBSCAN(eps=1.5, min_samples=12)
res = db.fit(all_points)
nb_class = len(set(res.labels_))
print(f"eps={eps} , min_s={min_s}, classes= {nb_class}")

plt.scatter(
    all_points[:,0],
    all_points[:,1],
    c=res.labels_,
    cmap='Set1')

plt.show()


# In[50]:


help(np.random.randn)


# In[ ]:




