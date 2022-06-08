# WAP to print first odd digit occurring in a number or else display proper error message
n=int(input("Enter number: "))
if n<0:
    n=-n
n=str(n)
n=int(n[::-1])
while n!=0:
    if((n%10)%2!=0):
        print(n%10)
        break
    n//=10
else:
    print("No odd digits found")