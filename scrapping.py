#!/usr/bin/env python
# coding: utf-8

# ## Web Scrapping using Beautiful Soup
# 
# ### Scrapping the lists of largest companies in the US based on revenue 2023

# In[1]:


pip install beautifulsoup4


# In[3]:


from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)


# In[4]:


soup.find('table')


# In[6]:


soup.find_all('table')[1] #--indexing


# In[10]:


table=soup.find('table', class_='wikitable sortable')


# In[11]:


print(table)


# In[21]:


world_titles=table.find_all('th')


# In[22]:


world_titles


# In[41]:


world_table_titles=[title.text.strip() for title in world_titles]

#.strip() - removes \n / cleans data

print(world_table_titles)


# In[24]:


import pandas as pd


# In[27]:


df = pd.DataFrame(columns=world_table_titles)
df


# In[32]:


column_data=table.find_all('tr')
column_data


# In[43]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    #print(individual_row_data)
    
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[44]:


df


# In[45]:


df.to_csv(r'C:\Users\otien\OneDrive\Documents\Work Pics\Work_Docs\companies.csv')


# In[ ]:





# In[ ]:




