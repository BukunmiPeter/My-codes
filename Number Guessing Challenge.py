#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
create a program that: 
- chooses a number between 1-100
-Takes a users guess and tells them if they are coreect or not

- Bonus: Tell the user if their guess was lower or higher than the computer's number
"""


# In[3]:


print("Guess right and win a prize!")
user_guessnum = int(input("Guess the number computer picked"))
import random as rn
comp_num = rn.randint(1,100)
if user_guessnum > comp_num:
    print("Oops!You're wrong. Your guess is higher than the computer's number ")
elif user_guessnum < comp_num:
    print("Oops!You're wrong. Your guess is lower than the computer's number ")
else:
    print("HUrray You're correct!!")


# In[ ]:




