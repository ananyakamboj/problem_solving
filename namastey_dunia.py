#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:04:06 2022

@author: ananyakamboj
"""

print("Namastey Duniya")
a= 123
print(a)

b= 'v' 
print(b)


c= True
print(c)

d= 1.23
print(d)

import sys
 
# Getting size using getsizeof() method and lately
# printing the same.
a = sys.getsizeof(1.234)
print(a)

a= -97

print(str(a))

a=2/5 
print(a)

a=2//5 
print(a)

a=2%5 
print(a)

a=0
b= 3

print(a==b)
print(int(not b))


#Lecture 3
#if else
a=-5
b=14

if(a>b):
    print("Answer is A")
else:
    print("Answer is B")
    
    
if (a>0):
    print("positive")
elif(a==0):
    print("zero")

#while loop
#printing in the same line
n= 10
i= 1
sum=0
while(i<=n):
    print(i,end=" ")
    sum=sum+i
    i=i+1

print("\nSum is", sum)
#efficient way of calculating sum from 1 to n
sum=n*(n+1)/2
print(sum)



#sum of all even numbers
i=2
sum_even=0
while(i<=n):
    sum_even +=i
    i+=2

print(sum_even)

#prime or not
i=2
n=67
flag=0
while(i<n):
    if(n%i==0):
        flag=1
        print("Not prime")
        break
    i+=1
if (flag==0):
    print("Prime")

#patterns
print("PATTERN 1")
a= '*' * 4
i=1
while(i<5):
    print('*' * 4)
    i+=1


print("PATTERN 2")
#pattern2
n=3
i=0
while(i<n):
    print('*' * n)
    i+=1

print("PATTERN 3")
#pattern2
n=3
i=1
while(i<=n):
    print(str(i) * n)
    i+=1

#Lecture 4
print("PATTERN 4")
n = 3
i = 1
while(i<=n):
    j=1
    while(j<=n):
        print(j, end=" ")
        j+=1
    i+=1
    print("\n")


















