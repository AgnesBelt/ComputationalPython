# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:12:33 2018

@author: beltramo
"""

def list_powers(n, m):
    "return a list of powered numbers"
    lis=[]
    for i in range(1, n+1):
        lis.append(i**m)
    return(lis)
    
for i in list_powers(4, 3):
    print(i)
