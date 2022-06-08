# WAP to find the last perfect number occurs before the entered number
n=int(input("Enter a number: "))
for i in range(n+1,1,-1):
    sum=0
    for j in range(1,(i//2)+1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)
        break