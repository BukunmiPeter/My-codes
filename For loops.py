#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
For loops can be used to 
-iterate through datasets e.g lists
- and to execute a block of codes in a certain number of times
"""


# In[23]:


#Executing codes a certain number of times
count=10
for number in range(3):
    count*=5
    print (number)
    print("Count: {}".format(count))
    """
    Code to train our algorithm
    """
print("Hello --This is not indented, hence not in the for loop.")


# In[24]:


#iterating through datasets e.g lists
my_list = [1,2,3,4,5,6,7,8,9]
my_string = "Hi there i like Python"
for element in my_list:
    element+=100
    print("Element Value:{}".format(element*10))
#for element in my_string:
    #print(element)


# In[ ]:




