#!/usr/bin/env python
# coding: utf-8

#     1. Predict the output
#         s1 = 'gaurav'
#         s2 = 'tuteur.py@gmail.com'
#         print(len(s1),len(s2)
#         -------------------------
#         Answer: 6 19

# In[2]:


s1 = 'gaurav'
s2 = 'tuteur.py@gmail.com' 
print(len(s1),len(s2))


#     2. WAP to input a string and print its length

# In[4]:


s1 = input("Enter a string: ")
print(len(s1))


#     3. WAP to input 2 number and print their sum and difference

# In[6]:


n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
print("The Sum of two numbers: ", n1+n2)
print("The Difference of two numbers: ", n1-n2)


#     4. Predict Output:
#         s1 = 'ab'
#         s2 = 'de'
#         s3 = s1+s2
#         print(s3)
#         ------------
#         Answer: abde

# In[9]:


s1 = 'ab'
s2 = 'de'
s3 = s1 + s2 
print(s3)


#     6. Predict Output
#         s1='ab'*4
#         print(s1)
#         ----------
#         Answer: abababab

# In[10]:


s1='ab'*4
print(s1)


#     7. Predict Output:
#         s1='ab\n'*4
#         print(s1)
#         -----------
#         Answer:
#         ab
#         ab
#         ab
#         ab

# In[11]:


s1='ab\n'*4
print(s1)


#     8. WAP to input a string s and a number n.Print s n times on the screen, each should appear in a separate line(donot use any kind of loops and use multiplication operator)

# In[26]:


s = input("Enter a string")
n = int(input("Enter a number"))
print(f'{s}\n'*n)


#     9. Predict Output:
#         res = print("Gaurav")
#         print(res)
#         ---------
#         Answer:
#         Gaurav
#         None

# In[27]:


res = print("Gaurav")
print(res)


#     10. Predict the Output:
#         res = len('tuteur.py@gmail.com')
#         print(type(res))
#         -----------------------------
#         Answer: int
#         

# In[28]:


res = len('tuteur.py@gmail.com')
print(type(res))


#     11. Predict Output:
#         s1 = 'gaurav'
#         s2 = 'tuteur.py@gmail.com'
#         s3 = s1 + '\n' + s2
#         print(type(s3))
#         print(len(s3))
#         -------------------------
#         Answer: 
#         str
#         25 + new line as 1 count = 26

# In[30]:


s1 = 'gaurav'
s2 = 'tuteur.py@gmail.com'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))


#     12. Find the name of the function to find the square root(see all the options available in dir() of math)
#     --------------------------------------------------------------------------------------------------------
#     Answer: sqrt

# In[39]:


import math
dir(math)


#     13. WAP to input a number and print its square root

# In[41]:


n = int(input("Enter a number: "))
print(math.sqrt(n))


#     14. WAP to input 4 numbers from User and print their average

# In[42]:


n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the second Number: "))
n3 = int(input("Enter the third Number: "))
n4 = int(input("Enter the fourth Number: "))
print((n1+n2+n3+n4)/4)


#     15. Use the help function to check what abs function in python does

# In[44]:


help()


#     -----------------------------------
#     16. What is the Output of this code when you run from the python interpreter
#         print(__name__)

# In[48]:


print(__name__)


#     17.What is the Output of this code when you run from the python script
#             print(__name__) 

#     18. Does dir of int class contain an attribute __name__ (Yes/No)
#     Answer:

# In[50]:


dir(int)


#     19. Predict the Output:
#         print(__name__)
#         print(__builtin__.__name__)
#         print(int.__name__)

# In[51]:


print(__name__)
print(__builtin__.__name__)
print(int.__name__)

