#!/usr/bin/env python
# coding: utf-8

# In[15]:


word = "word"
myList = [1,2,4,"hi",[7,8,["a","c","r"],9],5,"python",word]


# In[16]:


a =myList[4][2][2]
print(a)


# In[19]:


a_list = [1,6,77,"bear",5700,"cheese",8,700000,11,43]


# In[20]:


a_list[3]


# In[21]:


a_list[3:6]


# In[22]:


a_list[1:8]


# In[24]:


a_list[:5]


# In[25]:


a_list[:]


# In[27]:


a_list[1:8:2]


# In[28]:


a_list[:8:3]


# In[29]:


a_list[::2]


# In[30]:


a_list[::-1]


# In[36]:


a_list[8:4:-1]


# In[ ]:


"""
Create a list 
- Add a list in this list
-Add a list within this List
(Each list must contain at least four elements)
=========
Access the first two elements of the list within the original list 
Access the last three elements of the list within the list 
output the whole thing backwards
"""


# In[44]:


task_list = [1,2,3,[8,[12,13,14,15],9,10,11],4,5,6,7]


# In[51]:


task_list[3][:2]


# In[53]:


task_list[3][1][1:]


# In[54]:


task_list[::-1]


# In[ ]:




