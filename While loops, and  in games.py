#!/usr/bin/env python
# coding: utf-8

# In[3]:


#for loops
for i in range(10):
    print(i)


# In[6]:


#While loops
i=0
while i<10:
    print(i)
    i+=1


# In[ ]:


play = True

while play==True:
    #This can be any condition e.g while 1==1
    real_number = 10
    user_guess = int(input("Guess the number"))
    if user_guess == real_number:
        #play = False (using while loop break will make the game to stop immediately the condition is met without showing the rest of the game)
        break
    input ("Write more things") 
    print("...more of the game")
    print("...more of the game")
    print("...more of the game")
    print("...more of the game")
        
print("THis is outside the while loop. Game has ended")


# In[ ]:




