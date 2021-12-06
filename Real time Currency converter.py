#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
-Find a working API where we can access currencies (preferably with USD as the base currency)
- Create a programme that can take a user currency and amount, and convert it into  USD

"""


# In[1]:


import requests
url = "https://api.exchangerate-api.com/v4/latest/USD"


# In[2]:


response= requests.get(url)


# In[3]:


data=response.json()


# In[4]:


data["rates"]["AED"]


# In[5]:


print("Hey, welcome to your best currency converter")

amount = int(input("Enter your amount"))
user_currency = input("Enter your currency").upper()
value = data["rates"][user_currency]*amount
print ("Your {} {} is {}usd".format(amount,user_currency,value))


# In[ ]:




