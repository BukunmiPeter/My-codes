#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Basic Dictionaries
-Acccesing a value
-Accesing all key:value pairs
-printing all values
-Changing a value
-Adding a key:value pair
-Removing  a key:value pair
"""


# In[1]:


my_dict = {"John":23, "Michael":45, "Fiona":29}


# In[4]:


#Acccesing a value
my_dict["Michael"]


# In[5]:


#Accesing all key:value pairs
for pair in my_dict:
    print(pair)


# In[6]:


#printing all values
for pair in my_dict:
    print(my_dict[pair])


# In[8]:


#Changing a value
my_dict["John"]= 34
print(my_dict)


# In[10]:


#Adding a key:value pair
my_dict["Bob"]= 37
print(my_dict)


# In[11]:


my_dict.pop("Fiona")


# In[12]:


print(my_dict)


# In[ ]:




