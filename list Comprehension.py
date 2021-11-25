#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Quick way to create new lists
- Quick way to create list with condition (if x%2 ==0)
- Means to filter through a list with new condition
"""


# In[2]:


my_list = [x for x in range(100)]
print (my_list)


# In[5]:


for x in range(10):
    print(x)


# In[7]:


my_old_list = [number for number in range(50) if number%2==0]
print(my_old_list)


# In[8]:


my_ol_list = [number for number in range(50) if number%2!=0]
print(my_ol_list)


# In[9]:


fruit_list= ["apple","Banana","pear","Kiwi","moldy banana"]


# In[11]:


fresh_fruit_list = [fruit for fruit in fruit_list if fruit!= "moldy banana"]
print(fresh_fruit_list)


# In[ ]:




