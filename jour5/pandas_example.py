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


# In[ ]:




