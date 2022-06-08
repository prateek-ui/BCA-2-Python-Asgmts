# Take three numbers and display the bigger number
n1,n2,n3=int(input('Enter num 1: ')),int(input('Enter num 2: ')),int(input('Enter num 3: '))
if n1>n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)