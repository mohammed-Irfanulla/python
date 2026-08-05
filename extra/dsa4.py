'''Singly linked list'''
# head = None
# current=None
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def insert(data):
#     global head
#     global current
#     if head is None:
#         head=Node(data)
#         current=head
#     else:
#         current.next = Node(data)
#         current= current.next
# def printnode():
#     trav = head
#     while trav != None:
#         print(trav.data,"-->",end="")
#         trav=trav.next
#     print("null")
# for i in range(5):
#     insert(int(input("Enter the node data:")))
# printnode()

'''doubly linked list insertion only'''
# head=None
# current=None
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def insertend(data):
#     global head
#     global current
#     if head is None:
#         head=Node(data)
#         current=head
#     else:
#         current.next = Node(data)
#         current= current.next
# def insertfront(data):
#     global head
#     global current
#     if head is None:
#         head=Node(data)
#         current=head
#     else:
#         nodeaddr = Node(data)
#         nodeaddr.next= head
#         head=nodeaddr
# def printnode():
#     trav = head
#     while trav != None:
#         print(trav.data,"-->",end="")
#         trav=trav.next
#     print("null")
# for i in range(5):
#     insertfront(int(input("Enter the node data at front:")))
#     insertend(int(input("Enter the node dataat end:")))
# printnode()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None

# n = int(input("Enter number of nodes: "))

# for i in range(n):
#     x = int(input("Enter data: "))
#     new = Node(x)

#     if head is None:
#         head = new
#     else:
#         temp = head
#         while temp.next is not None:
#             temp = temp.next
#         temp.next = new

# prev = None
# current = head

# while current is not None:
#     nxt = current.next
#     current.next = prev
#     prev = current
#     current = nxt

# head = prev

# print("Reversed Linked List:")
# temp = head
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")





# 2.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None

# n = int(input("Enter number of nodes: "))

# for i in range(n):
#     x = int(input("Enter data: "))
#     new = Node(x)

#     if head is None:
#         head = new
#     else:
#         temp = head
#         while temp.next:
#             temp = temp.next
#         temp.next = new

# if head is not None and head.next is not None:
#     secondLast = None
#     last = head

#     while last.next:
#         secondLast = last
#         last = last.next

#     secondLast.next = None
#     last.next = head
#     head = last

# print("Linked List:")
# temp = head
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")



# 3.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None

# n = int(input("Enter number of nodes: "))

# for i in range(n):
#     x = int(input("Enter data: "))
#     new = Node(x)

#     if head is None:
#         head = new
#     else:
#         temp = head
#         while temp.next:
#             temp = temp.next
#         temp.next = new

# slow = head
# fast = head

# while fast.next is not None and fast.next.next is not None:
#     slow = slow.next
#     fast = fast.next.next

# head1 = head
# head2 = slow.next
# slow.next = None

# print("First Half:")
# temp = head1
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")

# print("Second Half:")
# temp = head2
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")



# 4.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None

# n = int(input("Enter number of nodes: "))

# for i in range(n):
#     x = int(input("Enter data: "))
#     new = Node(x)

#     if head is None:
#         head = new
#     else:
#         temp = head
#         while temp.next:
#             temp = temp.next
#         temp.next = new

# sum = 0
# temp = head

# while temp:
#     sum += temp.data
#     temp = temp.next

# print("Sum =", sum)



# 5.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None

# n = int(input("Enter number of nodes: "))

# for i in range(n):
#     x = int(input("Enter data: "))
#     new = Node(x)

#     if head is None:
#         head = new
#     else:
#         temp = head
#         while temp.next:
#             temp = temp.next
#         temp.next = new

# key = int(input("Enter node to delete: "))

# if head is not None and head.data == key:
#     head = head.next
# else:
#     prev = None
#     temp = head

#     while temp is not None and temp.data != key:
#         prev = temp
#         temp = temp.next

#     if temp is None:
#         print("Node not found")
#     else:
#         prev.next = temp.next

# print("Linked List:")
# temp = head
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")



