# WAP to create a menu driven program for dictionary of countries and their capitals
d={"India":"Delhi","Netherlands":"Amsterdam","UAE":"Dubai"}
while True:
    print("Dictionary menu: ")
    print("1.Insert\n2.Update\n3.Delete\n4.Display\n5.Exit")
    c=int(input("Enter choice: "))
    if c==1:
        country=input("Enter country: ")
        capital=input("Enter capital: ")
        d.update({country:capital})
        print("Operation successful")
    elif c==2:
        country=input("Enter country name to update: ")
        d.update({country:input("Enter new capital: ")})
        print("Operation successful")
    elif c==3:
        d.pop(input("Enter country to delete: "))
        print("Operation successful")
    elif c==4:
        print(d)
    elif c==5:
        print("Exiting...")
        break
    else:
        print("Invalid input please enter choice again")
print(d)