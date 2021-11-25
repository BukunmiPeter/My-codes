#!/usr/bin/env python
# coding: utf-8

# In[29]:


fruit_list = ["Apple", "Banana", "Orange","moldy banana","Pear"]
for fruit in fruit_list:
     #print(fruit_list)
    if fruit == "moldy banana":
        continue
    else:
            print(fruit)
            print("process continues")


# In[31]:


fruit_list = ["Apple", "Banana", "Orange","moldy banana","Pear"]
for fruit in fruit_list:
   #print(fruit_list)
  if fruit == "moldy banana":
      break
  else:
          print(fruit)
          print("check")
  
print("moldy banana stopped the process")


# In[ ]:




