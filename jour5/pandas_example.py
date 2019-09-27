#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

df = pd.read_csv("train.csv")
df
# df['Name']
# df.columns
# df.describe()

df['Ticket']


# In[38]:


import re
import numpy as np

def extract_number(ticket):
    result = re.findall('\d+$', ticket)
    if len(result):
        return result[0]
    return np.nan
df['TicketClean'] = df['Ticket'].map(extract_number)

#Filtre
df[df['Cabin'].isna()]


# In[39]:


# Combien il y a de femmes / hommes

# Proportion de femmes qui meurt
# Proportion d'hommes qui meurt

# Hist des ages survivants
# Hist ages des morts


# In[50]:


print(len(df[df["Sex"] == "male"]))
print(len(df[df["Sex"] == "female"]))

p_femmes_mort =  len(df[(df["Sex"] == "female") & ~df["Survived"]]) / len(df[df["Sex"] == "female"])
p_hommes_mort =  len(df[(df["Sex"] == "male") & ~df["Survived"]]) / len(df[df["Sex"] == "male"])

print(p_femmes_mort)
print(p_hommes_mort)

df[df["Survived"] == 1]["Age"].hist(bins=15)


# In[51]:



df[df["Survived"] == 0]["Age"].hist(bins=15)


# In[57]:


import re

def extract_title(name):
    return re.findall("\w+\.", name)[0]

df["Title"] = df['Name'].map(extract_title)
print(df["Embarked"].unique())
print(df["Title"].unique())


# In[58]:


dataset = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]]

dataset["Sex"] = df["Sex"].map({"male": 0, "female": 1})
dataset["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})


# In[70]:


dataset.count()
list_title = list(df["Title"].unique())

dataset["Title"] = df["Title"].map(lambda x: list_title.index(x) )

clean_data = dataset.dropna()


# In[71]:


clean_data


# In[73]:


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5).fit(
    clean_data[:100].drop(columns="Survived"),
    clean_data[:100]["Survived"])

score = knn.score(clean_data[100:200].drop(columns="Survived"),
    clean_data[100:200]["Survived"])
print(score)


# In[ ]:




