queue = []

n = int(input("Enter number of elements to insert: "))

for _ in range(n):
    x = int(input("Enter element: "))
    queue.append(x)

print("Queue after enqueue:", queue)
