#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


num=random.randrange(1,100)
guessCheck="wrong"
print("Welcome to guess the Number !")


# In[ ]:


while guessCheck=="wrong":
    response = int(input("Enter a number b/w 1 and 100"))
    try:
        value=int(response)
    except ValueError:
        print("Error! Invalid Value. Please Try again")
    value=int(response)
    if value < num:
        print("the guessed number is lower than the original number, Pleaase try again")
    elif value > num:
        print("the guessed number is higer than the Original number , Please try again")
    else :
        print ("Congratulations You have guessed the correct number ")
        guessCheck=="Correct"

print (" THANK YOU")


# In[ ]:




