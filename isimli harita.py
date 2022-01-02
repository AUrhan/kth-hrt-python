#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install folium ')


# In[2]:


get_ipython().system('pip install geopandas ')


# In[3]:


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import PIL
import io
import folium


# In[4]:


data = pd.read_csv('https://raw.githubusercontent.com/AUrhan/kth-hrt-python/main/kth.csv')
data.head()


# In[37]:


turkey = gpd.read_file('https://raw.githubusercontent.com/AUrhan/kth-hrt-python/main/kthk.json')
turkey.plot()


# In[35]:


#combine data with world gpd gdf
merge = turkey.join(data)
merge.plot()


# In[ ]:





# In[45]:


ax = merge.plot(cmap='OrRd', figsize=(10,10), legend=True, edgecolor='black', linewidth=0.4)
classification_kwds={'bins':[1000,2000,5000,10000,20000,50000,70000,100000,150000,200000,500000,600000]}


# In[68]:


ax=merge.plot(cmap='OrRd', figsize=(9,9),legend=True,edgecolor='purple',linewidth=0.4, scheme='user_defined', 
classification_kwds={'bins':[1000,2000,5000,10000,20000,50000,70000,100000,150000,200000,500000,600000]})
ax.set_title('Kütahya Nüfus Haritası', fontdict={'fontsize':20}, pad=12.5)


# In[ ]:




