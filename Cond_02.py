# Take two numbers from user and check whether the second number is the perfect divisor of the first
n1,n2=int(input("Enter number 1: ")),int(input("Enter number 2: "))
if n1%n2==0:
    print('Yes')
else:
    print('No')