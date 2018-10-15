# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:12:33 2018

@author: beltramo
"""

def list_squares(n):
    lis=[]
    for i in range(1, n+1):
        lis.append(i**2)
    return(lis)

print (__name__)
if __name__ == "__main__": 
  for i in list_squares(4):
      print(i)

      