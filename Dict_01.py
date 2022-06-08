# WAP to create a dictionary that stores the information of a book like (title, author, price) by taking input from user and display the information
d={}
title=input("Enter title: ")
author=input("Enter author: ")
price=int(input("Enter price: "))
d.update({"title":title,"author":author,"price":price})
print(d)