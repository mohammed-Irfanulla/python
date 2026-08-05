arr = []
for i in range(6):
    n = int(input(f"Enter element {i}: "))
    arr.append(n)
if arr:
    print("Smallest number:", min(arr))
else:
    print("No numbers entered")
