#             10 
#          20 30
#       40 50 60
#    70 80 90 100
s=4
n,m=10,1
for i in range(1,5):
    print('   '*s,end='')
    s-=1
    for j in range(1,i+1):
        print(str(n*m),end=' ')
        m+=1
    print()
