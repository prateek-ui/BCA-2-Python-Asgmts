# Create a menu-driven program for various operations in an array
from array import *
arr=array('i',[1,2,3,4,5])
while(True):
    print("Select operation:")
    print("\n1.Insert\n2.Delete\n3.Print\n4.Search\n5.Exit")
    n=int(input("Enter choice: "))
    if n==1:
        print("Select sub-operation:")
        print("\n1.Insert at beginning\n2.Insert at end\n3.Insert at a position")
        n=int(input("Enter choice: "))
        if n==1:
            arr.insert(0,int(input("Enter number: ")))
            print("Operation successful")
        elif n==2:
            arr.append(int(input("Enter number: ")))
            print("Operation successful")
        elif n==3:
            arr.insert(int(input("Enter position(index): ")),int(input("Enter number: ")))
            print("Operation successful")
        else:
            print("Wrong input please enter correct choice")
    elif n==2:
        print("Select sub-operation:")
        print("\n1.Delete from last\n2.Delete a specific value\n3.Delete from a position")
        n=int(input("Enter choice: "))
        if n==1:
            arr.pop()
            print("Operation successful")
        elif n==2:
            arr.remove(int(input("Enter number: ")))
            print("Operation successful")
        elif n==3:
            arr.pop(int(input("Enter position(index): ")))
            print("Operation successful")
        else:
            print("Wrong input please enter correct choice")
    elif n==3:
        print(arr)
    elif n==4:
        index=arr.index(int(input("Enter number to search: ")))
        if(index>=0 and index<len(arr)):
            print("Number is present at",index,"index")
    elif n==5:
        print("Exiting...")
        break
    else:
        print("Wrong input please enter correct option")
