# WAP to copy the contents of one file to another
f1=open("file1.txt","r")
f2=open("file2.txt","w")
s=f1.read()
f2.write(s)
f1.close()
f2.close()