# WAP to check whether a given number is a 2-digit odd number or not
n=input('Enter number: ')
if len(n)!=2:
    print('Not a 2 digit number')
elif int(n)%2!=0:
        print('2 digit odd number')
else:
    print('Not a 2 digit odd number')