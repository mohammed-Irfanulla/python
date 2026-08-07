queue = []

n = int(input("Enter the number of elements: "))

print("Enter queue elements:")
for _ in range(n):
    element = int(input())
    queue.append(element)

print("Original Queue:")
for item in queue:
    print(item, end=" ")

reverse_queue = []
for i in range(n - 1, -1, -1):
    reverse_queue.append(queue[i])

print("\nReversed Queue:")
for item in reverse_queue:
    print(item, end=" ")
