# Write a program to input a three-digit number and print its sum of digits
n=int(input('Enter a 3 digit number: '))
s=0
while n!=0:
   s+=n%10
   n//=10 
print(s)