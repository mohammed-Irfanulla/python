# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Create nodes
# node1 = Node(15)
# node2 = Node(3)
# node3 = Node(17)
# node4 = Node(90)

# # Link nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4  


# head = node1  # Head points to the first node

# # Traverse and print the linked list
# current = head
# while current:
#     print(current.data, end=" -> ")
#     current = current.next
# print("None")

'''linked list'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head = None
current=None
def insert(data):
    if head is not None:
        head=Node(data)
        current=head
    else:
        current.next = Node(data)
        current= current.next
def printnode():
    trav = head
    while trav.next != None:
        print(trav,"-->")
        trav=trav.next
for i in range(5):
    insert(int(input("Enter the node data")))

printnode()

'''pair of number == sum'''
# n = int(input("enter the size of array:"))
# a = []
# sum=int(input("enter the sum:"))
# for i in range(n):
#     a.append(int(input("enter the no:")))
# for i in range(n-1):
#     for j in range(i+1,n):
#         if a[i]+a[j] == sum:
#             print(a[i],a[j])
      
'''sort the array of without built-in'''

'''union of 2 array'''
# a=((input("enter the numbers string:"))).split()
# b=((input("enter the nums string:"))).split()
# union=[]
# for item in a:
#     if item not in union:
#         union.append(item)
# for item in b:
#     if item not in union:
#         union.append(item)
# print(" ".join(union))

'''or'''
# a=((input("enter the numbers string:"))).split()
# b=((input("enter the nums string:"))).split()
# union=[]
# for item in a:
#     if item not in union:
#         union.append(item)
#     if item in b:
#         b.remove(item)
# union.append(" ".join(b))
# print(" ".join(union))

'''find the 1st non repeating element in a array'''
# a=list(input("enter the string:"))
# for i in range(len(a)):
#     b=a[i]
#     a[i]=""
#     if b not in a:
#         print(b)
#         break
#     else:
#         a[i]=b
'''rearrange the array such that positive and negative numbers alternate'''
# def rearrange_alternating(arr):
#     pos = [x for x in arr if x >= 0]
#     neg = [x for x in arr if x < 0]
    
#     result = []
#     i, j = 0, 0
    
#     while i < len(pos) and j < len(neg):
#         result.append(pos[i])
#         result.append(neg[j])
#         i += 1
#         j += 1
        
#     result.extend(pos[i:])
#     result.extend(neg[j:])
    
#     return result

# # Example usage:
# arr = [1, 2, 3, -4, -1, 4]
# print(rearrange_alternating(arr))