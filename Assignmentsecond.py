#Q1 factorial of any number n is represented by n!and is is equal to 1*2*3....(n-1)*n

#Answer
number=int(input("enter the number"))
p=1
for i in range(1,number+1):
 p=p*i
print(p)

#Q2 Take 10 integer fron keyboard using loop and print their average value on the screen

#Answer
a=0
for i in range(1,10+1):
    p=int(input("enter the number"))
    a=a+p
print("average is ",a/10)


#Q3 Write a progran for finding even number between 1 to 100

#Answer
for i in range(1,100+1):
    if i%2==0:
        print(i)
    else:
        ("no")

#Q4 Write a program for printing a table by user input number in the following order
   #2*1=2
   #2*2=4
   #then sum is 2+1=3

 #Answer
tab=int(input("enter the value"))
a=1
b=0
for i in range(1,10+1):
    a=tab*i
    b=a+b
    print(tab,"*",i,"=",a)
print("sum is ",b)

