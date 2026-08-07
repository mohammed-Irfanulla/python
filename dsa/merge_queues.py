queue1 = []
queue2 = []
merged_queue = []

n1 = int(input("Enter the number of elements in Queue 1: "))
print("Enter Queue 1 elements:")
for _ in range(n1):
    queue1.append(int(input()))

n2 = int(input("\nEnter the number of elements in Queue 2: "))
print("Enter Queue 2 elements:")
for _ in range(n2):
    queue2.append(int(input()))

merged_queue = queue1 + queue2

print("\nQueue 1:")
for item in queue1:
    print(item, end=" ")

print("\nQueue 2:")
for item in queue2:
    print(item, end=" ")

print("\nMerged Queue:")
for item in merged_queue:
    print(item, end=" ")
