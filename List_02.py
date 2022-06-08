# WAP to concatenate two lists in the following order
ls1=["Hello","Take"]
ls2=["Dear","Sir"]
ls3=[]
for i in ls1:
    for j in ls2:
        ls3.append(i+' '+j)
print(ls3)