# WAP to accept 10 numbers in array and find maximum even and minimum odd number
from array import *
arr=array('i',[])
maxEven,maxOdd=0,0
for i in range(10):
    arr.append(int(input("Enter number: ")))
    if arr[i]%2==0 and maxEven<arr[i]:
        maxEven=arr[i]
    if arr[i]%2!=0 and maxOdd<arr[i]:
        maxOdd=arr[i]
print(maxEven, maxOdd)

