# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:12:33 2018

@author: beltramo
"""

print(1**2)
print(2**2)
print(3**2)
print(4**2)

def list_squares(n):
    "return a list of sqared numbers"
    lis=[]
    for i in range(1, n+1):
        lis.append(i**2)
    return(lis)
    
for i in list_squares(4):
    print(i)
