#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Create a program that emulates a twister turner
Each time the program s run it outputs one of each of the following(at random);
one color(red, green, blue, yellow)
left hand or right hand or left foot or right foot
"""


# In[ ]:


"""
Solution
output choice from list of colors
- Do the same body parts
Output results
"""


# In[34]:


import random
colors = ["red", "green","Yellow", "blue"]
body_parts = ["Right foot", "Left foot", "Right hand", " Left hand"]
color_random= random.choice(colors)
body_partsrandom= random.choice(body_parts)
print("Twister Turner says {},{}.".format(color_random,body_partsrandom))


# In[ ]:




