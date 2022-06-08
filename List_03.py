# WAP to find the list in a list of lists whose sum of elements is the highest
ls = [[23,41,7],[3,5,1],[42,-8,10]]
max=0
for i in ls:
    if max<sum(i):
        max=sum(i)
print(max)