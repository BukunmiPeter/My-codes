#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Create a game where: 
- User has to do something against the computer (e.g guess a random number, select a random element from a list)
-Have a condition where the user can lose lives based on their guess
-User has five lives per game
- when they run out of lives the game ends and they get a "Game over" message.
"""


# In[3]:


import random as rn
user_lives = 5
play= True
while play==True:
    comp_num= rn.randint(1,3)
    print(comp_num)
    user_guess = int(input("Guess the computer's number"))
          
    if comp_num != user_guess:
            user_lives-=1
            print("You lose. You now have {} lives left".format(user_lives))
              
    else:
        print("You win")
      
    if user_lives==0:
        print("Game over")
        break
       
       
            
    


# ## 

# In[ ]:




