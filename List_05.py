# WAP to create a matrix of 9 elements and display
# a. Maximum number
# b. Minimum number
# c. Maximum number of each row
# d. Minimum number of each row
ls = [[23,41,7],[3,-8,1],[42,2,10]]
ls1=[]
for i in ls:
    ls1.append(max(i))
print('Maximum: ',max(ls1))
ls1=[]
for i in ls:
    ls1.append(min(i))
print('Minimum: ',min(ls1))
print('Max of row 1:',max(ls[0]),'Max of row 2:',max(ls[1]),'Max of row 3:',max(ls[2]))
print('Max of row 1:',min(ls[0]),'Max of row 2:',min(ls[1]),'Max of row 3:',min(ls[2]))