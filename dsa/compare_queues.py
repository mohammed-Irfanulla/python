queue1 = []
queue2 = []

n1 = int(input("Enter the number of elements in Queue 1: "))
print("Enter Queue 1 elements:")
for _ in range(n1):
    queue1.append(int(input()))

n2 = int(input("\nEnter the number of elements in Queue 2: "))
print("Enter Queue 2 elements:")
for _ in range(n2):
    queue2.append(int(input()))

if n1 != n2:
    print("\nQueues are Not Equal")
else:
    equal = all(q1 == q2 for q1, q2 in zip(queue1, queue2))
    if equal:
        print("\nQueues are Equal")
    else:
        print("\nQueues are Not Equal")
