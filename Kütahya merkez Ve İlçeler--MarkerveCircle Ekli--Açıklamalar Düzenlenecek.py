#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install folium ')


# In[3]:


import folium


# In[4]:


folium.Map(location=[39.4200, 29.9857])


# In[14]:


m = folium.Map(location=[39.4200, 29.9857])
folium.Marker(location=[39.4200, 29.9857], tooltip=" Kütahya", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.5470, 29.4914], tooltip=" Tavşanlı", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.0580, 30.1086], tooltip=" Altıntaş", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.2149, 29.8703], tooltip=" Aslanapa", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.1969, 29.6172], tooltip=" Çavdarhisar", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.8010, 29.6127], tooltip=" Domaniç", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[38.8552, 29.9762], tooltip=" Dumlupınar", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.3444, 29.2579], tooltip=" Emet", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[38.9929, 29.4012], tooltip=" Gediz", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.2465, 29.2359], tooltip=" Hisarcık", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[38.9953, 29.1215], tooltip=" Pazarlar", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.0896, 28.9787], tooltip=" Simav", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)
folium.Marker(location=[39.0249, 29.2201], tooltip=" Şaphane", popup = ' Kadın nufüs 100k erkek nufüs 200k çocuk nufüs 50k.').add_to(m)


folium.CircleMarker(location=(39.4200, 29.9857),radius=100, fill_color='Orange').add_to(m)
folium.CircleMarker(location=(39.5470, 29.4914),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.0580, 30.1086),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.2149, 29.8703),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.1969, 29.6172),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.8010, 29.6127),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(38.8552, 29.9762),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.3444, 29.2579),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(38.9929, 29.4012),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.2465, 29.2359),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(38.9953, 29.1215),radius=40, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.0896, 28.9787),radius=50, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.0249, 29.2201),radius=40, fill_color='blue').add_to(m)

from folium import plugins

minimap = plugins.MiniMap()
m.add_child(minimap)
m


# In[ ]:




