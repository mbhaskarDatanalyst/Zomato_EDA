#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df=pd.read_csv(r"C:\Users\Mithu Bhaskar\OneDrive\Desktop\Git Repositories\Mbhaskar_Portfolio_website\Zomato_Data.csv", encoding='latin-1')


# In[5]:


df.head(10)


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.columns


# In[10]:


##Find missing values
df.isnull().sum()


# In[11]:


#finding columns having null values using Features as a temporary column
[features  for features in df.columns  if df[features].isnull().sum()>1]


# In[12]:


sns.heatmap(df.isnull(),yticklabels=False, cbar=False,cmap='viridis')


# In[13]:


df.cc=pd.read_excel(r"C:\Users\Mithu Bhaskar\OneDrive\Desktop\Git Repositories\Mbhaskar_Portfolio_website\Country-Code.xlsx")


# In[14]:


df.cc.head()


# In[15]:


df.columns


# In[16]:


#left join on the basis of country
f_df=pd.merge(df,df.cc,on='Country Code', how='left')


# In[17]:


f_df.head()


# In[18]:


f_df.Country.value_counts()


# In[19]:


country_names=f_df.Country.value_counts().index


# In[20]:


country_values=f_df.Country.value_counts().values


# In[33]:


#Pie-chart= Top 5 countries that uses zomato
plt.pie(country_values[:5],labels= country_names[:5],autopct='%1.2f%%')


# # Observation: Zomato having  maximum transaction from India and after that USA is there

# In[22]:


f_df.columns


# In[23]:


ratings=f_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[24]:


ratings


# # Observations:
#     
#     1) Rating  between 4.5 to 4.9----> Excellent
#     2) Rating between 4.0 to 4.4----->very good
#     3) Rating between 3.5 to 3.9----->good

# In[36]:


plt.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Aggregate rating', y='Rating Count',hue='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'])
# we can also  use PALETTE  function to assign colors of your choice


# # Observation:
#     -Not rated count is very high
#     -Maximum rating is between 2.5 to 3.4
# 

# In[35]:


#Countplot
sns.countplot(x='Rating color',data=ratings,hue='Rating color',palette=['white','red','orange','yellow','green','green'])


# In[42]:


#Find countries giving 0  ratings
f_df[f_df['Rating color']=='White'].groupby('Country').size().reset_index()


# # Observation
# Indian gives the highest rating of 0

# In[50]:


#Which country using which currency
f_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index().rename(columns={0:'Currency Count'})


# In[52]:


##Which country do have online deliveries options
f_df[f_df['Has Online delivery']== 'Yes'].Country.value_counts()


# In[57]:


f_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# # Observation
# 1. Online deliveries are available in India and UAE

# In[ ]:


##Create a piechart for cities distribution


# In[62]:


f_df.City.value_counts().reset_index()


# In[67]:


city_val=f_df.City.value_counts().values
city_labels=f_df.City.value_counts().index


# In[70]:


plt.pie(city_val[:5],labels=city_labels[:5], autopct='%1.2f%%')


# In[ ]:


##Top 10 cuisins


# In[71]:


f_df.columns


# In[94]:


f_df.Cuisines.value_counts().values[:10]


# In[93]:


f_df.Cuisines.value_counts().reset_index()[:10]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




