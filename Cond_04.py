# Accept a 4-digit number and display the smallest digit
n=int(input('Enter a 4 digit number: '))
minDig=n%10
n//=10
while n!=0:
    if(minDig>n%10):
        minDig=n%10
    n//=10
print(minDig)