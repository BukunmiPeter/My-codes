#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Generators - yield instead of return terminates local variables, yield "pauses"


# In[8]:


def a():
    y=6
    x= 5
    return y


# In[9]:


b= a()
print(b)


# In[1]:


def a():
    y=8
    x= 5
    yield x
    
    x+=1
    print(x)
    yield y


# In[2]:


example = a()


# In[3]:


next(example)


# In[4]:


next(example)


# In[ ]:




