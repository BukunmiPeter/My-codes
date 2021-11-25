#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Have currency rates in dictionary, key= currrencies
input amount
input currency
convert the amount by multiplying by dictionary value
-output
"""


# In[28]:


currency_rate = {"GBP":0.75,"EUR":0.89,"JPY":115.34,"CHF":0.93}
user_amount= int(input ("input amount in USD"))
user_currency= input("input currency you want to convert to").upper()
if user_currency == "GBP":
    converted_amount = user_amount * currency_rate["GBP"]
    print("Your {}usd is equivalent to{} pounds ".format(user_amount, converted_amount))
elif user_currency == "EUR":
    print("Your {}usd is equivalent to{} euros ".format(user_amount, converted_amount))
    
    converted_amount = user_amount * currency_rate["EUR"]
elif user_currency == "JPY":
    converted_amount = user_amount * currency_rate["JPY"]
    print("Your {}usd is equivalent to{} yen".format(user_amount, converted_amount))

elif user_currency == "CHF":
    converted_amount = user_amount * currency_rate["CHF"]
    print("Your {}usd is equivalent to{} swiss ".format(user_amount, converted_amount))
else:
    print("You entered an invalid currency. Try again!")


# In[ ]:




