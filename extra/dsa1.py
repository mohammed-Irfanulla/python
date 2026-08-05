'''creating basic array'''
# arr=[]
# start,stop=int(input("enter no1:")),int(input("enter no2:"))
# for i in range(start,stop+1):
#     arr.append(i)
#     print(arr[i],end=" ")

'''printing duplicate elements'''
# arr=[]
# count=0
# for i in range(0,10):
#     n=int(input(f"Enter the element{i}:"))
#     if n in arr:
#         print("duplicate!")
#     else:arr.append(n)
# print(arr)

'''printing 2nd largest no'''   
# arr=[]
# max=0
# max2=0
# for i in range(0,6):
#     n=int(input(f"Enter the element{i}:"))
#     arr.append(n)
#     if n>max:
#         max2=max
#         max=n
#     elif max2<n and max>n:
#         max2=n
# print(max,max2)

'''smallest no in array'''
# arr=[]
# min=0
# for i in range(0,6):
#     n=int(input(f"Enter the element{i}:"))
#     arr.append(n)

'''even and odd numbers in array'''
# arr=[]
# even=0
# odd=0
# for i in range(0,5):
#     n=int(input("enter no:"))
#     if n % 2==0:
#         even +=1
#     elif n % 2!=0:
#         odd+=1
#     arr.append(n)
# print(arr,even,odd)
'''reverse an array'''
'''binary search'''
# a=[]
# for i in range(0,int(input("Enter the range:")) ):
#     a.append(int(input("enter nos:")))
# print(a)

'''place all the starting zeros at the end of array'''
# a=[]
# zero=0
# for i in range(0,int(input("enter range:"))):
#     n=int(input("enter the no:"))
#     if n==0:
#         zero+=1
#     else:
#         a.append(n)
# for i in range(0,zero):
#     a.append(0)
# print(a)

'''reversing of string'''
# a=input("enter the string:")
# lst=[]
# for i in a:
#     lst.append(i)
# m=len(lst)
# for i in range(0,int(m/2)):
#     lst[i],lst[m-1]=lst[m-1],lst[i]
#     m -=1
# print("".join(lst))
'''          or               '''
# a=input("enter the string:")
# a=a[::-1]
# print(a)


'''check palindrom'''
# a=input("enter the string:")
# if a==a[::-1]:
#     print("yees")
# else:
#     print("no")

'''missing numbers'''
# lst=[]
# for i in range(0,int(input("enter the size:"))):
#     n=int(input("enter nos:"))
#     if i==0:
#         min=n
#         max=n
#     else:
#         if n>max:
#             max=n
#         elif n<min:
#             min=n
#     lst.append(n)
# for i in range(min,max+1):
#     if i not in lst:
#         print(i,end=" ")

'''frequency of character'''
# a=input("enter the string:")
# tar=input("enter the char:")
# count=0
# for i in a:
#     if i == tar:
#         count+=1
# print(count)

'''remove duplicates'''
# a=[]
# for i in range(int(input("size:"))):
#     n=input("enter the no:")
#     if n not in a:
#         a.append(n)
# print(" ".join(a))
'''or'''
# a=[]
# n=input("enter the no:").split()
# for item in n:
#     if item not in a:
#         a.append(item)
# print(" ".join(a))

'''anagram'''
# a=input("enter the string:")
# b=input("enter the string:")
# flag=0
# if len(a)==len(b):
#     for item in a:
#         if item not in b:
#             print("not")
#             flag=1
#             break
#     if flag==0:
#         print("Anagram")
# else:
#     print("not")

'''Rotate Array by K Positions'''
# a=input("enter the numbers:").split()
# rot=int(input("enter rot:"))
# b=a[-rot:] +a[:-rot]
# print(" ".join(b))

'''Longest Word in a Sentenc'''
# a=input("enter the string:").split()
# m=0
# b=""
# for item in a:
#     if len(item)>m:
#         m=len(item)
#         b=item
# print(b)

''' First Non-Repeating Character'''
# a=list(input("enter the string:"))
# for i in range(len(a)):
#     b=a[i]
#     a[i]=""
#     if b not in a:
#         print(b)
#         break
#     else:
#         a[i]=b

'''Count Vowels and Consonants'''
# a=input("enter the word:").lower().strip()
# vowels=0
# cons=0
# for i in a:
#     if i in "aeiou":
#         vowels+=1
#     else:
#         cons+=1
# print(vowels,cons)

''' Maximum Subarray Sum'''
# n=int(input("enter the size:"))
# a=[]
# for i in range(n):
#     a.append(int(input("enter the number:")))
# if a[::-1]7<0:
#     if (a)
#     a.remove(a)
# profit=0
# for i in range(len(a)):

# n = int(input("Enter number: "))
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(n))

# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# fibonacci(5)

# s = input("Enter sentence: ").lower().split()
# freq = {}
# for word in s:
#     freq[word] = freq.get(word, 0) + 1
# vowels = []
# consonants = []
# for word in s:
#     for ch in word:
#         if ch.isalpha():
#             if ch in "aeiou":
#                 vowels.append(ch)
#             else:
#                 consonants.append(ch)
# print("Word Frequency:", freq)
# print("Vowels:", vowels)
# print("Consonants:", consonants)

    
