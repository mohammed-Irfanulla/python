queue = []

n = int(input("Enter the number of elements: "))
print("Enter queue elements:")
for _ in range(n):
    queue.append(int(input()))

k = int(input("Enter K value: "))
k = k % n

for _ in range(k):
    first = queue.pop(0)
    queue.append(first)

print("\nQueue after rotation:")
for item in queue:
    print(item, end=" ")
