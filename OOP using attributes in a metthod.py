#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Animals:
    def __init__(self, name, colour,noise):
        self.name= name
        self.colour =colour
        self.noise = noise
    
    def describe(self):
        print("The {} is {} and it makes the noise {}.".format(self.name, self.colour, self.noise))


# In[13]:


owl = Animals("owl","brown","Twit tawoo")
dog = Animals("dog", "black", "barrk")


# In[14]:


owl.noise


# In[15]:


dog.describe()


# In[ ]:





# In[ ]:




