#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # 1. Read the dataset to python environment.

# In[4]:


data=pd.read_excel('C:\\Users\\Simi.Jacob\\OneDrive - EY\\ICT\\assig1\\iris.xls')
data


# # 2. Display the columns in the dataset.

# In[5]:


data.columns


# In[6]:


data.info()


# # 3. Calculate the mean of each column of the dataset.
# 

# In[7]:


data.mean()


# # 4. Check for the null values present in the dataset.

# In[8]:


data.isna().sum()


# # 5. Perform meaningful visualizations using the dataset. Bring at least 3 visualizations

# In[18]:


gf=data.plot(figsize=(10,10),title="Iris Data")
gf.set_xlabel("X- axis")
gf.set_ylabel("Y-axis")


# In[28]:


data.iloc[0][0:4].plot(kind='bar')


# In[37]:


data.plot(kind='hist', stacked=True, bins=100,figsize=(10,10),title="Iris dataset",orientation='horizontal')


# In[39]:


data.hist(figsize=(10,10),color='red')


# In[42]:


data.plot.scatter(x="SL",y="PL")


# In[ ]:




