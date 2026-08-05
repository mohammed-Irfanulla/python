# bitwise operation
# a=5
# b=3
# print(a&b)

# if conditioning
# a=(float)(input("Enter the time:"))
# if a>=9.15:
#     print("welcome")

# simple calculator using sring input
# a=input()
# print(eval(a))

# list and its methods
# lst1=["mango","kiwi","apple"]
# print(lst1[0:2]) #slicing
# print(lst1[::-1])#prints in reverse order

# prime number
# import math
# a=int(input("enter the no:"))
# for i in range(2,int(math.sqrt(a))):
#     if a % i == 0:
#         print("not prime")
#         break
# print("Prime")

# fibbonocci series
# n=int(input("enter the length of series:"))
# a=int(0)
# b=(int)(1)
# print(a,b,sep="\n")
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# armstrong number
# a = input("Enter the number")
# count = len(a)
# total = 0
# for n in a:
#     n = int(n)
#     total += n ** count
# print(total)
# if total == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# palindrome
# a=(input("enter no:"))
# b=a[::-1]
# print(a==b)

# square pattern 
# n=int(input("Enter no:"))
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ") 
#     print()

# def greet():
#     print("hiii")
# greet()

# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)
# print("Case-1:")
# nameAge("Olivia", 27)    

#factorial
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(int(input("Enter the no:"))))

#to reverse a num 1 to 10
# for i in range(10,0,-1):
#     print(i,end=" ")

#to count char in strings
# a=input("enter the string:")
# print("no of chars:",len(a))

#to check prime number
#import math
# a=int(input("enter the no:"))
# for i in range(2,int(math.sqrt(a))):
#     if a % i == 0:
#         print("not prime")
#         break
# print("Prime")

#to check vowels
# a=input("Enter the string:")
# count=int(0)
# for ch in a:
#     if ch.lower() in "aeiou":
#         count+=1
# print(count)

#to swap two number
# a=int(input("enter the no1:"))
# b=int(input("enter the no2:"))
# a=a+b
# b=abs(a-b)
# a=abs(a-b)
# print(a,b)

#create banking system
# amt = 5000
# def deposite(x):
#     global amt
#     amt+=abs(x)
#     return print("available amt:",amt)
# def withdraw(x):
#     global amt
#     if (amt-x)<300:
#         return (print("minimum bal amt to be 300!"))
#     else:
#         amt-=x
#         return print("available amt:",amt)
# # # def bal():
# # #     return print(amt)
# n='y'
# while n=='y':
#     ch=int(input("1.deposite 2.withdraw 3.balance:"))
#     if ch ==1:
#         deposite(int(input("enter amt:")))
#     elif ch==2:
#         withdraw(int(input("enter amt:")))
#     elif ch==3:
#         print(amt)
#     else:
#         print("invalid input")
#     n=input("do you want to continue? y/n:").lower()

#user input validation
# user="Raj_jas"
# pwd="Raj@123"
# user1=input("Enter user id:")
# pwd1=input("enter password:")
# if(user==user1 and pwd==pwd1):
#     print("welcome:",user1)
# else:
#     print("invalid credentials")
    
#generate employee id
# import random
# eid=random.randint(11111,29999)
# print(eid)

#password validation
# pwd=input("Enter the password:")
# lwcase=0
# upcase=0
# spc=0
# dig=0
# if len(pwd)>=8:
#     for i in pwd:
#         if i.isdigit():
#             dig+=1
#         elif i.isalpha():
#             if i.islower():
#                 lwcase+=1
#             if i.isupper():
#                 upcase+=1
#         else:
#             spc+=1
#     if(lwcase >1 and upcase>1  and spc>=1):
#         print("Strong password!")
#     else:
#         print("week password!")
# else:
#     print("password too short")

#generate strong password
import random
import string
lst=[]
count=1
for i in range(10):
    ch=int(random.randint(1,2))
    if ch ==1: 
        lst.append(random.choice(string.ascii_letters))
    elif ch==2:
        if count<=2:
            lst.append(random.choice("#_@$&"))
            count+=1
        else:
            lst.append(random.randint(1,9))
    else:
        lst.append(random.randint(1,9))
pwd="".join(str(item) for item in lst)
print("Your password is:",pwd)

