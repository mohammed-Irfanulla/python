arr = []
for i in range(10):
    n = int(input(f"Enter element {i}: "))
    if n in arr:
        print("Duplicate!", n)
    else:
        arr.append(n)
print("Final array:", arr)
