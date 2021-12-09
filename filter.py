#!/usr/bin/env python
# coding: utf-8

# In[3]:


my_list = [1,14,53,72,22,99]


# In[6]:


filtered_list = list(filter (lambda x:x>=50, my_list))
filtered_list


# In[12]:


names_list = ["John","Phil","Joe","Marleen","Jackle","Bruce","Mindy"]


short_names = list(filter(lambda name: len(name)<=4, names_list))

print(short_names)


# In[ ]:




