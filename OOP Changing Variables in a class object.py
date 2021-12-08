#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Person:
    def __init__(self, age):
        self.age=age
    
    def plus_year(self):
        self.age+=1
    
    def show_age(self):
        print("Your age is {}.".format(self.age))


# In[4]:


me = Person(40)


# In[10]:


me.plus_year()


# In[11]:


me.show_age()


# In[1]:


class Warrior:
    def __init__(self,name,strength,health):
        self.name = name
        self.strength = strength 
        self.health = health
        
        
    def report(self):
        print("Hi {}. Your strength is {} and your health is {}.".format(self.name, self.strength, self.health))
        
    def heal(self):
        self.health +=1
    
    def damage(self,dmg_amount):
         self.health -= dmg_amount
        
    def workout(self):
        self.strength += 1


# In[2]:


warrior_one = Warrior("Reginald the warrior", 10, 100)


# In[3]:


warrior_one.strength


# In[10]:


warrior_one.report()


# In[7]:


warrior_one.heal()


# In[9]:


warrior_one.damage(20)


# In[ ]:




