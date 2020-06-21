#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Eligible to vote r not
a=int(input("enter the value of a"))
if(a>18):
    print("a is eligible for voting")
else:
    print("a is not eligible for voting")


# In[4]:


# 2. even or odd
a=int(input("enter value of a"))
if(a%2)==0:
    print("the number is even")
else:
    print("the number is odd")


# In[5]:


# 3. Print the string in reverse order by using string index
a=str(input("enter a string:"))
print("reverse of the string is:")
print(a[::-1])


# In[6]:


# 4. Positive or negative using if-else
n=int(input("enter a number"))
if(n>0):
    print("number is positive")
else:
    print("number is negative")


# In[13]:


# 5.Roots of a quadratic equation using elif
import math
a=float(input("enter the coefficient a"))
b=float(input("enter the coefficient b"))
c=float(input("enter the coefficient c"))
d=b*b-4*a*c;
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("roots are real and equal",r1,"and",r2)
elif d==0:
    r1=-b/(2*a)
    print("roots are real and same",r1)
else:
    print("no real roots are there")


# In[8]:


# 6. positive or negative or zero using nested-if
num=float(input("enter a number"))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative number")


# In[11]:


# 7.To accept a number (1-5)and print the given number in words
number=(" " ,"one","two","three","four","five")
n=int(input("enter a number"))
print(number[n])


# In[16]:


# 8.To read a character and print the given character is vowel or consonant
ch=input("enter a character")
if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")


# In[ ]:




