#!/usr/bin/env python
# coding: utf-8

# In[14]:


#import necessary Python libraries
import pandas as pd
import folium
import datetime
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt 

# read csv files
df1 = pd.read_csv('2020.csv') # the data is published on Kaggle  https://www.kaggle.com/datasets/onlyrohit/crimes-in-chicago
df2 = pd.read_csv('2021.csv')
df3 = pd.read_csv('2022.csv') 
pop = pd.read_excel('chicagopop.csv') # population of each community area on Wikipedia and the region they belong  https://en.wikipedia.org/wiki/Community_areas_in_Chicago


# In[15]:


df1 = pd.concat([df1, df2], axis=0)  #concat all the dataframes of each year into 1 dataframe
df = pd.concat([df1, df3], axis=0)
 

#drop unecessary columns that we will not use
df = df.drop(columns=['Case Number','IUCR','Description', 'Beat', "District", "Ward", "FBI Code", "X Coordinate", "Y Coordinate", "Updated On",'Location'])
df = df.dropna()  #drop na values


# In[16]:


pop.head(3)  #check that we can see the data


# In[17]:


df.head(3)


# In[18]:


#we observe that we can insert the community area number of each neighbourhood by reseting the index + 1 
pop = pop.reset_index()
pop.rename(columns={'index':'Community Area'}, inplace=True)

# increase the index of all rows by 1
pop['Community Area'] = pop['Community Area'] + 1


# In[19]:


from datetime import datetime
# extract Hour from Date column and store it in new columns called 'Month','Hour'
df['Hour'] = df['Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M:%S %p').hour)

# extract month from Date column and store it in a new column called 'Month'
df['Month'] = df['Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M:%S %p').month)


# In[20]:


df = pd.merge(df, pop, on='Community Area', how='inner') #merge with pop, so all the data is in df dataframe


# In[21]:


df.head(3)


# In[22]:


import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster

m = folium.Map([41.881,-87.623], zoom_start=14) #latitude and longitude of Chicago 
latlon_2022 = df[['Latitude','Longitude']]
crime_heatmap = folium.Map(location= [41.881,-87.623], 
                           tiles = "Stamen Toner",
                           zoom_start = 12)
HeatMap(latlon_2022, min_opacity=0.05).add_to(crime_heatmap)
crime_heatmap


# In[23]:


f = df.groupby('Name').count()
areaname = f[['ID']]
areaname = areaname.reset_index()
areaname = areaname.rename(columns = {'ID':'Crime Records'})
neighbourhoods = pd.merge(pop, areaname, on='Name', how='inner')
neighbourhoods['Crime Rate'] = neighbourhoods['Crime Records'].div(neighbourhoods['Population'])
neighbourhoods['Victims per 100.000 People'] = neighbourhoods['Crime Records'].div(neighbourhoods['Population']) * 100000


# In[24]:


neighbourhoods.sort_values('Crime Rate',ascending = False).head(5)


# In[25]:


neighbourhoods.sort_values('Crime Rate',ascending = False).tail(5)


# In[26]:


from folium import plugins
from folium.plugins import MarkerCluster

df['Date'] = pd.to_datetime(df['Date'])
may31 = df[df['Date'].dt.date == pd.to_datetime("2020-05-31").date()]
may31 = may31[may31['Name']== 'Near West Side']

#Map points of the crime events
m2 = folium.Map([41.8668,-87.6664], zoom_start=14) #Latitude & Longitude of Near West Side
for index, row in may31.iterrows():
      folium.CircleMarker([row['Latitude'], row['Longitude']],
                        radius=5,
                        popup=row['Primary Type'],
                        fill_color="#3db7e4", 
                       ).add_to(m2)

dfmatrix = may31[['Latitude', 'Longitude']].values
# plot heatmap
m2.add_child(plugins.HeatMap(dfmatrix, radius=15))

#now we find the centroid and add it to the plot
lat = []
long = []
for index, row in may31.iterrows():
    lat.append(row["Latitude"])
    long.append(row["Longitude"])
lat1=sum(lat)/len(lat)
lat2=sum(long)/len(long)
folium.CircleMarker([lat1,lat2],
                        radius=5,
                        popup="CENTER LOCATION",
                        color='black',
                        fill_color="#3db7e4", 
                       ).add_to(m2)
m2

