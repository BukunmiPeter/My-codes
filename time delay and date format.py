#!/usr/bin/env python
# coding: utf-8

# In[18]:


"""
- Access data from 
- out put the currency value of btc
- have the value automatically update every 5 secs
- out put the currency time and date

"""


# In[9]:


import requests
url = "https://api.lunarcrush.com/v2"
response= requests.get(url)


# In[10]:


response.json()


# In[13]:


import time
while 1==1:
    print("Jesus Reigns")
    time.sleep(5)


# In[33]:


import datetime
today= (datetime.datetime.now().strftime("%d,%b %Y %H:%M:%S"))
print(today)


# In[ ]:





# In[ ]:




