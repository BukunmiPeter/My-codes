#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
- Map using normal functions
- Map using lambda
- Map using lambda, multiple inputs
"""


# In[7]:


list_of_nums = [1,10,100,1000,2000]
list_of_large_nums = []

def divider(x):
    y=x/5
    return y

#map(name of the function, name of the list)
list_of_large_nums = list(map(divider, list_of_nums))


list_of_large_nums 


# In[10]:


old_nums = [1,2,3,4,5,6,7]
new_nums = list(map(lambda x: x+9, old_nums))
new_nums


# In[11]:


num_tuple = (2,4,6,8,10)
new_tuple = tuple(map(lambda num: num*1000, num_tuple))
print(new_tuple)


# In[12]:


list_one = [1,2,3,4,5]
list_two = [300,400,500,600,700]

list_three = list(map(lambda x,y: x+y, list_one,list_two))

print(list_three)


# In[ ]:




