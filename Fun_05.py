# Make a function which will take two arguments, a list and an int and find the occurrence of that integer value in the list and return the result
def occurence(ls,num):
    return ls.count(num)
print(occurence([1,4,9,1,0,1,3,4],4))