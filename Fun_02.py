# Make a function which will take a number and return its sum of digits using recursion
def sumDig(num):
    s=0
    if num==0:
        return 0
    else:
        return num % 10 + sumDig(num//10) 
print(sumDig(123))