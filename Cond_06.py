# WAP to accept an arithmetic operator and two integers and perform the input operation on integers
n1,n2=int(input('Enter num 1: ')),int(input('Enter num 2: '))
op=input('Enter operator: ')
if(op=='+'):
    print(n1+n2)
elif(op=='-'):
    print(n1-n2)
elif(op=='*'):
    print(n1*n2)
elif(op=='/'):
    print(n1/n2)
elif(op=='//'):
    print(n1//n2)
elif(op=='%'):
    print(n1%n2)