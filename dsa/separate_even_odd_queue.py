queue = []
even_queue = []
odd_queue = []

n = int(input("Enter the number of elements: "))

print("Enter queue elements:")
for _ in range(n):
    element = int(input())
    queue.append(element)

for item in queue:
    if item % 2 == 0:
        even_queue.append(item)
    else:
        odd_queue.append(item)

print("\nOriginal Queue:")
for item in queue:
    print(item, end=" ")

print("\n\nEven Queue:")
for item in even_queue:
    print(item, end=" ")

print("\n\nOdd Queue:")
for item in odd_queue:
    print(item, end=" ")
