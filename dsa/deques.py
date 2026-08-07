'''implement dequeue operation in queue'''

# queue=list(map(int,input("enter elememts:").split()))
# if len(queue)==0:
#     print("queue underflow")
# else:
#     removed=queue.pop(0)
#     print(removed)
    # print(queue)



'''implement enqueue operation in queue'''
# queue = []

# n = int(input("Enter number of elements to insert: "))

# for i in range(n):
#     x = int(input("Enter element: "))
#     queue.append(x)    

# print("Queue after enqueue:", queue)
'''circular queue using list and operations of enqueue and dequeue'''
# size = int(input("Enter size of circular queue: "))

# queue = [None] * size
# front = -1
# rear = -1

# while True:
#     print("\n1. Enqueue")
#     print("2. Dequeue")
#     print("3. Display")
#     print("4. Exit")

#     ch = int(input("Enter your choice: "))

#     if ch == 1:
#         if (front == 0 and rear == size - 1) or (front == rear + 1):
#             print("Queue Overflow")

#         else:
#             x = int(input("Enter element: "))

#             if front == -1:
#                 front = rear = 0
#             elif rear == size - 1:
#                 rear = 0
#             else:
#                 rear += 1

#             queue[rear] = x
#             print("Inserted:", x)

#     elif ch == 2:
#         if front == -1:
#             print("Queue Underflow")

#         else:
#             print("Deleted:", queue[front])

#             if front == rear:
#                 front = rear = -1
#             elif front == size - 1:
#                 front = 0
#             else:
#                 front += 1
#     elif ch == 3:
#         if front == -1:
#             print("Queue is Empty")
#         else:
#             print("Queue Elements:", end=" ")
#             if front <= rear:
#                 for i in range(front, rear + 1):
#                     print(queue[i], end=" ")
#             else:
#                 for i in range(front, size):
#                     print(queue[i], end=" ")
#                 for i in range(0, rear + 1):
#                     print(queue[i], end=" ")
#             print()
#     elif ch == 4:
#         print("Program Ended")
#         break
#     else:
#         print("Invalid Choice")



'''reverse a queue'''
# queue = []

# n = int(input("Enter the number of elements: "))

# print("Enter queue elements:")

# for i in range(n):
#     element = int(input())
#     queue.append(element)

# print("Original Queue:")
# for i in range(n):
#     print(queue[i], end=" ")

# reverse_queue = []

# for i in range(n - 1, -1, -1):
#     reverse_queue.append(queue[i])

# print("\nReversed Queue:")
# for i in range(n):
#     print(reverse_queue[i], end=" ")

'''separate a elements of queue into even and odd'''

# queue = []
# even_queue = []
# odd_queue = []

# n = int(input("Enter the number of elements: "))

# print("Enter queue elements:")

# for i in range(n):
#     element = int(input())
#     queue.append(element)

# # Separate elements
# for i in range(n):
#     if queue[i] % 2 == 0:
#         even_queue.append(queue[i])
#     else:
#         odd_queue.append(queue[i])

# # Display Original Queue
# print("\nOriginal Queue:")
# for i in range(n):
#     print(queue[i], end=" ")

# # Display Even Queue
# print("\n\nEven Queue:")
# for i in range(len(even_queue)):
#     print(even_queue[i], end=" ")

# # Display Odd Queue
# print("\n\nOdd Queue:")
# for i in range(len(odd_queue)):
#     print(odd_queue[i], end=" ")
'''merge 2 queue into single queue while preserving the order of elements'''

queue1 = []
queue2 = []
merged_queue = []

# Input for Queue 1
n1 = int(input("Enter the number of elements in Queue 1: "))

print("Enter Queue 1 elements:")
for i in range(n1):
    element = int(input())
    queue1.append(element)

# Input for Queue 2
n2 = int(input("\nEnter the number of elements in Queue 2: "))

print("Enter Queue 2 elements:")
for i in range(n2):
    element = int(input())
    queue2.append(element)

# Copy Queue 1 into merged_queue
for i in range(n1):
    merged_queue.append(queue1[i])

# Copy Queue 2 into merged_queue
for i in range(n2):
    merged_queue.append(queue2[i])

# Display Queue 1
print("\nQueue 1:")
for i in range(n1):
    print(queue1[i], end=" ")

# Display Queue 2
print("\nQueue 2:")
for i in range(n2):
    print(queue2[i], end=" ")

# Display Merged Queue
print("\nMerged Queue:")
for i in range(len(merged_queue)):
    print(merged_queue[i], end=" ")
'''to compare 2 queue and determine they contain same element in same order'''
# Compare Two Queues

queue1 = []
queue2 = []

# Input for Queue 1
n1 = int(input("Enter the number of elements in Queue 1: "))

print("Enter Queue 1 elements:")
for i in range(n1):
    element = int(input())
    queue1.append(element)

# Input for Queue 2
n2 = int(input("\nEnter the number of elements in Queue 2: "))

print("Enter Queue 2 elements:")
for i in range(n2):
    element = int(input())
    queue2.append(element)

# Compare sizes
if n1 != n2:
    print("\nQueues are Not Equal")
else:
    equal = True

    # Compare each element
    for i in range(n1):
        if queue1[i] != queue2[i]:
            equal = False
            break

    if equal:
        print("\nQueues are Equal")
    else:
        print("\nQueues are Not Equal")
'''rotate a queue by k position '''
# Rotate Queue by K Positions

queue = []

n = int(input("Enter the number of elements: "))

print("Enter queue elements:")
for i in range(n):
    element = int(input())
    queue.append(element)

k = int(input("Enter K value: "))

# If K is greater than queue size
k = k % n

# Rotate the queue
for i in range(k):

    first = queue[0]

    # Shift elements to the left
    for j in range(n - 1):
        queue[j] = queue[j + 1]

    # Place first element at the end
    queue[n - 1] = first

print("\nQueue after rotation:")

for i in range(n):
    print(queue[i], end=" ")
'''to implement a customer servic queue 
1.add customer
2.servie customer 
3.waiting customer
4.display front customer
5.total customers'''
# Customer Service Queue

queue = []

while True:

    print("\n----- Customer Service Queue -----")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Waiting Customers")
    print("4. Display Front Customer")
    print("5. Display Total Customers")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Customer
    if choice == 1:

        customer = input("Enter Customer Name: ")
        queue.append(customer)
        print(customer, "added to the queue.")

    # Serve Customer
    elif choice == 2:

        if len(queue) == 0:
            print("No customers to serve.")

        else:
            print(queue[0], "has been served.")

            # Shift elements to the left
            for i in range(len(queue) - 1):
                queue[i] = queue[i + 1]

            queue.pop()

    # Display Waiting Customers
    elif choice == 3:

        if len(queue) == 0:
            print("No waiting customers.")

        else:
            print("Waiting Customers:")

            for i in range(len(queue)):
                print(queue[i])

    # Display Front Customer
    elif choice == 4:

        if len(queue) == 0:
            print("Queue is Empty")

        else:
            print("Front Customer:", queue[0])

    # Display Total Customers
    elif choice == 5:

        print("Total Customers:", len(queue))

    # Exit
    elif choice == 6:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")