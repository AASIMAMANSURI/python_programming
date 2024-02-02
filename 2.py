# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:50:57 2024

@author: rcc
"""

# python  variables
    
    #A variable name must start with a letter or the underscore character
    #A variable name cannot start with a number
    #Python has no command for declaring a variable.
    #A variable is created the moment you first assign a value to it.


# var one =12
#this is not allowed .we cant put space between the variable name


A = 1
B = "AASIMA"

print(A)
print(B)

    #Variables do not need to be declared with any particular type, and can even change type after they have been set.
x="abc"
x =1
    
print(x)


    # if we want to specify the datatype to the variable we can do this with casting

a = int(10)
b = str(1002)
c =float(1800)

print(a)
print(b)
print(c)


    #we can get the data type of a variable with the type() function.
        
A = 1
B = "AASIMA"

    #only print will give blank line
print()

print(type(A))
print(type(B))
    

    #we can define string using sinlge '' or double qoutes ""
    #both will work
    
x ='aasima'
y = "aasima"

print(x)
print(y)


    #Variable names are case-sensitive.
    # "A"  and "a"  both are different 
    
a=10
A=20

print(a + A)
# this will give output as 30 .addtion of "A" ans "a"


     #Many Values to Multiple Variables in one line
     
x,y,z = 10 ,20.3 ,30;

print(x)
print(y)
print(z )


    #One Value to Multiple Variables in one line

a = b = c ="Aasima"

print(b)
print(a)
print(c)