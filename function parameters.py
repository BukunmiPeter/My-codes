#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
def f(x): 3x + 1

what is f(2) = 7

def f(x,y): 3x + 2y
what is f(3,2) = 13

"""


# In[10]:


def function_name(one,second_para):
    print(one)
    print("This is the second brother {}".format(second_para))


# In[12]:


function_name("John","Michael")


# In[18]:


def multiplier (first, sec, th, ri, jd):
    third = first*sec
    print(third)
    print(jd)


# In[19]:


multiplier (4,5,6,7,8)


# In[24]:


def greeter(name):
    print("Hi there {}. I hope you have a lovely day.".format(name))


# In[25]:


greeter("Michael")


# In[51]:


current_balance = 1000


# In[52]:


def withdraw(balance, amount):
    balance -=amount
    print("You have withdrawn: {}. Your balance is:{}".format(amount, balance))
    return balance


# In[54]:


current_balance = withdraw(current_balance, 10)


# In[ ]:




