# WAP to input an integer and replace all even digits with zero
n=input("Enter a number: ")
s=''
for i in str(n):
    if int(i)%2==0:
        s+='0'
    else:
        s+=i
print(int(s))