#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Method_class:   
    x = "Hi there"

    def subtractor(num_one, num_two):
        num_three = num_one - num_two
        print("{}-{} = {}.".format(num_one,num_two,num_three))
        
    def print_stuff(a,b):
        print(a,b)


# In[10]:


Method_class.subtractor(24,5)


# In[13]:


Method_class.print_stuff("Hi", 5)


# In[ ]:




