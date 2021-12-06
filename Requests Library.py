#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
REQUESTS
 http requests GET  POST
- Install requests pip install requests, pip3 install requests, conda install requests (for ananconda users)
- import
- get
-status codes
- content
json() - "https://api.exchangerate-api.com/v4/latest/USD"
- json files. Getting the info you need
- Fining APIs (Aoplication Programming Inteface)

"""


# In[1]:


import requests


# In[10]:


#http response codes   200 & 300 okay, 400 & 500 not okay read more


url = "http://www.google.com"

requests.get(url)


# In[11]:


response = requests.get(url)


# In[13]:


#response.content


# In[19]:


#.json 

myJson = { "John": 23, "Peter":45, "new":{"a":1, "b":2}}


# In[22]:


myJson["new"]["a"]


# In[26]:


currencyurl = "https://api.exchangerate-api.com/v4/latest/USD"
response=requests.get(currencyurl)


# In[29]:


data= response.json()


# In[31]:


data["rates"]["AED"]


# In[32]:


data


# In[35]:


response = requests.get("http://jsonrates.com/get/?from=USD&to=EUR")


# In[36]:


response.json()


# In[ ]:




