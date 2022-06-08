# WAP to find all pairs of elements in an integer array whose sum is equal to a given number
from array import *
arr = array('i',[2,4,5,6,7])
num = int(input("Input num: "))
for i in range(len(arr)):
    tmp = arr[i]
    for j in range(len(arr)):
        if(i!=j and tmp+arr[j]==num):
            print(tmp,'+',arr[j],'=',num)