# WAP to accept 10 numbers in an array and find the sum of all prime numbers
from array import *
arr=array('i',[])
sum=0
for i in range(10):
    arr.append(int(input("Enter number: ")))
    if arr[i]<=1:
        continue
    for j in range(2,int((arr[i]/2)+1)):
        if arr[i]%j==0:
            break
    else:
        sum+=arr[i]
print(sum)