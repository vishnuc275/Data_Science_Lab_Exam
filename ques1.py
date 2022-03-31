#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:57:23 2022

@author: sjcet
"""



import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("matrix 1:")
print(arr1)

arr2=np.array([[7,8,9],[1,3,7],[8,5,3]])
print("matrix 2:")
print(arr2)

print("substraction of matrices:")
print(arr1-arr2)

x=np.diag(arr1)
print("sum of diagonal elements of matrix 1 :",np.sum(x))

y=np.diag(arr2)
print("sum of diagonal elements of matrix 2 : ",np.sum(y))

