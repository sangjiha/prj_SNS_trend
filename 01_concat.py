#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[31]:


df = pd.read_csv('./crawling/youtube_naver_blog_concat.csv', index_col=0)


# In[32]:


data = pd.read_csv('./crawling/naver_blog_crawling_맛집.csv', index_col=0) 
print(data.info())
print(data.head())


# In[33]:


data = data.rename(columns={'content': 'title'})


# In[34]:


df = pd.concat([df,data], ignore_index=True)


# In[35]:


df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)


# In[36]:


df.to_csv('./crawling/youtube_naver_blog_concat2.csv')


# In[37]:


print(df.head())


# In[38]:


print(df.info())


# In[ ]:




