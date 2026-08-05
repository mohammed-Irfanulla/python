arr = []
even = 0
odd = 0
for i in range(5):
    n = int(input(f"Enter number {i}: "))
    arr.append(n)
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Array:", arr)
print("Even count:", even)
print("Odd count:", odd)
