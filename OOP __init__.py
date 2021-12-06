#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animals:
    def __init__(self,size,noise,colour,num_of_legs):
        self.size = size
        self.noise = noise
        self.colour = colour
        self.num_of_legs = num_of_legs 


# In[2]:


tiger = Animals(100,"Rwaaar", "orange and black", 4)
orangutan = Animals(150,"Oooo", "Orange",2)
dolphin = Animals(88,"reeee","Grey",0)


# In[5]:


tiger.num_of_legs


# In[6]:


orangutan.size


# In[7]:


dolphin.colour


# In[9]:


class House:
    def __init__(self,address,num_of_rooms, market_value,distance_from_school, SqM,back_garden):
        self.address = address
        self.num_of_rooms = num_of_rooms
        self.market_value = market_value
        self.distance_from_school = distance_from_school
        self.SqM = SqM
        self.back_garden = back_garden
    


# In[10]:


house_1024 = House("101 fake street", 8, 10000, 2, 120, True)
house_3402 = House("103 Great road", 100,100000, 0.5, 300, True)


# In[11]:


house_1024.distance_from_school


# In[12]:


house_3402.SqM


# In[ ]:




