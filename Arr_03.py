# WAP to find the intersection of two arrays
from array import *
arr1=[1,2,3,4,5]
arr2=[11,2,33,4,5]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            print(arr1[i])