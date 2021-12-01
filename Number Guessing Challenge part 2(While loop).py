#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
create a program that: 
- chooses a number between 1-100
-Takes a users guess and tells them if they are coreect or not

- Bonus: Tell the user if their guess was lower or higher than the computer's number
"""


# In[ ]:


#Part 2 -- 
"""
Create the same number guessing game as before
make it so that the user only has to run the programme once and keep guessing until they get it right
"""


# In[2]:



import random as rn
while 1==1:
    comp_num = rn.randint(1,100)
    print(comp_num)
    print("Guess right and win a prize!")
    user_guessnum = int(input("Guess the number computer picked"))
    if user_guessnum > comp_num:
        print("Oops!You're wrong. Your guess was higher than the computer's number ")
        print("Your guess was {}, computer number was {}.".format( user_guessnum, comp_num))
    elif user_guessnum < comp_num:
        print("Oops!You're wrong. Your guess was lower than the computer's number ")
        print("Your guess was {}, computer number was {}.".format( user_guessnum, comp_num))
    else:
        print("HUrray You're correct!!")
        break
    


# In[ ]:





# In[ ]:




