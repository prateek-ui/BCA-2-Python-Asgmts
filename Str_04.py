str=input("Enter string: ")
check1,check2,check3,check4=False,False,False,False
if len(str)>=10:
    for i in str:
        if i.islower():
            check1=True
        if i.isupper():
            check2=True
        if i.isdigit():
            check3=True
        if i=='@' or i=='$' or i=='*' or i=='_':
            check4=True         
    if (check1 and check2 and check3 and check4) == True:
        print("Password is valid")
    else:
        print("Password is invalid")    
else:
    print("Password is invalid")