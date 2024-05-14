#!/usr/bin/env python
# coding: utf-8

# ## Basic Exploratory Data Analysis on Las Vegas Strip

# In[4]:


# import the necessary Library

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


# load and read data file
las_vegas_strip = pd.read_csv(r'C:\Users\preci\Downloads\LasVegasTripAdvisorReviews-Dataset.csv') #copy the file path into the string
las_vegas_strip


# In[4]:


# check the first five rows
las_vegas_strip.head()


# ### Data Inspection and Manipulation

# In[5]:


# check last 5 rows
las_vegas_strip.tail()


# In[7]:


# Check data shape
las_vegas_strip.shape


# In[8]:


# check data columns
las_vegas_strip.columns


# In[9]:


# check for data types
las_vegas_strip.dtypes


# In[10]:


# check info about data
las_vegas_strip.info()


# In[11]:


# checking for missing values
las_vegas_strip.isnull()


# In[13]:


las_vegas_strip.isnull().sum()


# In[14]:


# you can visualize to confirm missing values
plt.figure(figsize =(10, 5))
plt.title('Visualizing missing values')
sns.heatmap(las_vegas_strip.isnull(), cbar = True, cmap = 'magma_r')


# In[15]:


# Do staticscal descriptive analysis of numerical values
las_vegas_strip.describe().astype('int')


# In[29]:


# A negative minimum value for memebership years was discovered while carrying out the dataset inspection and manipulation
# correcting negative value to positive value by replacing it with the mean value
las_vegas_strip['Membership Years'] = las_vegas_strip['Membership Years'].replace(1806, 0)
las_vegas_strip


# In[28]:


# Do staticscal descriptive analysis of numerical values
las_vegas_strip.describe().astype('int')


# ## Exploratory Data Analysis : Relationship, Insights and Visualization
# - Univariate Analysis
# - Bivariate Analysis
# - Multivariate Analysis
# 
# #### Univariate Analysis
# - considering one feature or variable of the data

# In[31]:


# How many hotels per country
count_hotels_country = las_vegas_strip['Country'].value_counts().sort_values(ascending = False)
count_hotels_country


# In[34]:


# Top 10 countries with the highest number of hotels
count_hotels_c_h = count_hotels_country.head(10)
count_hotels_c_h


# In[104]:


# Visualize using bar charts
ax = count_hotels_c_h.plot(kind = 'bar', figsize = (10, 5), title = 'Top 10 countries', xlabel = 'Country', 
                        ylabel = 'Count of hotels', legend = False)
# annotate
ax.bar_label(ax.containers[0], label_type = 'edge')

#pad the spacing between the number and edge of the figure
ax.margins(y = 0.1)

# show the visual
plt.show()


# In[38]:


count_tt = las_vegas_strip['Traveler Type'].value_counts().sort_values(ascending = False)
count_tt


# ### Observation
# - USA has the highest numbers of hotels 

# In[103]:


# Visualize using bar charts
ax = count_tt.plot(kind = 'barh', figsize = (10, 5), title = 'Count of traveller types', xlabel = 'Traveler Type', 
                        ylabel = 'Top traveller type', legend = False)
# annotate
ax.bar_label(ax.containers[0], label_type = 'edge')

#pad the spacing between the number and edge of the figure
ax.margins(y = 0.1)

# show the visual
plt.show()


# #### Observation
# - According to our dataset Couples are the most popular or common  traveller types

# ### Bivariate Analysis
# - Considering two variables agains each other

# In[42]:


# Summary statistics per hotels and ratings
las_vegas_strip.groupby('Hotel Name').Rating.describe().astype('int')


# In[50]:


las_vegas_strip.groupby('Hotel Name').Rating.median().sort_values()


# In[51]:


# view the distribution of rating by hotel name
sns.boxplot(data = las_vegas_strip, x = 'Rating', y = 'Hotel Name')
plt.show()


# ### Observation 
# - There are 8 hotels with 5 stars rating and Circus Circus Hotel & Casino Las Vegas has the least ratings of 3 stars.

# In[29]:


# countries and hotels with the highest reviews
hct_r = las_vegas_strip.groupby(['Country', 'Hotel Name'])['Hotel Reviews'].mean().astype('int').unstack('Hotel Name').head(10)
hct_r


# In[32]:


plt.figure(figsize=(15,15))
chart = sns.scatterplot(
    x='Country',
    y='Hotel Reviews', 
    data= las_vegas_strip,
    hue='Hotel Name',
    palette= 'deep')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='right')


# In[88]:


plt.figure(figsize = (12, 8))
corre1 = las_vegas_strip.corr()
sns.heatmap(corre1, annot = True)


# In[9]:


# Stay period with Highest number of Traveler types
lvs_tt= las_vegas_strip.groupby(['Stay Period', 'Traveler Type'])['Stay Period'].count()
lvs_tt


# In[26]:


las_vegas_strip.groupby(['Stay Period', 'Traveler Type'])['Stay Period'].count().unstack().plot(kind='bar', stacked=True, figsize = (20,8))
plt.show


# In[9]:


# Top five hotels by membership using pie chart
top3_loc =las_vegas_strip.groupby("Hotel Name")["Membership Years"].sum().head(5).sort_values()
top3_loc


# In[10]:


# Visuzlize Top 5 Hotels by membership years
explode= (0.1, 0, 0)
plt.pie(top3_loc, labels = top3_loc.index, autopct = '%1.1f', shadow = True, startangle= 140)
plt.title('Top 5 Hotels with Most Membership')
plt.show


# In[15]:


## countries with travel types

cot_loc = las_vegas_strip.groupby(['Country', 'Traveler Type'])['Country'].count()
cot_loc


# In[25]:


las_vegas_strip.groupby(['Country', 'Traveler Type'])['Country'].count().unstack().plot(kind='bar', stacked=True, figsize = (20,8))
plt.show()

