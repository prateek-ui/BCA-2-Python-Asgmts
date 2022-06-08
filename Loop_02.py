# WAP to swap first and last digit of a number
n=1234
last=n%10
first=n//pow(10,len(str(n))-1)
last*=pow(10,len(str(n))-1)
last+=n%pow(10,len(str(n))-1)
last//=10
last=last*10+first
print(last)