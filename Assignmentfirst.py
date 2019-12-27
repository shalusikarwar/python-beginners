#Write a programe of python for taking two input from user and perform
#addition,substraction,multiplication,and divide operation on input

#solution
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
add=num1+num2
print(add)
sub=num1-num2
print(sub)
mul=num1*num2
print(mul)
div=num1/num2
print(div)

#*******************************************************************************************************

#Write a program to check given input is integer or not

#solution
"""a=input("enter the number")
if (a.isdigit()):
 print("number is integer")
else:
 print("not integer")"""
a=int(input("enter the value"))
b=input("enter the second value")
if type(a)==type(b):
 print(" integer")
else:
 print("not integer")

#*********************************************************************************************
#Write a programe to check given input is the list item or not

#solution
list=["banana","apple","kiwi","orangre"]
a=input("enter the item")
"""if a==list[0]:
    print("item in list")
elif a==list[1]:
    print("item in list at 2")
elif a==list[2]:
    print("item in list at 3")
elif a==list[3]:
    print("item in list at 4")
else:
    print("item is not in list")"""
if a in list:
 print("element is exits")
else:
 print("not")

#*******************************************************************************************************

#Write a program for taking the value from user  in list such as your name ,class
#rolln no,college number,branch and to print all of this value in one line print function

#solution
name=input("enter the name")
Class=int(input("enter class"))
roll_no=int(input("enter roll number"))
clg=str(input("enter clg name"))
branch=str(input("enter the branch name"))
thislist=list((name,Class,roll_no,clg,branch))
print(thislist)
print(name,Class,roll_no,clg,branch)
