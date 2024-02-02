# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:33:41 2024

@author: rcc
"""

#Unpack a Collection

    #If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.1
    
    #list
    
l =[1,2,3]

a,b,c = l

print(b)
print(a)
print(c)

    #tuple
t =("a", "b","c")

x , y, z =t 

print(x)
print(y)
print(z)


    #set
s ={ "aasima","jinal","riya"}

a, b, c = s;

print(a)
print(b)
print(c)