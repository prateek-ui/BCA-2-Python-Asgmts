# WAP to create a matrix of 9 elements and sort every row in descending order
ls = [[23,41,7],[3,5,1],[42,-8,10]]
for i in ls:
    i.sort(reverse=True)
print(ls)