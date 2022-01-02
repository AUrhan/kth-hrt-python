#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install folium ')


# In[2]:


get_ipython().system('pip install geopandas ')


# In[2]:


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import PIL
import io


# In[6]:


data = pd.read_csv('https://raw.githubusercontent.com/AUrhan/kth-hrt-python/main/kth.csv')
data.head()


# In[14]:


turkey = gpd.read_file('https://raw.githubusercontent.com/AUrhan/kth-hrt-python/main/kthk.json')
turkey.plot()


# In[18]:


#combine data with world gpd gdf
merge = turkey.join(data)


# In[19]:


merge.plot()


# In[24]:


ax = merge.plot(cmap='OrRd', figsize=(10,10), legend=True, edgecolor='black', linewidth=0.4)


# In[28]:


ax = merge.plot(cmap='OrRd',column='IL-ILCE'/'TOPLAM'/'Erkek-Male'/'Kadin-Female'/'Cocuk-Child', figsize=(10,10), legend=True, edgecolor='black', linewidth=0.4)


# In[ ]:




